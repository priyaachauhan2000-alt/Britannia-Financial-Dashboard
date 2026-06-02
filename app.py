import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Britannia Phase 2 Inspection")

file_path = "Britannia_Financial_Intelligence_Phase2.xlsx"

xls = pd.ExcelFile(file_path)

st.write(xls.sheet_names)

for sheet in xls.sheet_names:

    st.divider()

    st.header(sheet)

    df = pd.read_excel(file_path, sheet_name=sheet)

    st.write("Columns:")

    st.write(list(df.columns))

    st.dataframe(df.head(10))
