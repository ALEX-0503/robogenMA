from __future__ import annotations

import math

from robogenma.schemas import SimulationMetrics

Point = tuple[int, int]


def path_length(path: list[Point]) -> float:
    if len(path) < 2:
        return 0.0
    length = 0.0
    for i in range(1, len(path)):
        dx = path[i][0] - path[i - 1][0]
        dy = path[i][1] - path[i - 1][1]
        length += math.hypot(dx, dy)
    return length


def make_metrics(planned: list[Point], executed: list[Point], max_steps: int) -> SimulationMetrics:
    success = bool(executed and planned and executed[-1] == planned[-1])
    completion_rate = 1.0 if success else min(1.0, len(executed) / max(1, len(planned)))
    p_len = path_length(planned)
    e_len = path_length(executed)
    if planned and executed:
        ex, ey = executed[-1]
        gx, gy = planned[-1]
        localization_error = math.hypot(ex - gx, ey - gy)
    else:
        localization_error = float("inf")
    runtime_steps = min(max_steps, len(executed))
    return SimulationMetrics(
        success=success,
        completion_rate=completion_rate,
        path_length_plan=p_len,
        path_length_exec=e_len,
        localization_error=localization_error,
        runtime_steps=runtime_steps,
    )

