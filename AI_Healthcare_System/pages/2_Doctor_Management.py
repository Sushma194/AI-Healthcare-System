import streamlit as st
import pandas as pd


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("👨‍⚕️ Doctor Management")

df = pd.read_csv("data/doctors.csv")

doctor_id = st.text_input("Doctor ID")
name = st.text_input("Doctor Name")
specialization = st.text_input("Specialization")
experience = st.number_input(
    "Experience (Years)",
    0,
    50
)

if st.button("Add Doctor"):

    new_row = pd.DataFrame({
        "Doctor ID":[doctor_id],
        "Name":[name],
        "Specialization":[specialization],
        "Experience":[experience]
    })

    df = pd.concat([df,new_row])

    df.to_csv(
        "data/doctors.csv",
        index=False
    )

    st.success("Doctor Added")

st.markdown("---")

st.dataframe(df,use_container_width=True)