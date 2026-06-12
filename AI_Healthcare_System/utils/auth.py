import streamlit as st

# Demo Users
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "doctor": {
        "password": "doctor123",
        "role": "Doctor"
    },
    "patient": {
        "password": "patient123",
        "role": "Patient"
    }
}

def login():

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username in USERS:

            if USERS[username]["password"] == password:

                st.session_state.logged_in = True

                st.session_state.username = username

                st.session_state.role = USERS[username]["role"]

                st.success("Login Successful")

                st.rerun()

            else:
                st.error("Wrong Password")

        else:
            st.error("User Not Found")


def logout():

    if st.sidebar.button("Logout"):

        st.session_state.clear()

        st.rerun()


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )