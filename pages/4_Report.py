from __future__ import annotations

import streamlit as st

from robogenma.utils.report import to_markdown_report
from robogenma.utils.ui import inject_base_style, render_app_shell
from robogenma.utils.visualization import metrics_dataframe

inject_base_style()
render_app_shell("report")
st.markdown(
    """
    <div class="panel">
      <h4>Result Report</h4>
      <p class="panel-sub">Review core metrics, optimization suggestions, and export markdown report.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

decision = st.session_state.get("decision")
if not decision:
    st.warning("No simulation result found. Please run Strategy & Simulation first.")
    st.stop()

metrics = decision.result.metrics
c1, c2, c3 = st.columns(3)
c1.metric("Completion Rate", f"{metrics.completion_rate:.2f}")
c2.metric("Localization Error", f"{metrics.localization_error:.2f}")
c3.metric("Runtime Steps", metrics.runtime_steps)

st.subheader("Metrics Dashboard")
df = metrics_dataframe(metrics)
st.dataframe(df, use_container_width=True)
st.bar_chart(df.set_index("metric"))

with st.expander("Feedback Suggestions", expanded=True):
    for item in decision.feedback.suggestions:
        st.write(f"- {item}")

report_md = to_markdown_report(decision)
btn_col, _ = st.columns([1, 2])
with btn_col:
    st.download_button(
        label="Download Markdown Report",
        data=report_md,
        file_name="robogenma_report.md",
        mime="text/markdown",
        use_container_width=True,
    )

with st.expander("Report Preview", expanded=False):
    st.text_area("Markdown Content", value=report_md, height=340)

