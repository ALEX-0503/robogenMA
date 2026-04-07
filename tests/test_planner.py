from robogenma.sim.environment import generate_environment
from robogenma.sim.planner import improved_astar


def test_improved_astar_finds_path_on_sparse_grid():
    env = generate_environment(
        width=20,
        height=15,
        obstacle_density=0.05,
        disturbance_strength=0.2,
        seed=42,
        start=(1, 1),
        goal=(18, 13),
    )
    path = improved_astar(
        env=env,
        start=(1, 1),
        goal=(18, 13),
        avoid_weight=1.5,
        disturbance_weight=1.0,
    )
    assert path
    assert path[0] == (1, 1)
    assert path[-1] == (18, 13)

