from __future__ import annotations

from robogenma.agents.cs_agent import CSAgent
from robogenma.agents.fo_agent import FOAgent
from robogenma.agents.rk_agent import RKAgent
from robogenma.schemas import AgentDecision, SimulationRequest
from robogenma.sim import SimulationEngine


class MainAgent:
    """Orchestrates RK -> CS -> Sim -> FO workflow."""

    def __init__(self) -> None:
        self.rk = RKAgent()
        self.cs = CSAgent()
        self.sim = SimulationEngine()
        self.fo = FOAgent()

    def run(self, task_text: str, robot_type: str = "microrobot", drive_mode: str = "magnetic") -> AgentDecision:
        task, env, constraints = self.rk.parse(task_text, robot_type=robot_type, drive_mode=drive_mode)
        strategy = self.cs.plan(task, env, constraints)
        request = SimulationRequest(task=task, constraints=constraints, environment=env, strategy=strategy)
        result = self.sim.run(request)
        feedback = self.fo.optimize(strategy, result)
        return AgentDecision(request=request, result=result, feedback=feedback)

