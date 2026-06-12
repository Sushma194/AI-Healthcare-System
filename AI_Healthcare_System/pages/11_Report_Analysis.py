import streamlit as st
import pandas as pd
import numpy as np


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title("🩺 AI Medical Report Analysis")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Report")
    st.dataframe(df)

    st.subheader("AI Analysis")

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_cols) == 0:

        st.warning(
            "No numeric values found for analysis"
        )

    else:

        for col in numeric_cols:

            avg = df[col].mean()
            max_val = df[col].max()
            min_val = df[col].min()

            st.write(f"### {col}")

            st.write(
                f"Average Value: {avg:.2f}"
            )

            st.write(
                f"Maximum Value: {max_val}"
            )

            st.write(
                f"Minimum Value: {min_val}"
            )

            if max_val > avg * 1.5:

                st.error(
                    f"⚠ Abnormally High {col} Detected"
                )

            elif min_val < avg * 0.5:

                st.warning(
                    f"⚠ Abnormally Low {col} Detected"
                )

            else:

                st.success(
                    f"✅ {col} Within Expected Range"
                )

    st.success(
        "Medical Report Analysis Completed"
    )