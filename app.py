import streamlit as st
import pandas as pd

FILE = "Britannia_Financial_Intelligence_Phase2.xlsx"

monthly = pd.read_excel(FILE, sheet_name="Monthly_Report")

monthly = monthly[monthly["Month"].notna()]
monthly = monthly[monthly["Month"].astype(str).str.contains("2024|2025")]

st.write(monthly.tail())

st.write("LATEST ROW")
st.write(monthly.iloc[-1])
