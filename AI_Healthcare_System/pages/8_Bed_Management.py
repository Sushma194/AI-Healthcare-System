import streamlit as st
import pandas as pd
import os


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("🛏 Bed Management System")

file_path = "data/beds.csv"

# Safe loading (prevents crash)
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=["Bed ID", "Type", "Status"])

# Metrics
if not df.empty:

    occupied = len(df[df["Status"] == "Occupied"])
    available = len(df[df["Status"] == "Available"])

    col1, col2 = st.columns(2)

    col1.metric("Occupied Beds", occupied)
    col2.metric("Available Beds", available)

    st.dataframe(df, use_container_width=True)

else:
    st.warning("No bed data found. Please check beds.csv file.")