import streamlit as st
import pandas as pd
import plotly.express as px
import os


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("📊 Hospital Analytics Dashboard")

patients_file = "data/patients.csv"

if os.path.exists(patients_file):
    patients = pd.read_csv(patients_file)
else:
    patients = pd.DataFrame()

st.subheader("Hospital KPIs")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Patients", len(patients))
col2.metric("Doctors", 85)
col3.metric("Appointments", 340)
col4.metric("Beds", 120)

st.markdown("---")

gender_data = pd.DataFrame({
    "Gender":["Male","Female"],
    "Count":[120,95]
})

fig = px.pie(
    gender_data,
    names="Gender",
    values="Count",
    title="Patient Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)