import streamlit as st
import pandas as pd

st.title("Phase 2 File Inspection")

file_path = "Britannia_Financial_Intelligence_Phase2.xlsx"

xls = pd.ExcelFile(file_path)

st.write("Sheets:")
st.write(xls.sheet_names)

for sheet in xls.sheet_names:
    st.subheader(sheet)

    df = pd.read_excel(file_path, sheet_name=sheet)

    st.write(df.head())
