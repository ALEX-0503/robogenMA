from __future__ import annotations

import time

import streamlit as st

from robogenma.agents.main_agent import MainAgent
from robogenma.utils.seed import set_global_seed
from robogenma.utils.ui import inject_base_style, render_app_shell, render_stage_progress
from robogenma.utils.visualization import make_trajectory_figure

inject_base_style()
render_app_shell("simulation")
render_stage_progress("simulation")
st.markdown(
    """
    <div class="panel">
      <h4>Simulation Control</h4>
      <p class="panel-sub">Run full workflow and evaluate robot trajectory and feedback metrics.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

task_text = st.session_state.get("task_text")
if not task_text:
    st.warning("No task input found. Please complete Requirement Input first.")
    st.stop()

info_col, action_col = st.columns([2, 1])
with info_col:
    st.markdown("Workflow: `RK -> CS -> Simulation -> FO`")
with action_col:
    seed = st.number_input("Random Seed", min_value=0, max_value=10_000, value=42, step=1)

if st.button("Start Simulation", type="primary", use_container_width=True):
    progress = st.progress(0)
    status = st.empty()
    status.info("Initializing simulation kernel...")
    time.sleep(0.25)
    progress.progress(30)
    status.info("Running RK/CS pipeline...")

    set_global_seed(seed)
    main_agent = MainAgent()
    decision = main_agent.run(
        task_text=task_text,
        robot_type=st.session_state.get("robot_type", "microrobot"),
        drive_mode=st.session_state.get("drive_mode", "magnetic"),
    )
    progress.progress(80)
    status.info("Applying FO feedback and preparing report...")
    time.sleep(0.25)
    decision.request.environment.seed = int(seed)
    st.session_state["decision"] = decision
    progress.progress(100)
    status.success("Simulation complete. Redirecting to Result Report...")
    time.sleep(0.35)
    st.switch_page("pages/4_Report.py")

decision = st.session_state.get("decision")
if decision:
    m = decision.result.metrics
    st.markdown('<div class="metric-row">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Duration", f"{m.runtime_steps/10:.1f}s")
    c2.metric("Final Error", f"±{m.localization_error:.2f}")
    c3.metric("Path Drift Ratio", f"{(m.path_length_exec / max(m.path_length_plan, 1e-6)):.2f}")
    c4.metric("Task Completion", f"{m.completion_rate*100:.0f}%")
    st.markdown("</div>", unsafe_allow_html=True)

    fig = make_trajectory_figure(
        width=decision.request.environment.width,
        height=decision.request.environment.height,
        obstacles=decision.result.obstacles,
        planned_path=decision.result.planned_path,
        executed_path=decision.result.executed_path,
    )
    with st.expander("Robot Trajectory", expanded=True):
        st.pyplot(fig)
        st.caption("Blue: planned path. Orange dashed: executed path.")

    with st.expander("Optimization Suggestions", expanded=True):
        st.write(f"Strategy summary: {decision.request.strategy.summary}")
        for tip in decision.feedback.suggestions:
            st.write(f"- {tip}")
else:
    st.info("Click Start Simulation to generate trajectory and metrics.")

