# 🖥️ Running Auditor Agent on Your Local Machine

## Complete Step-by-Step Guide for Windows, Mac, and Linux

---

## Prerequisites

Before you start, make sure you have installed:

1. **Python 3.9+** → Download from https://www.python.org/downloads/
2. **Node.js 16+** → Download from https://nodejs.org/
3. **Git** → Download from https://git-scm.com/
4. **Google Gemini API Key** (Free) → Get from https://aistudio.google.com/app/apikeys
5. **VS Code or any code editor** (Optional but recommended)

### Check if installed:
```bash
python --version
node --version
npm --version
git --version
```

---

## Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/AmaraNageswari3105/auditor-agent.git
cd auditor-agent
```

---

## Step 2: Set Up Backend (FastAPI Server)

### 2.1 Navigate to Backend Folder
```bash
cd backend
```

### 2.2 Create Python Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ You'll see `(venv)` at the start of your terminal line once activated.

### 2.3 Install Backend Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- FastAPI (web framework)
- Uvicorn (server)
- Pandas (data processing)
- Google Generative AI
- Python-multipart (file uploads)
- Scikit-learn (anomaly detection)
- And more...

### 2.4 Create .env File

Create a file named `.env` in the `backend` folder:

```bash
# Windows: Use Notepad
type nul > .env

# Mac/Linux: Use terminal
touch .env
```

Open `.env` and add:
```
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///fraud_detection.db
CORS_ORIGINS=http://localhost:3000,http://localhost:5000
PORT=8000
```

**To get your Gemini API Key:**
1. Go to https://aistudio.google.com/app/apikeys
2. Click "Create API key"
3. Copy the key and paste it in .env

### 2.5 Run Backend Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend is running! Open: http://localhost:8000
✅ API Docs available at: http://localhost:8000/docs

**Keep this terminal open!**

---

## Step 3: Set Up Frontend (React)

### 3.1 Open New Terminal/Command Prompt

Navigate to frontend folder (from project root):
```bash
cd frontend
```

### 3.2 Install Frontend Dependencies
```bash
npm install
```

This installs React and all required packages.

### 3.3 Create .env File

Create `.env` in the `frontend` folder:

**Windows (Notepad):**
```bash
type nul > .env
```

**Mac/Linux (Terminal):**
```bash
touch .env
```

Add this content:
```
REACT_APP_API_URL=http://localhost:8000
```

### 3.4 Run Frontend
```bash
npm start
```

✅ Frontend opens automatically at: http://localhost:3000

**Keep this terminal open too!**

---

## Step 4: Test Your Application

### 4.1 Access the Application
Go to: **http://localhost:3000**

You should see:
- 🔍 Auditor Agent header
- 📤 Upload CSV File button
- Professional purple gradient design

### 4.2 Test with Sample Data

Create a file named `test_data.csv` in your project:

```csv
Transaction_ID,Vendor_Name,Amount,Department,Date
T001,Normal Vendor,5000,Finance,2024-01-15
T002,Suspicious Vendor,500000,IT,2024-01-16
T003,Regular Vendor,10000,HR,2024-01-17
T004,Fraud Corp,1000000,Procurement,2024-01-18
T005,Good Vendor,25000,Finance,2024-01-19
```

### 4.3 Upload and Analyze

1. Click "📤 Upload CSV File"
2. Select `test_data.csv`
3. Wait 2-3 seconds for analysis
4. See results with:
   - Total transactions
   - Flagged transactions
   - Risk score
   - AI explanations from Gemini

---

## Folder Structure

```
audit or-agent/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env (CREATE THIS)
│   └── venv/ (AUTO CREATED)
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.jsx
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── .env (CREATE THIS)
│   └── node_modules/ (AUTO CREATED)
│
└── README.md
```

---

## 🚀 Quick Start (One-Time Setup)

### Terminal 1 - Backend:
```bash
cd auditor-agent/backend
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

### Terminal 2 - Frontend:
```bash
cd auditor-agent/frontend
npm install
npm start
```

**Both running? Open http://localhost:3000 ✅**

---

## Next Time (Without Setup)

### Terminal 1:
```bash
cd auditor-agent/backend
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
uvicorn main:app --reload
```

### Terminal 2:
```bash
cd auditor-agent/frontend
npm start
```

---

## Troubleshooting

### Problem: "venv is not recognized"
**Solution:** Make sure you're in the `backend` folder and run activation command again.

### Problem: "pip install fails"
**Solution:** 
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: "npm install fails"
**Solution:**
```bash
rm -rf node_modules package-lock.json
npm install
```

### Problem: "Port 8000 already in use"
**Solution:** Change port in backend:
```bash
uvicorn main:app --reload --port 8001
```
Then update frontend `.env` to:
```
REACT_APP_API_URL=http://localhost:8001
```

### Problem: "GEMINI_API_KEY not set"
**Solution:**
1. Get key from https://aistudio.google.com/app/apikeys
2. Add to `.env` file in backend folder
3. Restart backend server

### Problem: "Blank white screen on localhost:3000"
**Solution:**
1. Check browser console (F12)
2. Check if backend is running
3. Check .env file has correct API_URL

---

## Important Notes

✅ **Always activate venv before running backend**
✅ **Keep both terminals running**
✅ **Never commit .env file to GitHub**
✅ **Make sure Gemini API key has free tier enabled**
✅ **Use Chrome/Firefox for best experience**

---

## Need Help?

Check the files:
- `DEPLOYMENT.md` - For production deployment
- `README.md` - For project overview
- Backend logs - Check terminal for errors
- Browser console (F12) - Check frontend errors

---

## Success! 🎉

You now have a fully running AI-powered fraud detection system on your local machine!

Next steps:
- Test with different CSV files
- Modify the code and see changes (hot reload enabled)
- Prepare for Google Agrnthon submission
