from __future__ import annotations

import streamlit as st

from robogenma.utils.ui import inject_base_style, render_app_shell, render_stage_progress

st.set_page_config(page_title="RobogenMA Demo", layout="wide")
inject_base_style()
render_app_shell("requirement")
render_stage_progress("requirement")

st.markdown("### Quick Start")
st.markdown(
    """
    <div class="decor-grid">
      <div class="decor-item">Pattern A · Agent orchestration wave</div>
      <div class="decor-item">Pattern B · Disturbance-aware planning</div>
      <div class="decor-item">Pattern C · Closed-loop optimization</div>
    </div>
    <div class="status-strip">
      <div class="status-item"><b>Theme</b><span>Lab-grade UI · English</span></div>
      <div class="status-item"><b>Workflow</b><span>RK / CS / SD / FO</span></div>
      <div class="status-item"><b>Reproducibility</b><span>Seed-based simulation</span></div>
      <div class="status-item"><b>Output</b><span>Metrics + Markdown report</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
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

with st.expander("Classroom Script (Stable Mainline + 30s Bonus)", expanded=False):
    st.markdown(
        """
        - **0:00-0:20** Introduce RK -> CS -> Simulation -> FO pipeline.
        - **0:20-0:50** Requirement Input: choose `simple_task`, click `Parse Requirement`.
        - **0:50-1:25** Parameter Display: show metrics + JSON.
        - **1:25-2:10** Strategy & Simulation: run with seed `42`.
        - **2:10-2:45** Result Report: show metrics and export markdown.
        - **2:45-3:15 Bonus** Mention `External Link Boost` as optional data-driven enhancement.
        """
    )

if st.button("Load Classroom Preset (simple_task)", use_container_width=True, type="primary"):
    st.session_state["task_text"] = (
        "Simple task: navigate in a medium grid start(1,1) goal(35,25) with low disturbance."
    )
    st.session_state["robot_type"] = "microrobot"
    st.session_state["drive_mode"] = "magnetic"
    st.switch_page("pages/1_Task_Input.py")

