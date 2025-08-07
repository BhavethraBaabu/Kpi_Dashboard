import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from kpi_utils import calculate_kpis, generate_summary

st.title("Automated KPI Dashboard Generator")

uploaded_file = st.file_uploader("Upload your sales CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Raw data:", df.head())

    kpis = calculate_kpis(df)

    st.subheader("KPI Visualizations")
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # Revenue plot
    ax[0, 0].plot(kpis['Date'], kpis['Revenue'])
    ax[0, 0].set_title('Monthly Revenue')

    # Churn plot
    ax[0, 1].plot(kpis['Date'], kpis['Churn Rate'])
    ax[0, 1].set_title('Monthly Churn Rate')

    # MRR plot
    ax[1, 0].plot(kpis['Date'], kpis['MRR'])
    ax[1, 0].set_title('Monthly Recurring Revenue (MRR)')

    # Growth plot
    ax[1, 1].plot(kpis['Date'], kpis['Growth'])
    ax[1, 1].set_title('Monthly Growth %')

    st.pyplot(fig)

    st.subheader("KPI Summary")
    summary = generate_summary(kpis)
    st.write(summary)