import streamlit as st
import pandas as pd


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("🧑 Patient Management")

df = pd.read_csv("data/patients.csv")

st.subheader("Add New Patient")

patient_id = st.text_input("Patient ID")
name = st.text_input("Name")
age = st.number_input("Age",1,120)
gender = st.selectbox(
    "Gender",
    ["Male","Female","Other"]
)

blood = st.selectbox(
    "Blood Group",
    [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ]
)

condition = st.text_input("Medical Condition")

if st.button("Add Patient"):

    new_row = pd.DataFrame({
        "Patient ID":[patient_id],
        "Name":[name],
        "Age":[age],
        "Gender":[gender],
        "Blood Group":[blood],
        "Condition":[condition]
    })

    df = pd.concat([df,new_row])

    df.to_csv(
        "data/patients.csv",
        index=False
    )

    st.success("Patient Added Successfully")

st.markdown("---")

st.subheader("Patient Records")

st.dataframe(df,use_container_width=True)