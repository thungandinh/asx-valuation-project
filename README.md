# ASX Equity Valuation & Financial Health Dashboard 📈

An interactive, web-based quantitative finance dashboard built with **Python**, **Streamlit**, and **Plotly**. This application automates real-time financial data retrieval, valuation modeling, and key accounting health checks for companies listed on the Australian Securities Exchange (ASX).

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://asx-valuation-dashboard.streamlit.app)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Live Demo
You can access the live, interactive web application here: 
👉 [ASX Valuation Dashboard on Streamlit](https://asx-valuation-project-wggvc6gztdlao58mmgfkph.streamlit.app/)

## 🌟 Key Features

- **Real-Time Market Data Integration:** Dynamically fetches financial data, historical price trends, and fundamental metrics directly via `yfinance`.
- **Automated Valuation Models:**
  - **Dividend Discount Model (DDM):** Single-stage DDM calculation with sensitivity options.
  - **Capital Asset Pricing Model (CAPM):** Dynamic $r_e$ (Cost of Equity) derivation using beta and risk-free rates.
- **Financial Health & Multiples Screening:** Interactive key ratios breakdown including P/E, P/B, EV/EBITDA, and Return on Equity (ROE).
- **Interactive Visualizations:** Time-series stock price charts and historical performance plots powered by `Plotly`.
- **Responsive Web Interface:** Deployed as a lightweight, user-friendly interactive web application using `Streamlit`.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.9+
- **Frontend / Framework:** Streamlit
- **Data Manipulation & Analytics:** Pandas, NumPy
- **Financial Data Provider:** `yfinance`
- **Data Visualization:** Plotly Express / Plotly Graph Objects

---

## 📁 Repository Structure

```text
asx-valuation-project/
│
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python package dependencies
├── README.md               # Project documentation
└── data/                   # (Optional) Benchmark or static data resources
```

---

## 🚀 Local Installation & Quickstart

To run this dashboard locally on your machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/thungandinh/asx-valuation-project.git
   cd asx-valuation-project
   ```

2. **Create and Activate a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # venv\Scripts\activate   # On Windows
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

5. **Access the Dashboard:**
   Open your browser and navigate to `http://localhost:8501`.

---

## 📊 Usage & How It Works

1. Enter any valid **ASX Ticker Symbol** (e.g., `BHP.AX`, `CBA.AX`, `TLS.AX`) in the sidebar search box.
2. View real-time pricing, historical performance, and company key metrics.
3. Adjust valuation parameters (e.g., Growth Rate $g$, Risk-Free Rate $R_f$) to run real-time dynamic sensitivity analyses.

---

## 👤 Author

**Ngan Dinh**  
*Bachelor of Commerce (Finance & Business Analytics) Student at The University of Sydney (USYD)*  
- **GitHub:** [@thungandinh](https://github.com/thungandinh)
- **LinkedIn:** [Connect on LinkedIn](https://www.linkedin.com/)

---
*Feel free to star ⭐️ this repository if you find it helpful!*me.md…]()
