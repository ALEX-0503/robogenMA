from __future__ import annotations

import json

import streamlit as st

from robogenma.agents.rk_agent import RKAgent

st.title("Parameter Table (RK Agent)")

task_text = st.session_state.get("task_text")
robot_type = st.session_state.get("robot_type", "microrobot")
drive_mode = st.session_state.get("drive_mode", "magnetic")

if not task_text:
    st.warning("No task input yet. Go to Task Input page first.")
    st.stop()

rk = RKAgent()
task, env, constraints = rk.parse(task_text, robot_type=robot_type, drive_mode=drive_mode)
st.subheader("Structured task parameters")
st.code(
    json.dumps(
        {
            "task": task.model_dump(),
            "environment": env.model_dump(),
            "constraints": constraints.model_dump(),
        },
        indent=2,
    ),
    language="json",
)
st.session_state["rk_task"] = task
st.session_state["rk_env"] = env
st.session_state["rk_constraints"] = constraints

