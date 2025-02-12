import streamlit as st
import pathlib

# Function to load CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set up page
st.set_page_config(page_title="Stock Portfolio", page_icon="📈", layout="wide")

st.title("Portfolio")

# Load external CSS
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)

# Portfolio Data (Added Dividend Yield and Dividend Income)
portfolio = [
    {"ticker": "V", "name": "Visa", "price": 351.23, "change": 3.21, "change_pct": 0.92, "units": 2.67191, "avg_open": 285.25, "pl": 176.23, "pl_pct": 23.12, "div_yield": 0.80, "div_income": 8.54},
    {"ticker": "UPS", "name": "United Parcel Service Inc", "price": 114.16, "change": 1.05, "change_pct": 0.93, "units": 7.97302, "avg_open": 127.23, "pl": -104.26, "pl_pct": -10.28, "div_yield": 3.20, "div_income": 25.51},
    {"ticker": "O", "name": "Realty Income Corp", "price": 53.96, "change": -0.16, "change_pct": -0.30, "units": 14.09761, "avg_open": 53.20, "pl": 10.71, "pl_pct": 1.43, "div_yield": 4.60, "div_income": 34.24},
    {"ticker": "ASML", "name": "ASML Holding NV - ADR", "price": 744.08, "change": 16.38, "change_pct": 2.25, "units": 0.7898, "avg_open": 696.37, "pl": 37.65, "pl_pct": 6.85, "div_yield": 0.75, "div_income": 5.92},
    {"ticker": "NKE", "name": "NIKE", "price": 70.94, "change": 2.26, "change_pct": 3.29, "units": 7.10552, "avg_open": 80.92, "pl": -71.01, "pl_pct": -12.35, "div_yield": 1.50, "div_income": 10.66},
    {"ticker": "MC.PA", "name": "LVMH Moet Hennessy", "price": 678.38, "change": -6.42, "change_pct": -0.94, "units": 0.71, "avg_open": 633.41, "pl": 6.16, "pl_pct": 1.26, "div_yield": 1.30, "div_income": 8.74},
    {"ticker": "MAIN", "name": "Main Street Capital Corp", "price": 60.57, "change": -0.44, "change_pct": -0.72, "units": 8.16084, "avg_open": 49.25, "pl": 92.55, "pl_pct": 23.02, "div_yield": 5.80, "div_income": 47.33},
]

# Header Row
st.markdown('<div class="stock-table">', unsafe_allow_html=True)
columns = st.columns([1.5, 1, 1, 1, 1, 1, 1, 1, 1])  # Adjusted for 8 columns
columns[0].markdown('<div class="stock-title">Asset</div>', unsafe_allow_html=True)
columns[1].markdown('<div class="stock-title">Units</div>', unsafe_allow_html=True)
columns[2].markdown('<div class="stock-title">Price</div>', unsafe_allow_html=True)
columns[3].markdown('<div class="stock-title">Avg. Open</div>', unsafe_allow_html=True)
columns[4].markdown('<div class="stock-title">Dividend Yield</div>', unsafe_allow_html=True)
columns[5].markdown('<div class="stock-title">Dividend Income</div>', unsafe_allow_html=True)
columns[6].markdown('<div class="stock-title">P/L</div>', unsafe_allow_html=True)
columns[7].markdown('<div class="stock-title">P/L (%)</div>', unsafe_allow_html=True)

# Display Stock Data
for stock in portfolio:
    row = st.columns([1.5, 1, 1, 1, 1, 1, 1, 1, 1])
    
    # Stock Name and Ticker
    row[0].markdown(f"**{stock['ticker']}**  \n<small>{stock['name']}</small>", unsafe_allow_html=True)

    # Units
    row[1].markdown(f"<div class='stock-data'>{stock['units']:.5f}</div>", unsafe_allow_html=True)
    
    # Price and Change
    row[2].markdown(f"<div class='stock-data'>{stock['price']}</div>", unsafe_allow_html=True)

    # Average Open Price
    row[3].markdown(f"<div class='stock-data'>{stock['avg_open']:.2f}</div>", unsafe_allow_html=True)

    # Dividend Yield
    row[4].markdown(f"<div class='stock-data'>{stock['div_yield']:.2f}%</div>", unsafe_allow_html=True)

    # Dividend Income
    row[5].markdown(f"<div class='stock-data'>${stock['div_income']:.2f}</div>", unsafe_allow_html=True)

    # Profit/Loss
    pl_class = "gain" if stock["pl"] > 0 else "loss"
    row[6].markdown(f"<div class='stock-data'><span class='{pl_class}'>${stock['pl']:.2f}</span></div>", unsafe_allow_html=True)

    # Profit/Loss Percentage
    row[7].markdown(f"<div class='stock-data'><span class='{pl_class}'>{stock['pl_pct']:.2f}%</span></div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
