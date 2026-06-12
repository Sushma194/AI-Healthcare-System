import streamlit as st
import pandas as pd
import plotly.express as px


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("📈 Patient Outcome Prediction")

st.subheader("Enter Patient Information")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=40
)

severity = st.slider(
    "Disease Severity",
    1,
    10,
    5
)

oxygen = st.slider(
    "Oxygen Level (%)",
    50,
    100,
    95
)

heart_rate = st.slider(
    "Heart Rate",
    40,
    180,
    80
)

icu = st.selectbox(
    "ICU Required",
    ["No", "Yes"]
)

if st.button("Predict Outcome"):

    score = 0

    if age > 60:
        score += 2

    if severity > 7:
        score += 3

    if oxygen < 90:
        score += 3

    if heart_rate > 120:
        score += 2

    if icu == "Yes":
        score += 3

    recovery = max(0, 100 - (score * 10))

    st.subheader("Prediction Results")

    st.metric(
        "Recovery Probability",
        f"{recovery}%"
    )

    if recovery >= 80:
        st.success("Excellent Recovery Expected")

    elif recovery >= 50:
        st.warning("Moderate Recovery Expected")

    else:
        st.error("High Risk Patient")

    report = pd.DataFrame({
        "Metric": [
            "Age",
            "Severity",
            "Oxygen Level",
            "Heart Rate",
            "ICU",
            "Recovery Probability"
        ],
        "Value": [
            age,
            severity,
            oxygen,
            heart_rate,
            icu,
            f"{recovery}%"
        ]
    })

    st.dataframe(
        report,
        use_container_width=True
    )

    chart_data = pd.DataFrame({
        "Category": [
            "Recovery",
            "Risk"
        ],
        "Value": [
            recovery,
            100 - recovery
        ]
    })

    fig = px.pie(
        chart_data,
        names="Category",
        values="Value",
        title="Outcome Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )