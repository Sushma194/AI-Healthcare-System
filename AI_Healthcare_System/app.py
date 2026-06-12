import streamlit as st
import pandas as pd
import plotly.express as px


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_theme()

st.set_page_config(
    page_title="AI Healthcare System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI-Powered Healthcare Prediction & Resource Management System")
st.caption("A smart hospital command center with analytics, predictions, records, and alerts in one place.")

st.markdown("""
### Welcome to Healthcare Intelligence Platform

AI-powered system for:
- Disease Prediction
- Treatment Recommendation
- Outcome Prediction
- Bed Management
- Staff Scheduling
- Resource Allocation
- Medical Report Analysis
- AI Chatbot
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Patients", "1,250", "+8%")
with col2:
    st.metric("Doctors", "85", "+3")
with col3:
    st.metric("Beds", "320", "98% occupied")
with col4:
    st.metric("Appointments", "540", "+12 today")

st.divider()

st.subheader("📊 Hospital Analytics")

monthly_activity = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Appointments": [120, 180, 250, 300, 380, 420],
        "Admissions": [90, 110, 130, 160, 190, 220],
    }
)

line_chart = px.line(
    monthly_activity,
    x="Month",
    y=["Appointments", "Admissions"],
    title="Monthly Appointments vs Admissions",
    markers=True,
)
line_chart.update_layout(template="plotly_white", height=340)
st.plotly_chart(line_chart, use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    ward_df = pd.DataFrame(
        {"Ward": ["ICU", "General", "Pediatrics", "Emergency"], "Occupancy": [78, 65, 54, 82]}
    )
    ward_chart = px.bar(ward_df, x="Ward", y="Occupancy", color="Ward", title="Ward Occupancy %")
    ward_chart.update_layout(template="plotly_white", height=320)
    st.plotly_chart(ward_chart, use_container_width=True)
with col_b:
    service_df = pd.DataFrame({"Service": ["Diagnostics", "Surgery", "Emergency", "Outpatient"], "Count": [40, 28, 19, 35]})
    pie_chart = px.pie(service_df, names="Service", values="Count", hole=0.35, title="Service Utilization")
    pie_chart.update_layout(template="plotly_white", height=320)
    st.plotly_chart(pie_chart, use_container_width=True)

st.divider()
st.success("✅ AI Healthcare System Running Successfully")