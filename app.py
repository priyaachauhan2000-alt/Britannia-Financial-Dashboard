import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Britannia Financial Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

FILE = "Britannia_Financial_Intelligence_Phase2.xlsx"

monthly = pd.read_excel(FILE, sheet_name="Monthly_Report")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("📊 Britannia Financial Intelligence Dashboard")
st.markdown("Executive Financial Performance Dashboard")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

latest = monthly.iloc[-1]

revenue = latest["Total_Revenue"]
expense = latest["Total_Operating_Expenses"]
profit = latest["Net_Profit"]
burn_rate = latest["Burn_Rate"]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Revenue",
    f"₹{revenue:,.2f} Cr"
)

c2.metric(
    "Expenses",
    f"₹{expense:,.2f} Cr"
)

c3.metric(
    "Net Profit",
    f"₹{profit:,.2f} Cr"
)

c4.metric(
    "Burn Rate",
    f"₹{burn_rate:,.2f} Cr"
)

st.divider()

# ---------------------------------------------------
# REVENUE TREND
# ---------------------------------------------------

st.subheader("📈 Revenue Trend")

fig_rev = px.line(
    monthly,
    x="Month",
    y="Total_Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(
    fig_rev,
    use_container_width=True
)

# ---------------------------------------------------
# PROFIT TREND
# ---------------------------------------------------

st.subheader("💹 Net Profit Trend")

fig_profit = px.bar(
    monthly,
    x="Month",
    y="Net_Profit",
    title="Monthly Net Profit"
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# ---------------------------------------------------
# REVENUE MIX
# ---------------------------------------------------

st.subheader("💰 Revenue Mix")

rev_mix = pd.DataFrame({
    "Channel": [
        "O2C",
        "Retail",
        "Digital"
    ],
    "Revenue": [
        latest["O2C_Revenue"],
        latest["Retail_Revenue"],
        latest["Digital_Revenue"]
    ]
})

fig_mix = px.pie(
    rev_mix,
    names="Channel",
    values="Revenue",
    hole=0.4
)

st.plotly_chart(
    fig_mix,
    use_container_width=True
)

# ---------------------------------------------------
# EXPENSE BREAKDOWN
# ---------------------------------------------------

st.subheader("🏢 Expense Breakdown")

expense_df = pd.DataFrame({
    "Category": [
        "Employee",
        "Marketing",
        "R&D",
        "CAPEX"
    ],
    "Amount": [
        latest["Employee_Cost"],
        latest["Marketing_Cost"],
        latest["R&D_Cost"],
        latest["CAPEX"]
    ]
})

fig_expense = px.bar(
    expense_df,
    x="Category",
    y="Amount",
    title="Expense Breakdown"
)

st.plotly_chart(
    fig_expense,
    use_container_width=True
)

# ---------------------------------------------------
# REVENUE VS EXPENSE
# ---------------------------------------------------

st.subheader("⚖ Revenue vs Expense")

comparison = go.Figure()

comparison.add_trace(
    go.Scatter(
        x=monthly["Month"],
        y=monthly["Total_Revenue"],
        mode="lines+markers",
        name="Revenue"
    )
)

comparison.add_trace(
    go.Scatter(
        x=monthly["Month"],
        y=monthly["Total_Operating_Expenses"],
        mode="lines+markers",
        name="Expenses"
    )
)

st.plotly_chart(
    comparison,
    use_container_width=True
)

# ---------------------------------------------------
# CASH BURN DAYS
# ---------------------------------------------------

st.subheader("🔥 Cash Burn Days")

fig_burn = px.line(
    monthly,
    x="Month",
    y="Cash_Burn_Days",
    markers=True
)

st.plotly_chart(
    fig_burn,
    use_container_width=True
)

# ---------------------------------------------------
# DATA TABLE
# ---------------------------------------------------

st.subheader("📋 Monthly Financial Report")

st.dataframe(
    monthly,
    use_container_width=True
)
