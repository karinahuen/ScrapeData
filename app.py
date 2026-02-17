import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GBP Market Dashboard", layout="wide")
st.title("Global Currency Dashboard")

try:
    df = pd.read_csv("gbp_rates.csv")

   
    st.markdown("### Market Snapshot")

    kpi1, kpi2, kpi3 = st.columns(3)
    
    def get_rate(pair):
        row = df[df['Currency Pair'] == pair]
        if not row.empty:
            return row['Rate'].values[0]
        return 0

    kpi1.metric("USD", f"{get_rate('GBP/USD'):.4f}")
    kpi2.metric("EUR", f"{get_rate('GBP/EUR'):.4f}")
    kpi3.metric("HKD", f"{get_rate('GBP/HKD'):.4f}") 

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Exchange Rate Table")
        # Display the table with 4 decimal places
        st.dataframe(
            df.style.format({"Rate": "{:.4f}"}),
            use_container_width=True,
            hide_index=True
        )

    with col2:
        st.subheader("Compare Values")
        # Bar Chart
        fig = px.bar(
            df, 
            x='Currency Pair', 
            y='Rate', 
            color='Rate',
            text_auto='.4f', 
            title="How much is £1 worth?"
        )
        st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Data file is missing. Please run 'scraper.py' first.")