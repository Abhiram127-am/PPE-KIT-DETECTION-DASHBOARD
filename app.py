import streamlit as st

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 PPE Analytics Dashboard")

st.markdown("### Power BI Live Dashboard")

POWERBI_URL = "https://app.powerbi.com/view?r=eyJrIjoiNTViNWZjMTEtZmUxNi00ZTdjLTkxYTUtYmVlOTRkMTg2MmJkIiwidCI6ImY4OTAxNGMxLTJiODYtNGU1My1iZjk1LTgxYTk4ZDhhNjI2NyJ9"

st.components.v1.iframe(
    src=POWERBI_URL,
    width=1400,
    height=800,
    scrolling=True
)