import streamlit as st
import pandas as pd
from datetime import datetime


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("📄 Healthcare Reports")

report_type = st.selectbox(
    "Select Report",
    [
        "Patient Recovery Report",
        "Disease Statistics Report",
        "Bed Occupancy Report",
        "Resource Usage Report",
        "Doctor Performance Report"
    ]
)

if st.button("Generate Report"):

    current_date = datetime.now().strftime("%Y-%m-%d")

    if report_type == "Patient Recovery Report":

        report = pd.DataFrame({
            "Patient": [
                "Ravi",
                "Suresh",
                "Anjali"
            ],
            "Recovery %": [
                90,
                75,
                85
            ]
        })

    elif report_type == "Disease Statistics Report":

        report = pd.DataFrame({
            "Disease": [
                "Diabetes",
                "Heart Disease",
                "Kidney Disease"
            ],
            "Cases": [
                120,
                80,
                45
            ]
        })

    elif report_type == "Bed Occupancy Report":

        report = pd.DataFrame({
            "Bed Type": [
                "ICU",
                "General",
                "Emergency"
            ],
            "Occupied": [
                25,
                60,
                10
            ]
        })

    elif report_type == "Resource Usage Report":

        report = pd.DataFrame({
            "Resource": [
                "Ventilator",
                "Oxygen Unit",
                "MRI Machine"
            ],
            "Usage %": [
                70,
                85,
                55
            ]
        })

    else:

        report = pd.DataFrame({
            "Doctor": [
                "Dr. Kumar",
                "Dr. Priya",
                "Dr. Raj"
            ],
            "Patients Handled": [
                50,
                45,
                60
            ]
        })

    st.success("Report Generated Successfully")

    st.subheader(report_type)

    st.dataframe(
        report,
        use_container_width=True
    )

    csv = report.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV Report",
        data=csv,
        file_name=f"{report_type}_{current_date}.csv",
        mime="text/csv"
    )