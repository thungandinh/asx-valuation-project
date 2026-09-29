import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

# 1. Cấu hình trang web
st.set_page_config(page_title="ASX Valuation Tool", page_icon="📊", layout="wide")

st.title("📊 ASX Equity Valuation Dashboard")
st.write("Dự án phân tích Sức khỏe Tài chính & Định giá Cổ phiếu (ASX)")

# Sidebar
st.sidebar.header("🔍 Cấu hình")
ticker_input = st.sidebar.text_input("Mã cổ phiếu (VD: ALL.AX, CBA.AX):", value="ALL.AX").upper()
g_rate = st.sidebar.slider("Tốc độ tăng trưởng cổ tức (g %):", 1.0, 6.0, 3.0, 0.5) / 100

if ticker_input:
    try:
        stock = yf.Ticker(ticker_input)
        info = stock.info
        
        company_name = info.get('longName', ticker_input)
        price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        
        st.header(f"{company_name} ({ticker_input})")
        st.subheader(f"Giá hiện tại: ${price} AUD")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### 📌 Chỉ số Tài chính")
            st.metric("P/E Ratio", round(info.get('trailingPE', 0), 2) if info.get('trailingPE') else "N/A")
            st.metric("P/B Ratio", round(info.get('priceToBook', 0), 2) if info.get('priceToBook') else "N/A")
            roe = info.get('returnOnEquity')
            st.metric("ROE (%)", f"{round(roe * 100, 2)}%" if roe else "N/A")
            
        with col2:
            st.write("### 📈 Định giá DDM")
            d0 = info.get('dividendRate', 0)
            beta = info.get('beta', 1.0)
            if beta is None: beta = 1.0
            
            re = 0.04 + (beta * 0.06) # CAPM
            st.write(f"* **Cost of Equity ($r_e$):** {round(re*100, 2)}%")
            st.write(f"* **Cổ tức D0:** ${d0} AUD")
            
            if d0 and d0 > 0:
                if re > g_rate:
                    intrinsic_val = (d0 * (1 + g_rate)) / (re - g_rate)
                    margin = ((intrinsic_val - price) / price) * 100
                    st.metric("Giá trị Nội tại (Intrinsic Value)", f"${round(intrinsic_val, 2)} AUD", delta=f"{round(margin, 2)}%")
                else:
                    st.warning("Cost of Equity nhỏ hơn g.")
            else:
                st.info("Công ty không trả cổ tức định kỳ.")
                
        # Biểu đồ
        st.markdown("---")
        st.write("### 📉 Lịch sử Giá 1 Năm")
        df_hist = stock.history(period="1y").reset_index()
        if not df_hist.empty:
            fig = px.line(df_hist, x="Date", y="Close", title=f"Biểu đồ giá {ticker_input}")
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error(f"Lỗi: {e}")