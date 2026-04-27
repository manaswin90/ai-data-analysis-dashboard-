import streamlit as st
import pandas as pd
from src.data_cleaning import load_data, clean_data

st.title("📊 Data Analysis Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    df = clean_data(df)

    st.write("### Dataset Preview")
    st.dataframe(df)

    st.write("### Basic Stats")
    st.write(df.describe())

    column = st.selectbox("Select column", df.columns)

    st.write("### Distribution")
    st.bar_chart(df[column].value_counts())

    st.write("### Correlation Heatmap")
    st.write(df.corr())
