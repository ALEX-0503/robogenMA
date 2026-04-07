from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="RobogenMA Demo", layout="wide")
st.title("RobogenMA: RK-CS-Sim-FO Demo")
st.markdown(
    """
    This MVP demonstrates an end-to-end flow:
    **Task Input -> RK parse -> CS strategy -> Simulation -> FO feedback**
    """
)

with st.expander("Quick start", expanded=True):
    st.write("1) Open `Task Input` page and load an example.")
    st.write("2) Open `Parameter Table` to inspect parsed structured parameters.")
    st.write("3) Open `Simulation` to run.")
    st.write("4) Open `Report` to review charts and export markdown.")

col1, col2 = st.columns(2)
with col1:
    st.info("Use fixed seed examples for stable classroom demos.")
with col2:
    st.success("Deploy-ready for Streamlit Community Cloud.")

