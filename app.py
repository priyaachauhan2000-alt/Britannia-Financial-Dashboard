import streamlit as st
import pandas as pd

st.title("FINAL DEBUG")

FILE = "Britannia_Financial_Intelligence_Phase2.xlsx"

monthly = pd.read_excel(FILE, sheet_name="Monthly_Report")

st.write(monthly.columns.tolist())

st.write("LAST ROW")
st.write(monthly.iloc[-1])

st.write("SECOND LAST ROW")
st.write(monthly.iloc[-2])

st.write(monthly.tail())
