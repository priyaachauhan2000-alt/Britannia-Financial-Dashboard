import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

monthly = pd.read_excel(
    "Britannia_Financial_Intelligence_Phase2.xlsx",
    sheet_name="Monthly_Report"
)

monthly = monthly.iloc[:-2]

monthly = monthly.reset_index(drop=True)

latest = monthly.iloc[-1]

st.write("Latest row being used:")
st.write(latest)
