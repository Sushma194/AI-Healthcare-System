import streamlit as st


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title(
    "💊 Treatment Recommendation"
)

disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease"
    ]
)

if st.button(
    "Generate Recommendation"
):

    if disease == "Diabetes":

        st.success("""
Specialist:
Endocrinologist

Tests:
HbA1c
Fasting Blood Sugar

Medication:
Metformin
""")

    elif disease == "Heart Disease":

        st.success("""
Specialist:
Cardiologist

Tests:
ECG
Echocardiogram

Medication:
Aspirin
Statins
""")

    elif disease == "Kidney Disease":

        st.success("""
Specialist:
Nephrologist

Tests:
Creatinine
Urine Analysis

Medication:
As prescribed by doctor
""")