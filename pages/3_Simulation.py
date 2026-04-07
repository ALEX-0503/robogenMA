from __future__ import annotations

import streamlit as st

from robogenma.agents.main_agent import MainAgent
from robogenma.utils.seed import set_global_seed
from robogenma.utils.visualization import make_trajectory_figure

st.title("Simulation")

task_text = st.session_state.get("task_text")
if not task_text:
    st.warning("No task input yet. Go to Task Input page first.")
    st.stop()

seed = st.number_input("Random seed", min_value=0, max_value=10_000, value=42, step=1)
if st.button("Run RK -> CS -> Sim -> FO", type="primary"):
    set_global_seed(seed)
    main_agent = MainAgent()
    decision = main_agent.run(
        task_text=task_text,
        robot_type=st.session_state.get("robot_type", "microrobot"),
        drive_mode=st.session_state.get("drive_mode", "magnetic"),
    )
    decision.request.environment.seed = int(seed)
    st.session_state["decision"] = decision
    st.success("Simulation complete.")

decision = st.session_state.get("decision")
if decision:
    fig = make_trajectory_figure(
        width=decision.request.environment.width,
        height=decision.request.environment.height,
        obstacles=decision.result.obstacles,
        planned_path=decision.result.planned_path,
        executed_path=decision.result.executed_path,
    )
    st.pyplot(fig)
    st.caption("Blue: planned path. Orange dashed: executed path.")
else:
    st.info("Run simulation to generate trajectory and metrics.")

