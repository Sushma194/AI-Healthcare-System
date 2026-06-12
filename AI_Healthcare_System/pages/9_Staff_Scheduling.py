import streamlit as st
import pandas as pd
import plotly.express as px
import os


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("👨‍⚕️ Staff Scheduling")

file_path = "data/staff.csv"

if not os.path.exists(file_path):

    df = pd.DataFrame({
        "Staff ID": ["S1", "S2", "S3"],
        "Name": ["John", "David", "Emma"],
        "Role": ["Doctor", "Nurse", "Doctor"],
        "Shift": ["Morning", "Night", "Evening"]
    })

    os.makedirs("data", exist_ok=True)
    df.to_csv(file_path, index=False)

else:
    df = pd.read_csv(file_path)

st.subheader("Current Staff Schedule")

st.dataframe(
    df,
    use_container_width=True
)

fig = px.histogram(
    df,
    x="Shift",
    color="Role",
    title="Shift Allocation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

patient_load = st.slider(
    "Expected Patient Load",
    0,
    500,
    100
)

if patient_load > 300:
    st.warning("Additional Staff Required")
else:
    st.success("Current Staff Sufficient")