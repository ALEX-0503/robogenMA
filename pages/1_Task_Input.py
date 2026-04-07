from __future__ import annotations

from pathlib import Path

import streamlit as st

from robogenma.utils.io import load_json

st.title("Task Input")

example_dir = Path("data/examples")
example_files = sorted([p.name for p in example_dir.glob("*.json")])
choice = st.selectbox("Example scenario", ["(none)"] + example_files)

default_text = "Navigate in a medium grid from start(1,1) to goal(35,25) with mild disturbance."
default_robot = "microrobot"
default_drive = "magnetic"

if choice != "(none)":
    data = load_json(example_dir / choice)
    default_text = data["task_text"]
    default_robot = data.get("robot_type", default_robot)
    default_drive = data.get("drive_mode", default_drive)

task_text = st.text_area("Task Description", value=default_text, height=140)
robot_type = st.text_input("Robot Type", value=default_robot)
drive_mode = st.text_input("Drive Mode", value=default_drive)

if st.button("Save task input", type="primary"):
    st.session_state["task_text"] = task_text
    st.session_state["robot_type"] = robot_type
    st.session_state["drive_mode"] = drive_mode
    st.success("Task input saved. Next: Parameter Table page.")

