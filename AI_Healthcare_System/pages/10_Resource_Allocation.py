import streamlit as st
import pandas as pd
import plotly.express as px


def load_theme():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_theme()

st.title(
    "📦 Resource Allocation"
)

df = pd.read_csv(
    "data/hospital_resources.csv"
)

st.dataframe(
    df,
    use_container_width=True
)

fig = px.bar(
    df,
    x="Resource",
    y="Available",
    title="Hospital Resources"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

resource = st.selectbox(
    "Resource",
    df["Resource"]
)

if st.button(
    "Forecast Demand"
):

    st.info(
        f"Expected demand for {resource}: +15%"
    )