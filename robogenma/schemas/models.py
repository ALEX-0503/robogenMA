from __future__ import annotations

from typing import List, Tuple

from pydantic import BaseModel, Field

Point = Tuple[int, int]


class TaskInput(BaseModel):
    task_text: str = Field(..., min_length=5)
    robot_type: str = "microrobot"
    drive_mode: str = "magnetic"


class ConstraintSpec(BaseModel):
    max_steps: int = 500
    obstacle_density: float = Field(0.15, ge=0.0, le=0.6)
    disturbance_strength: float = Field(0.2, ge=0.0, le=2.0)


class EnvironmentSpec(BaseModel):
    width: int = Field(40, ge=8, le=120)
    height: int = Field(30, ge=8, le=120)
    start: Point = (1, 1)
    goal: Point = (35, 25)
    seed: int = 42


class StrategySpec(BaseModel):
    planner: str = "improved_astar"
    step_size: int = 1
    avoid_weight: float = Field(1.6, ge=0.1, le=5.0)
    disturbance_weight: float = Field(1.0, ge=0.1, le=5.0)
    pseudocode: str = ""
    summary: str = ""


class SimulationRequest(BaseModel):
    task: TaskInput
    constraints: ConstraintSpec
    environment: EnvironmentSpec
    strategy: StrategySpec


class SimulationMetrics(BaseModel):
    success: bool
    completion_rate: float
    path_length_plan: float
    path_length_exec: float
    localization_error: float
    runtime_steps: int


class SimulationResult(BaseModel):
    planned_path: List[Point]
    executed_path: List[Point]
    obstacles: List[Point]
    metrics: SimulationMetrics


class FeedbackResult(BaseModel):
    suggestions: List[str]
    tuned_strategy: StrategySpec


class AgentDecision(BaseModel):
    request: SimulationRequest
    result: SimulationResult
    feedback: FeedbackResult

