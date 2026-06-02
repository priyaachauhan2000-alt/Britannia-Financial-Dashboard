monthly = pd.read_excel(
    "Britannia_Financial_Intelligence_Phase2.xlsx",
    sheet_name="Monthly_Report"
)

# Remove the last two bad rows
monthly = monthly.iloc[:-2]

# Reset index
monthly = monthly.reset_index(drop=True)

latest = monthly.iloc[-1]

st.write("Latest row being used:")
st.write(latest)
