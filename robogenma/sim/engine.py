from __future__ import annotations

from robogenma.schemas import SimulationRequest, SimulationResult
from robogenma.sim.environment import generate_environment
from robogenma.sim.planner import improved_astar
from robogenma.utils.metrics import make_metrics

Point = tuple[int, int]


class SimulationEngine:
    def run(self, request: SimulationRequest) -> SimulationResult:
        env = generate_environment(
            width=request.environment.width,
            height=request.environment.height,
            obstacle_density=request.constraints.obstacle_density,
            disturbance_strength=request.constraints.disturbance_strength,
            seed=request.environment.seed,
            start=request.environment.start,
            goal=request.environment.goal,
        )
        planned_path = improved_astar(
            env=env,
            start=request.environment.start,
            goal=request.environment.goal,
            avoid_weight=request.strategy.avoid_weight,
            disturbance_weight=request.strategy.disturbance_weight,
        )
        executed_path = self._execute_with_disturbance(
            planned_path,
            env.field,
            request.constraints.max_steps,
            request.environment.goal,
        )
        metrics = make_metrics(planned_path, executed_path, request.constraints.max_steps)
        return SimulationResult(
            planned_path=planned_path,
            executed_path=executed_path,
            obstacles=sorted(list(env.obstacles)),
            metrics=metrics,
        )

    def _execute_with_disturbance(
        self,
        path: list[Point],
        field,
        max_steps: int,
        goal: Point,
    ) -> list[Point]:
        if not path:
            return []
        out = [path[0]]
        for p in path[1:max_steps]:
            x, y = p
            disturbance = float(field[y, x])
            drift = int(round(disturbance * 0.25))  # deterministic drift for repeatability
            candidate = (x, y + drift)
            out.append(candidate)
            if candidate == goal:
                break
        return out

