from __future__ import annotations

import streamlit as st

from robogenma.utils.ui import inject_base_style, render_app_shell

st.set_page_config(page_title="RobogenMA Demo", layout="wide")
inject_base_style()
render_app_shell("requirement")

st.markdown("### Quick Start")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
        <div class="panel">
            <h4>Demo Flow</h4>
            <p>1) Open Requirement Input and load a scenario template</p>
            <p>2) Check parsed parameters in Parameter Display</p>
            <p>3) Run Strategy & Simulation with one click</p>
            <p>4) Present metrics and export report in Result Report</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="panel">
            <h4>Stability Tips</h4>
            <p>- Use fixed scenario templates and seed = 42</p>
            <p>- Run simple_task before complex_task in class demo</p>
            <p>- Keep report preview collapsed and export markdown on demand</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Load Classroom Preset (simple_task)", use_container_width=True, type="primary"):
    st.session_state["task_text"] = (
        "Simple task: navigate in a medium grid start(1,1) goal(35,25) with low disturbance."
    )
    st.session_state["robot_type"] = "microrobot"
    st.session_state["drive_mode"] = "magnetic"
    st.success("Preset loaded into session state. Continue on Requirement Input or Simulation page.")

