import streamlit as st
import pandas as pd
import os


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("📋 Electronic Health Records (EHR)")

file_path = "data/medical_records.csv"

# Create file if missing
if not os.path.exists(file_path):

    sample = pd.DataFrame({
        "Patient ID": [1],
        "Patient Name": ["Ravi"],
        "Diagnosis": ["Diabetes"],
        "Treatment": ["Medication"],
        "Doctor": ["Dr. Kumar"]
    })

    os.makedirs("data", exist_ok=True)
    sample.to_csv(file_path, index=False)

# Load records
df = pd.read_csv(file_path)

st.subheader("Existing Medical Records")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

st.subheader("Add New Medical Record")

patient_id = st.number_input(
    "Patient ID",
    min_value=1
)

patient_name = st.text_input(
    "Patient Name"
)

diagnosis = st.text_input(
    "Diagnosis"
)

treatment = st.text_input(
    "Treatment"
)

doctor = st.text_input(
    "Doctor Name"
)

if st.button("Save Record"):

    new_record = pd.DataFrame({
        "Patient ID": [patient_id],
        "Patient Name": [patient_name],
        "Diagnosis": [diagnosis],
        "Treatment": [treatment],
        "Doctor": [doctor]
    })

    df = pd.concat(
        [df, new_record],
        ignore_index=True
    )

    df.to_csv(
        file_path,
        index=False
    )

    st.success(
        "Medical Record Saved Successfully"
    )

    st.rerun()