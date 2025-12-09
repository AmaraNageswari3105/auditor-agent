# Auditor Agent - Deployment Guide

## 🚀 Complete Deployment Instructions

This guide provides step-by-step instructions to deploy the Auditor Agent application to production with both backend and frontend components.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Backend Deployment](#backend-deployment)
3. [Frontend Deployment](#frontend-deployment)
4. [Integration & Testing](#integration--testing)
5. [Public Access](#public-access)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- Python 3.9+
- Node.js 16+
- pip (Python package manager)
- npm (Node package manager)
- Google Gemini API Key (free tier available)
- Git
- Server/Hosting account (Heroku, Render, AWS, Google Cloud, etc.)

---

## Backend Deployment

### Step 1: Clone the Repository
```bash
git clone https://github.com/AmaraNageswari3105/auditor-agent.git
cd auditor-agent/backend
```

### Step 2: Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the backend folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///fraud_detection.db
CORS_ORIGINS=http://localhost:3000,https://app.auditor-agent.com
PORT=8000
```

### Step 5: Run FastAPI Server Locally
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### Step 6: Deploy to Production

#### Option A: Deploy to Render
1. Push code to GitHub
2. Go to render.com and create new Web Service
3. Connect your GitHub repository
4. Set environment variables in Render dashboard
5. Deploy automatically from main branch
6. Backend URL: `https://auditor-agent-api.onrender.com`

#### Option B: Deploy to Heroku
```bash
heroku login
heroku create auditor-agent-api
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

---

## Frontend Deployment

### Step 1: Install Dependencies
```bash
cd ../frontend
npm install
```

### Step 2: Create .env File
Create `.env` file in frontend folder:
```
REACT_APP_API_URL=http://localhost:8000
```

For production:
```
REACT_APP_API_URL=https://auditor-agent-api.onrender.com
```

### Step 3: Build React App
```bash
npm run build
```

### Step 4: Test Locally
```bash
npm start
```

Access at: `http://localhost:3000`

### Step 5: Deploy Frontend

#### Option A: Deploy to Vercel (Recommended for React)
```bash
npm install -g vercel
vercel login
vercel
```

Your frontend will be at: `https://auditor-agent.vercel.app`

#### Option B: Deploy to Netlify
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod --dir=build
```

---

## Integration & Testing

### 1. Test File Upload
- Go to frontend: `https://auditor-agent.vercel.app`
- Click "Upload CSV File"
- Select sample transaction CSV
- Verify results display correctly

### 2. Test API Endpoints
```bash
curl -X POST http://localhost:8000/analyze \
  -F "file=@sample_transactions.csv"
```

### 3. Sample CSV Format
```csv
Transaction_ID,Vendor_Name,Amount,Department,Date
T001,Vendor A,50000,Finance,2024-01-15
T002,Vendor B,150000,IT,2024-01-16
```

---

## Public Access

### Full Stack URLs (After Deployment)
- **Frontend**: https://auditor-agent.vercel.app
- **Backend API**: https://auditor-agent-api.onrender.com
- **API Documentation**: https://auditor-agent-api.onrender.com/docs

### How Public Users Access:
1. Government auditors visit the frontend URL
2. Upload CSV file with transaction data
3. System analyzes and flags suspicious transactions
4. Download compliance report as PDF

---

## Troubleshooting

### Backend Issues
- "Module not found": Run `pip install -r requirements.txt` again
- "GEMINI_API_KEY not set": Check .env file configuration
- "CORS error": Update CORS_ORIGINS in environment variables

### Frontend Issues
- "API not responding": Verify REACT_APP_API_URL is correct
- "Blank page": Check browser console for errors
- "Upload fails": Ensure CSV format matches expected structure

### Deployment Issues
- "Build fails": Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- "Timeout errors": Check server logs on hosting platform

---

## Production Checklist

- [ ] Database backup configured
- [ ] API rate limiting enabled
- [ ] HTTPS/SSL certificate installed
- [ ] Environment variables secured
- [ ] Error logging configured
- [ ] CORS properly configured
- [ ] File upload size limits set
- [ ] Performance monitoring enabled

---

## Support

For issues, check GitHub: https://github.com/AmaraNageswari3105/auditor-agent

---

## License

MIT License - See LICENSE file for details
