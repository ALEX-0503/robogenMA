from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from robogenma.schemas import SimulationMetrics

Point = tuple[int, int]


def make_trajectory_figure(
    width: int,
    height: int,
    obstacles: list[Point],
    planned_path: list[Point],
    executed_path: list[Point],
):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_title("Trajectory Overview")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    if obstacles:
        ox, oy = zip(*obstacles)
        ax.scatter(ox, oy, s=10, c="black", alpha=0.5, label="Obstacles")
    if planned_path:
        px, py = zip(*planned_path)
        ax.plot(px, py, color="tab:blue", linewidth=2, label="Planned")
        ax.scatter([px[0], px[-1]], [py[0], py[-1]], c=["green", "red"], s=50)
    if executed_path:
        ex, ey = zip(*executed_path)
        ax.plot(ex, ey, color="tab:orange", linestyle="--", linewidth=2, label="Executed")
    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)
    return fig


def metrics_dataframe(metrics: SimulationMetrics) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "metric": [
                "completion_rate",
                "path_length_plan",
                "path_length_exec",
                "localization_error",
                "runtime_steps",
            ],
            "value": [
                metrics.completion_rate,
                metrics.path_length_plan,
                metrics.path_length_exec,
                metrics.localization_error,
                metrics.runtime_steps,
            ],
        }
    )

