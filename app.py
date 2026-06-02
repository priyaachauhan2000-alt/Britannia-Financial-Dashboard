import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Britannia Dashboard Debug")

FILE = "Britannia_Financial_Intelligence_Phase2.xlsx"

monthly = pd.read_excel(FILE, sheet_name="Monthly_Report")

st.subheader("Data Shape")
st.write(monthly.shape)

st.subheader("Column Names")
st.write(monthly.columns.tolist())

st.subheader("Last 10 Rows")
st.dataframe(monthly.tail(10), use_container_width=True)
