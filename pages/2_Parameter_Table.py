from __future__ import annotations

import json

import streamlit as st

from robogenma.agents.rk_agent import RKAgent
from robogenma.utils.ui import inject_base_style, render_app_shell

inject_base_style()
render_app_shell("parameter")
st.markdown(
    """
    <div class="panel">
      <h4>Parameter Display</h4>
      <p class="panel-sub">Structured parameters parsed by RK Agent. Values can be reviewed before simulation.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

task_text = st.session_state.get("task_text")
robot_type = st.session_state.get("robot_type", "microrobot")
drive_mode = st.session_state.get("drive_mode", "magnetic")

if not task_text:
    st.warning("No task input found. Please complete Requirement Input first.")
    st.stop()

rk = RKAgent()
task, env, constraints = rk.parse(task_text, robot_type=robot_type, drive_mode=drive_mode)
st.subheader("Parameter Sync Status")
c1, c2, c3 = st.columns(3)
c1.metric("Grid Size", f"{env.width} x {env.height}")
c2.metric("Obstacle Density", f"{constraints.obstacle_density:.2f}")
c3.metric("Disturbance", f"{constraints.disturbance_strength:.2f}")

with st.expander("Full Structured JSON", expanded=True):
    st.code(
        json.dumps(
            {
                "task": task.model_dump(),
                "environment": env.model_dump(),
                "constraints": constraints.model_dump(),
            },
            indent=2,
            ensure_ascii=True,
        ),
        language="json",
    )
st.session_state["rk_task"] = task
st.session_state["rk_env"] = env
st.session_state["rk_constraints"] = constraints

