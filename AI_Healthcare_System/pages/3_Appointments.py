import streamlit as st
import pandas as pd
import os
from datetime import datetime


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("📅 Appointment Booking")

patient_name = st.text_input("Patient Name")

doctor_name = st.text_input("Doctor Name")

appointment_date = st.date_input("Appointment Date")

if st.button("Book Appointment"):

    appointment_file = "data/appointments.csv"

    if os.path.exists(appointment_file):
        appointments = pd.read_csv(appointment_file)
    else:
        appointments = pd.DataFrame()

    new_appointment = pd.DataFrame({
        "Patient":[patient_name],
        "Doctor":[doctor_name],
        "Date":[appointment_date]
    })

    appointments = pd.concat(
        [appointments,new_appointment],
        ignore_index=True
    )

    appointments.to_csv(
        appointment_file,
        index=False
    )

    # Notification
    notification_file = "data/notifications.csv"

    if os.path.exists(notification_file):
        notifications = pd.read_csv(notification_file)
    else:
        notifications = pd.DataFrame(
            columns=["Message","Time"]
        )

    message = f"Appointment booked by {patient_name} with Dr. {doctor_name}"

    new_notification = pd.DataFrame({
        "Message":[message],
        "Time":[datetime.now()]
    })

    notifications = pd.concat(
        [notifications,new_notification],
        ignore_index=True
    )

    notifications.to_csv(
        notification_file,
        index=False
    )

    st.success("Appointment Booked Successfully")