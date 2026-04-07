from __future__ import annotations

import json
from datetime import datetime

from robogenma.schemas import AgentDecision


def to_markdown_report(decision: AgentDecision) -> str:
    m = decision.result.metrics
    req = decision.request
    lines = [
        "# RobogenMA Simulation Report",
        "",
        f"- Generated: {datetime.utcnow().isoformat()}Z",
        "",
        "## Task",
        f"- Text: {req.task.task_text}",
        f"- Robot: {req.task.robot_type}",
        f"- Drive mode: {req.task.drive_mode}",
        "",
        "## Parameters",
        "```json",
        json.dumps(req.model_dump(), indent=2),
        "```",
        "",
        "## Strategy",
        f"- Summary: {req.strategy.summary}",
        "- Pseudocode:",
        "```text",
        req.strategy.pseudocode,
        "```",
        "",
        "## Results",
        f"- Success: {m.success}",
        f"- Completion rate: {m.completion_rate:.2f}",
        f"- Planned length: {m.path_length_plan:.2f}",
        f"- Executed length: {m.path_length_exec:.2f}",
        f"- Localization error: {m.localization_error:.2f}",
        f"- Runtime steps: {m.runtime_steps}",
        "",
        "## Feedback Optimization",
    ]
    for s in decision.feedback.suggestions:
        lines.append(f"- {s}")
    return "\n".join(lines)

