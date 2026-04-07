from robogenma.agents.rk_agent import RKAgent


def test_rk_parse_basic():
    rk = RKAgent()
    task, env, constraints = rk.parse("simple mission in medium map start(1,1) goal(10,12)")
    assert task.robot_type == "microrobot"
    assert env.start == (1, 1)
    assert env.goal == (10, 12)
    assert 0.0 <= constraints.obstacle_density <= 0.6

