from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

Point = tuple[int, int]


@dataclass
class GridEnvironment:
    width: int
    height: int
    obstacles: set[Point]
    field: np.ndarray  # shape (h, w) disturbance costs

    def in_bounds(self, p: Point) -> bool:
        x, y = p
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, p: Point) -> bool:
        return p not in self.obstacles

    def neighbors(self, p: Point) -> Iterable[Point]:
        x, y = p
        for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if self.in_bounds(n) and self.passable(n):
                yield n


def generate_environment(
    width: int,
    height: int,
    obstacle_density: float,
    disturbance_strength: float,
    seed: int,
    start: Point,
    goal: Point,
) -> GridEnvironment:
    rng = np.random.default_rng(seed)
    obstacle_mask = rng.random((height, width)) < obstacle_density
    obstacle_mask[start[1], start[0]] = False
    obstacle_mask[goal[1], goal[0]] = False
    ys, xs = np.where(obstacle_mask)
    obstacles = set(zip(xs.tolist(), ys.tolist()))

    x = np.linspace(0, np.pi * 2, width)
    y = np.linspace(0, np.pi * 2, height)
    xx, yy = np.meshgrid(x, y)
    field = disturbance_strength * (np.sin(xx) * np.cos(yy) + 1.0)

    return GridEnvironment(width=width, height=height, obstacles=obstacles, field=field)

