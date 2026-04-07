from __future__ import annotations

from pathlib import Path

import streamlit as st

from robogenma.utils.io import load_json
from robogenma.utils.ui import inject_base_style, render_app_shell

inject_base_style()
render_app_shell("requirement")
st.markdown(
    """
    <div class="panel">
      <h4>Requirement Input</h4>
      <p class="panel-sub">Provide natural language task requirements or choose a scenario template.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

example_dir = Path("data/examples")
example_files = sorted([p.name for p in example_dir.glob("*.json")])
choice = st.selectbox("Scenario Template", ["(none)"] + example_files)

default_text = "Navigate in a medium grid from start(1,1) to goal(35,25) with mild disturbance."
default_robot = "microrobot"
default_drive = "magnetic"

if choice != "(none)":
    data = load_json(example_dir / choice)
    default_text = data["task_text"]
    default_robot = data.get("robot_type", default_robot)
    default_drive = data.get("drive_mode", default_drive)

left, right = st.columns([2, 1])
with left:
    task_text = st.text_area("Task Requirement Description", value=default_text, height=180)
with right:
    robot_type = st.text_input("Robot Type", value=default_robot)
    drive_mode = st.text_input("Drive Method", value=default_drive)
    st.markdown(
        """
        <div class="hint-box">
        Example requirements:<br>
        • Biomedical: cell transport, obstacle-rich channel, low drift<br>
        • Microfluidic: target area navigation with disturbance compensation
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.button("Parse Requirement", type="primary", use_container_width=True):
    st.session_state["task_text"] = task_text
    st.session_state["robot_type"] = robot_type
    st.session_state["drive_mode"] = drive_mode
    st.success("Requirement saved. Next step: open Parameter Display page.")

