from __future__ import annotations

from robogenma.schemas import FeedbackResult, SimulationResult, StrategySpec


class FOAgent:
    """Feedback optimization agent: tune strategy from simulation outcome."""

    def optimize(self, strategy: StrategySpec, result: SimulationResult) -> FeedbackResult:
        suggestions: list[str] = []
        tuned = strategy.model_copy(deep=True)
        m = result.metrics

        if not m.success:
            tuned.avoid_weight = min(5.0, tuned.avoid_weight + 0.4)
            tuned.disturbance_weight = min(5.0, tuned.disturbance_weight + 0.3)
            suggestions.append("Path failed: increase avoid/disturbance weights and retry.")
        if m.localization_error > 2.0:
            tuned.step_size = 1
            suggestions.append("High localization error: use conservative step size.")
        if m.path_length_exec > m.path_length_plan * 1.25:
            tuned.disturbance_weight = min(5.0, tuned.disturbance_weight + 0.2)
            suggestions.append("Execution drift detected: strengthen disturbance compensation.")
        if not suggestions:
            suggestions.append("Performance is stable. Keep current parameters.")

        return FeedbackResult(suggestions=suggestions, tuned_strategy=tuned)

