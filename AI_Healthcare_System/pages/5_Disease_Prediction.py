import streamlit as st
import pandas as pd


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("🩺 AI Disease Prediction")

st.subheader("Enter Patient Details")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

fever = st.selectbox(
    "Fever",
    ["No", "Yes"]
)

cough = st.selectbox(
    "Cough",
    ["No", "Yes"]
)

fatigue = st.selectbox(
    "Fatigue",
    ["No", "Yes"]
)

breathing_issue = st.selectbox(
    "Breathing Issue",
    ["No", "Yes"]
)

def predict_disease():

    score = 0

    if fever == "Yes":
        score += 2

    if cough == "Yes":
        score += 2

    if fatigue == "Yes":
        score += 1

    if breathing_issue == "Yes":
        score += 3

    if age > 50:
        score += 1

    if score >= 6:
        return "High Risk Condition"

    elif score >= 3:
        return "Medium Risk Condition"

    else:
        return "Low Risk Condition"

def treatment_recommendation(result):

    if "High" in result:

        return """
🚨 Immediate Medical Attention

🚨 Oxygen Monitoring

🚨 Hospital Evaluation
"""

    elif "Medium" in result:

        return """
⚠ Doctor Consultation

⚠ Medication

⚠ Monitor Symptoms
"""

    else:

        return """
✅ Healthy Lifestyle

✅ Regular Exercise

✅ Balanced Diet
"""

if st.button("Predict Disease"):

    result = predict_disease()

    recommendation = treatment_recommendation(
        result
    )

    st.subheader("Prediction Result")

    if "High" in result:
        st.error(result)

    elif "Medium" in result:
        st.warning(result)

    else:
        st.success(result)

    st.subheader(
        "Treatment Recommendation"
    )

    st.info(recommendation)

    report = pd.DataFrame({
        "Parameter": [
            "Age",
            "Fever",
            "Cough",
            "Fatigue",
            "Breathing Issue",
            "Prediction"
        ],
        "Value": [
            age,
            fever,
            cough,
            fatigue,
            breathing_issue,
            result
        ]
    })

    st.subheader("Patient Report")

    st.dataframe(
        report,
        use_container_width=True
    )

    csv = report.to_csv(
        index=False
    )

    st.download_button(
        "Download Report",
        csv,
        file_name="disease_prediction_report.csv",
        mime="text/csv"
    )