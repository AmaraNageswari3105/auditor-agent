import React, { useState, useRef } from 'react';
import './App.css';

const App = () => {
  const [transactions, setTransactions] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setLoading(true);
    setError(null);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) throw new Error('Upload failed');
      const data = await response.json();
      setResults(data);
      setTransactions(data.transactions);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const triggerFileInput = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="container">
      <header className="header">
        <h1>🔍 Auditor Agent</h1>
        <p>AI-Powered Fraud Detection for Public Spending</p>
      </header>

      <section className="upload-section">
        <button className="upload-btn" onClick={triggerFileInput}>
          📤 Upload CSV File
        </button>
        <input
          ref={fileInputRef}
          type="file"
          accept=".csv"
          onChange={handleFileUpload}
          style={{ display: 'none' }}
        />
      </section>

      {loading && <div className="spinner">Analyzing transactions...</div>}
      {error && <div className="error">Error: {error}</div>}

      {results && (
        <section className="results">
          <h2>Analysis Results</h2>
          <div className="summary">
            <div className="stat">Total: {results.total_transactions}</div>
            <div className="stat red">Flagged: {results.flagged_count}</div>
            <div className="stat">Risk Score: {results.risk_score?.toFixed(2)}</div>
          </div>
          <div className="report" dangerouslySetInnerHTML={{ __html: results.compliance_report }} />
        </section>
      )}
    </div>
  );
};

export default App;
