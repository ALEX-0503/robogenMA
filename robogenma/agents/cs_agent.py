from __future__ import annotations

from robogenma.schemas import ConstraintSpec, EnvironmentSpec, StrategySpec, TaskInput


class CSAgent:
    """Control strategy agent: build planning + control configuration."""

    def plan(
        self,
        task: TaskInput,
        env: EnvironmentSpec,
        constraints: ConstraintSpec,
    ) -> StrategySpec:
        avoid_weight = 1.4 + constraints.obstacle_density * 1.8
        disturbance_weight = 1.0 + constraints.disturbance_strength * 0.8

        summary = (
            f"Use improved A* on {env.width}x{env.height} grid, prioritize obstacle "
            "clearance and disturbance compensation."
        )
        pseudocode = "\n".join(
            [
                "OPEN <- {start}",
                "while OPEN not empty:",
                "  node <- min_f(OPEN), f=g+h+disturbance+clearance_penalty",
                "  if node == goal: reconstruct path",
                "  for each neighbor: relax edge and update OPEN",
            ]
        )
        return StrategySpec(
            planner="improved_astar",
            step_size=1,
            avoid_weight=avoid_weight,
            disturbance_weight=disturbance_weight,
            summary=summary,
            pseudocode=pseudocode,
        )

