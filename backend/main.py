# backend/main.py - FastAPI Backend for Auditor Agent
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import io
import datetime as dt
from datetime import timedelta
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Auditor Agent API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

def compute_anomaly_scores(df):
    """Compute risk scores for transactions"""
    df = df.copy()
    
    required_cols = ["transaction_id", "department", "vendor", "amount", "date", "time"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    df["date"] = pd.to_datetime(df["date"])
    try:
        df["time"] = pd.to_datetime(df["time"], format="%H:%M").dt.time
        df["datetime"] = df.apply(
            lambda r: dt.datetime.combine(r["date"].date(), r["time"]), axis=1
        )
    except:
        df["datetime"] = df["date"]
    
    df["amount"] = df["amount"].astype(float)
    dept_stats = df.groupby("department")["amount"].agg(["mean", "std"]).reset_index()
    df = df.merge(dept_stats, on="department", how="left", suffixes=("", "_dept"))
    df["std"] = df["std"].replace(0, 1)
    df["amount_zscore"] = (df["amount"] - df["mean"]) / df["std"]
    df["amount_zscore"] = df["amount_zscore"].fillna(0).abs()
    
    df["weekday"] = df["datetime"].dt.weekday
    df["is_weekend"] = df["weekday"].isin([5, 6]).astype(int)
    
    df["hour"] = df["datetime"].dt.hour
    df["is_odd_hour"] = ((df["hour"] < 8) | (df["hour"] > 19)).astype(int)
    
    df = df.sort_values("datetime").reset_index(drop=True)
    df["vendor_count_7d"] = 0
    for vendor in df["vendor"].unique():
        mask = df["vendor"] == vendor
        vendor_df = df[mask].copy()
        for idx in vendor_df.index:
            t = df.loc[idx, "datetime"]
            window = (df["datetime"] >= t - pd.Timedelta(days=7)) & (df["datetime"] <= t)
            df.loc[idx, "vendor_count_7d"] = window.sum()
    
    risk_score = np.zeros(len(df))
    risk_score += np.clip(df["amount_zscore"] / 4, 0, 1) * 0.40
    risk_score += df["is_weekend"] * 0.20
    risk_score += df["is_odd_hour"] * 0.20
    risk_score += np.clip((df["vendor_count_7d"] - 2) / 10, 0, 1) * 0.20
    
    risk_score = np.clip(risk_score, 0, 1)
    df["risk_score"] = risk_score
    df["risk_label"] = pd.cut(
        df["risk_score"],
        bins=[-0.01, 0.35, 0.65, 1.0],
        labels=["Low", "Medium", "High"]
    )
    
    return df

@app.get("/health")
async def health():
    return {"status": "Auditor Agent API Running"}

@app.post("/analyze")
async def analyze_transactions(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df_raw = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        
        required_cols = ["transaction_id", "department", "vendor", "amount", "date", "time"]
        missing_cols = [col for col in required_cols if col not in df_raw.columns]
        if missing_cols:
            raise HTTPException(
                status_code=400,
                detail=f"Missing columns: {', '.join(missing_cols)}"
            )
        
        df_scored = compute_anomaly_scores(df_raw)
        
        total_txns = len(df_scored)
        high_risk = len(df_scored[df_scored["risk_label"] == "High"])
        medium_risk = len(df_scored[df_scored["risk_label"] == "Medium"])
        low_risk = len(df_scored[df_scored["risk_label"] == "Low"])
        
        high_risk_amount = float(df_scored[df_scored["risk_label"] == "High"]["amount"].sum())
        avg_risk_score = float(df_scored["risk_score"].mean())
        
        top_dept = df_scored[df_scored["risk_label"] == "High"].groupby("department")["amount"].sum()
        top_dept_name = str(top_dept.idxmax()) if len(top_dept) > 0 else "N/A"
        
        top_vendor_counts = df_scored[df_scored["risk_label"] == "High"]["vendor"].value_counts()
        top_vendor_name = str(top_vendor_counts.idxmax()) if len(top_vendor_counts) > 0 else "N/A"
        
        high_risk_data = df_scored[df_scored["risk_label"] == "High"][
            ["transaction_id", "department", "vendor", "amount", "risk_score"]
        ].head(50).to_dict(orient="records")
        
        return {
            "status": "Analysis Complete",
            "summary": {
                "total_transactions": int(total_txns),
                "high_risk_count": int(high_risk),
                "medium_risk_count": int(medium_risk),
                "low_risk_count": int(low_risk),
                "high_risk_amount": high_risk_amount,
                "avg_risk_score": avg_risk_score,
                "top_flagged_department": top_dept_name,
                "top_flagged_vendor": top_vendor_name,
            },
            "risk_distribution": {
                "High": int(high_risk),
                "Medium": int(medium_risk),
                "Low": int(low_risk),
            },
            "high_risk_transactions": high_risk_data,
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
