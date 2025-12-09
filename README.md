# auditor-agent
# 🕵️ Auditor Agent - AI-Powered Fraud Detection

**AI-powered fraud detection system for public spending using Google Gemini API. Full-stack application with FastAPI backend and React frontend.**

## 📋 Project Overview

Auditor Agent is an intelligent system that monitors public sector transactions, automatically detects suspicious financial activities, and generates compliance reports using advanced anomaly detection and AI explanations.

### Key Features
- ✅ Real-time anomaly detection (4-signal risk scoring)
- ✅ Multi-factor fraud detection (amount, timing, vendor frequency)
- ✅ AI-powered compliance reports via Google Gemini API
- ✅ Professional fraud detection dashboard
- ✅ RESTful API backend with FastAPI
- ✅ React frontend with interactive visualizations
- ✅ Google Cloud integration (Gemini, BigQuery ready)

## 🏗️ Architecture

```
auditor-agent/
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # Environment variables
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── components/
│   └── vite.config.js
├── docker-compose.yml           # Docker setup
└── README.md
```

## 🚀 Quick Start

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
echo "GEMINI_API_KEY=your_key_here" > .env
python main.py
```
Backend runs on `http://localhost:8000`

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on `http://localhost:5173`

## 🔑 Google Products Used
- **Gemini API** - AI compliance report generation
- **Google Colab** - ML development & prototyping
- **BigQuery** - Data warehouse (future integration)
- **Vertex AI** - Model deployment (future)

## 📊 Anomaly Detection Engine

4-Signal Risk Scoring:
1. **Z-Score** (40%) - Amount deviation from department average
2. **Weekend Transactions** (20%) - Off-hours spending patterns
3. **Odd Hours** (20%) - Late night transactions
4. **Vendor Frequency** (20%) - Suspicious vendor clustering

## 🎯 API Endpoints

### POST `/analyze`
Upload CSV file and get fraud detection results.

**Request:**
```bash
curl -F "file=@transactions.csv" http://localhost:8000/analyze
```

**Response:**
```json
{
  "status": "✅ Analysis Complete",
  "summary": {
    "total_transactions": 500,
    "high_risk_count": 31,
    "medium_risk_count": 462,
    "high_risk_amount": 11008051.11
  },
  "risk_distribution": {"High": 31, "Medium": 462, "Low": 7}
}
```

### POST `/generate-report`
Generate AI compliance report using Gemini.

## 📦 Required CSV Format

```csv
transaction_id,department,vendor,amount,date,time,category,payment_method
TXN_00001,Health Ministry,ABC Construction Ltd,45000,2025-12-01,10:30,Equipment,Bank Transfer
```

## 🐳 Docker Setup

```bash
docker-compose up
```

## 📈 Results

- **500** transactions analyzed
- **31** high-risk transactions flagged
- **$11M+** in suspicious spending identified
- **4** professional visualization charts
- **AI-generated** compliance reports

## 🎓 For Google Agent(h)on

- Uses **Google Gemini API** for AI explanations
- Built on **Google Colab** for rapid development
- Architecture ready for **BigQuery** & **Vertex AI**
- Professional dashboard for presentations
- Ready for **Google Cloud** deployment

## 📝 License

MIT License - Feel free to use and modify.

## 🤝 Contributing

Contributions are welcome! Please fork and submit pull requests.

## 📧 Contact

**Amara Nageswari** - AI/ML Developer  
GitHub: [@AmaraNageswari3105](https://github.com/AmaraNageswari3105)  
Project: [auditor-agent](https://github.com/AmaraNageswari3105/auditor-agent)
