from __future__ import annotations

import streamlit as st

from robogenma.utils.report import to_markdown_report
from robogenma.utils.visualization import metrics_dataframe

st.title("Report")

decision = st.session_state.get("decision")
if not decision:
    st.warning("No simulation result yet. Run Simulation first.")
    st.stop()

metrics = decision.result.metrics
c1, c2, c3 = st.columns(3)
c1.metric("Completion Rate", f"{metrics.completion_rate:.2f}")
c2.metric("Localization Error", f"{metrics.localization_error:.2f}")
c3.metric("Runtime Steps", metrics.runtime_steps)

st.subheader("Metrics Table")
df = metrics_dataframe(metrics)
st.dataframe(df, use_container_width=True)
st.bar_chart(df.set_index("metric"))

st.subheader("Feedback Suggestions")
for item in decision.feedback.suggestions:
    st.write(f"- {item}")

report_md = to_markdown_report(decision)
st.download_button(
    label="Download Markdown report",
    data=report_md,
    file_name="robogenma_report.md",
    mime="text/markdown",
)
st.text_area("Report preview", value=report_md, height=320)

