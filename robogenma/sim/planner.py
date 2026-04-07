from __future__ import annotations

import heapq
import math

from robogenma.sim.environment import GridEnvironment

Point = tuple[int, int]


def _manhattan(a: Point, b: Point) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _clearance_penalty(env: GridEnvironment, p: Point) -> float:
    x, y = p
    penalty = 0.0
    for nx in range(max(0, x - 1), min(env.width, x + 2)):
        for ny in range(max(0, y - 1), min(env.height, y + 2)):
            if (nx, ny) in env.obstacles:
                penalty += 1.0
    return penalty


def improved_astar(
    env: GridEnvironment,
    start: Point,
    goal: Point,
    avoid_weight: float,
    disturbance_weight: float,
) -> list[Point]:
    open_heap: list[tuple[float, Point]] = [(0.0, start)]
    came_from: dict[Point, Point | None] = {start: None}
    g_score: dict[Point, float] = {start: 0.0}

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return _reconstruct(came_from, current)

        for nxt in env.neighbors(current):
            disturbance_cost = float(env.field[nxt[1], nxt[0]]) * disturbance_weight
            clearance_cost = _clearance_penalty(env, nxt) * avoid_weight * 0.15
            tentative_g = g_score[current] + 1.0 + disturbance_cost + clearance_cost
            if tentative_g < g_score.get(nxt, math.inf):
                g_score[nxt] = tentative_g
                came_from[nxt] = current
                f = tentative_g + _manhattan(nxt, goal)
                heapq.heappush(open_heap, (f, nxt))
    return []


def _reconstruct(came_from: dict[Point, Point | None], node: Point) -> list[Point]:
    path = [node]
    while came_from[node] is not None:
        node = came_from[node]  # type: ignore[assignment]
        path.append(node)
    path.reverse()
    return path

