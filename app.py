import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Britannia Financial Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# LOAD DATA
# ---------------------------------

FILE = "Britannia_Financial_Intelligence_Phase2.xlsx"

monthly = pd.read_excel(
    FILE,
    sheet_name="Monthly_Report"
)

# Remove footer rows
monthly = monthly.iloc[:-2]
monthly = monthly.reset_index(drop=True)

latest = monthly.iloc[-1]

# ---------------------------------
# HEADER
# ---------------------------------

st.title("📊 Britannia Financial Intelligence Dashboard")
st.markdown("Executive Financial Performance Dashboard")

# ---------------------------------
# KPI CARDS
# ---------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Revenue",
    f"₹{latest['Total_Revenue']:,.2f}"
)

c2.metric(
    "Expenses",
    f"₹{latest['Total_Operating_Expenses']:,.2f}"
)

c3.metric(
    "Profit",
    f"₹{latest['Net_Profit']:,.2f}"
)

c4.metric(
    "Burn Rate",
    f"{latest['Burn_Rate']:,.2f}"
)

st.divider()

# ---------------------------------
# REVENUE TREND
# ---------------------------------

st.subheader("📈 Revenue Trend")

fig1 = px.line(
    monthly,
    x="Month",
    y="Total_Revenue",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------
# PROFIT TREND
# ---------------------------------

st.subheader("💹 Net Profit Trend")

fig2 = px.bar(
    monthly,
    x="Month",
    y="Net_Profit"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------
# REVENUE MIX
# ---------------------------------

st.subheader("💰 Revenue Mix")

revenue_mix = pd.DataFrame({
    "Channel": ["O2C", "Retail", "Digital"],
    "Revenue": [
        latest["O2C_Revenue"],
        latest["Retail_Revenue"],
        latest["Digital_Revenue"]
    ]
})

fig3 = px.pie(
    revenue_mix,
    names="Channel",
    values="Revenue",
    hole=0.45
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------
# EXPENSE BREAKDOWN
# ---------------------------------

st.subheader("🏢 Expense Breakdown")

expense_mix = pd.DataFrame({
    "Category": ["Employee", "Marketing", "R&D", "CAPEX"],
    "Amount": [
        latest["Employee_Cost"],
        latest["Marketing_Cost"],
        latest["R&D_Cost"],
        latest["CAPEX"]
    ]
})

fig4 = px.bar(
    expense_mix,
    x="Category",
    y="Amount"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------
# REVENUE VS EXPENSE
# ---------------------------------

st.subheader("⚖ Revenue vs Expense")

fig5 = go.Figure()

fig5.add_trace(
    go.Scatter(
        x=monthly["Month"],
        y=monthly["Total_Revenue"],
        mode="lines+markers",
        name="Revenue"
    )
)

fig5.add_trace(
    go.Scatter(
        x=monthly["Month"],
        y=monthly["Total_Operating_Expenses"],
        mode="lines+markers",
        name="Expenses"
    )
)

st.plotly_chart(fig5, use_container_width=True)

# ---------------------------------
# CASH BURN DAYS
# ---------------------------------

st.subheader("🔥 Cash Burn Days")

fig6 = px.line(
    monthly,
    x="Month",
    y="Cash_Burn_Days",
    markers=True
)

st.plotly_chart(fig6, use_container_width=True)

# ---------------------------------
# MONTHLY REPORT
# ---------------------------------

st.subheader("📋 Monthly Financial Report")

st.dataframe(
    monthly,
    use_container_width=True
)
