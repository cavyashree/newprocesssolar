import streamlit as st
import pandas as pd

st.title("Solar Power Generation")

st.write("This app displays the solar power generation dataset and allows uploading your own CSV.")

# Load your dataset from repository
df = pd.read_csv("solarpowergeneration.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Upload option
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded:
    st.subheader("Uploaded File Preview")
    new_df = pd.read_csv(uploaded)
    st.dataframe(new_df.head())
