from robogenma.agents.main_agent import MainAgent


def test_main_workflow_smoke():
    agent = MainAgent()
    decision = agent.run("simple navigation in medium map start(1,1) goal(20,14)")
    assert decision.request.strategy.planner == "improved_astar"
    assert decision.result.metrics.runtime_steps >= 0
    assert len(decision.feedback.suggestions) >= 1

