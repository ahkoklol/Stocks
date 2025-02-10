import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title = "Name to be chosen",
    page_icon = "📈",
)

st.title("Stock Screener")

SPX500 = [
  "AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "META", "TSLA", "AVGO", "BRK.B",
    "WMT", "LLY", "JPM", "V", "MA", "ORCL", "UNH", "XOM", "COST", "NFLX",
    "HD", "PG", "JNJ", "BAC", "ABBV", "CRM", "TMUS", "KO", "CVX", "WFC",
    "PLTR", "CSCO", "ACN", "IBM", "MS", "PM", "ABT", "AXP", "GS", "MRK",
    "GE", "TMO", "LIN", "MCD", "BX", "ISRG", "NOW", "DIS", "PEP", "ADBE",
    "QCOM", "T", "CAT", "AMD", "RTX", "VZ", "TXN", "INTU", "BKNG", "SPGI",
    "AMGN", "UBER", "LOW", "NEE", "MDLZ", "DHR", "SCHW", "UPS", "HON", "NKE",
    "DE", "BLK", "MO", "AMT", "SBUX", "CVS", "ELV", "SO", "INTC", "LMT",
    "BA", "C", "MMM", "PFE", "ADP", "SYK", "COP", "TGT", "DUK", "CI",
    "BDX", "PLD", "MMC", "CB", "APD", "ZTS", "GSBD", "CL", "ICE", "ITW",
    "MCO", "HUM", "NSC", "PNC", "USB", "WM", "SHW", "EW", "FIS", "FISV",
    "GILD", "ADI", "REGN", "VRTX", "ECL", "AON", "BK", "PSA", "D", "AEP",
    "ETN", "NOC", "HLT", "ADSK", "CSX", "TFC", "FDX", "ROK",
    "TROW", "KMB", "SPG", "TRV", "AIG", "ALL", "A", "APH", "ADM", "AEE",
    "AES", "AFL", "AKAM", "ALK", "ALB", "ARE", "ALGN",
    "ALLE", "LNT", "AWK", "AMP", "ABC", "AME", "ANSS",
    "APA", "AMAT", "APTV", "ANET", "AJG", "AIZ",
    "ATO", "AZO", "AVB", "AVY", "BKR", "BLL", "BBWI", "BAX",
    "BBY", "BIO", "TECH", "BIIB", "BXP", "BSX", "BMY", "BR", "BRO", "BF.B", "CHRW", "COG",
    "CDNS", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CBOE",
    "CBRE", "CDW", "CE", "CNC", "CNP", "CDAY", "CERN", "CF", "CRL",
    "CHTR", "CMG", "CHD", "CINF", "CTAS",
    "CFG", "CTXS", "CLX", "CME", "CMS", "CTSH",
    "CAG", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "CTRA",
    "CCI", "CMI", "DHI", "DRI", "DVA", "DAL",
    "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DISCA", "DISCK", "DISH",
    "DG", "DLTR", "DPZ", "DOV", "DOW", "DTE", "DRE", "DD",
    "DXC", "EMN", "EBAY", "EIX", "EA", "EMR", "ENPH",
    "ETR", "EOG", "EPAM", "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES",
    "RE", "EXC", "EXPE", "EXPD", "EXR", "FFIV", "FAST", "FRT",
    "FITB", "FE", "FRC", "FLT", "FMC", "F", "FTNT",
    "FTV", "FBHS", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GNRC",
    "GD", "GIS", "GM", "GPC", "GL", "GPN", "HAL",
    "HBI", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE",
    "HOLX", "HRL", "HST", "HWM", "HPQ", "HBAN", "HII",
    "IEX", "IDXX", "INFO", "ILMN", "INCY", "IR", "IP", "IPG", "IFF", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY",
    "J", "JBHT", "JCI", "JNPR", "K", "KEY", "KEYS",
    "KIM", "KMI", "KLAC", "KHC", "KR", "LHX", "LH", "LRCX", "LW",
    "LVS", "LEG", "LDOS", "LEN", "LNC", "LYV", "LKQ", "L",
    "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM",
    "MAS", "MTCH", "MKC", "MCK", "MET", "MTD",
    "MGM", "MCHP", "MU", "MAA", "MHK", "TAP", "MPWR", "MNST",
    "MOS", "MSI", "NDAQ", "NTAP", "NWL", "NEM",
    "NWSA", "NWS", "NI", "NTRS", "NCLH", "NOV",
    "NRG", "NUE", "NVR", "NXPI", "ORLY", "OXY", "ODFL", "OMC", "ON",
    "OKE", "OGN", "OTIS", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL",
    "PNR", "PBCT", "PKI", "PRGO", "PSX", "PNW", "PXD",
    "POOL", "PPG", "PPL", "PFG", "PGR", "PRU", "PEG",
    "PTC", "PHM", "QRVO", "PWR", "DGX", "RL", "RJF",
    "O", "REG", "RF", "RSG", "RMD", "RHI", "ROL", "ROP",
    "ROST", "RCL", "SBAC", "SLB", "STX", "SEE", "SRE",
    "SWKS", "SJM", "SNA", "SEDG", "LUV", "SWK",
    "STT", "STE", "SIVB", "SYF", "SNPS",
    "TPR", "TEL", "TDY", "TFX", "TER", "TXT",
    "TJX", "TSCO", "TT", "TDG", "TRMB", "TYL", "TSN",
    "UDR", "ULTA", "UAA", "UA", "UNP", "UAL", "URI",
    "VLO", "VTR", "VRSN", "VRSK", "VFC", "VTRS", "VICI",
    "VNO", "VMC", "WRB", "WAB", "WAT",
    "WELL", "WST", "WDC", "WRK", "WY", "WHR", "WMB",
    "XEL", "XRX", "XYL", "YUM", "ZBRA", "ZBH", "ZION"
]

# Searchable select box (acts as search bar + dropdown)
selected_stock = st.selectbox(
    "🔍 Search for a stock by ticker symbol:",
    options=SPX500,
    index=None,  # No default selection
)

if selected_stock:
    ticker = yf.Ticker(selected_stock)
    dividend_info = ticker.calendar  # Fetch upcoming events

    ex_dividend_date = dividend_info.get("Ex-Dividend Date", "N/A")
    dividend_date = dividend_info.get("Dividend Date", "N/A")

    st.write(f"**Ticker Symbol:** {selected_stock}")
    st.write(f"📆 **Ex-Dividend Date:** {ex_dividend_date}")
    st.write(f"💰 **Next Dividend Payment Date:** {dividend_date}")
    st.write("---")  # Adds a separator for better readability