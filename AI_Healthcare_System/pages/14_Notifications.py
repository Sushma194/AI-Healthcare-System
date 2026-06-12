import streamlit as st
import pandas as pd
import os


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_theme()


st.set_page_config(
    page_title="Notifications",
    page_icon="🔔",
    layout="wide"
)

st.title("🔔 Notifications Center")

notification_file = "data/notifications.csv"


# Create file if not exists
if not os.path.exists(notification_file):

    notifications = pd.DataFrame(
        columns=[
            "Message",
            "Time"
        ]
    )

    notifications.to_csv(
        notification_file,
        index=False
    )


# Read Notifications
notifications = pd.read_csv(
    notification_file
)


# Notification Count
st.metric(
    "Total Notifications",
    len(notifications)
)

st.divider()


# Display Notifications
if len(notifications) > 0:

    notifications = notifications.iloc[::-1]

    for index, row in notifications.iterrows():

        with st.container():

            st.info(
                f"""
🔔 {row['Message']}

🕒 {row['Time']}
"""
            )

else:

    st.warning(
        "No Notifications Available"
    )


st.divider()


# Clear Notifications
if st.button(
    "🗑 Clear All Notifications"
):

    empty_df = pd.DataFrame(
        columns=[
            "Message",
            "Time"
        ]
    )

    empty_df.to_csv(
        notification_file,
        index=False
    )

    st.success(
        "Notifications Cleared Successfully"
    )

    st.rerun()