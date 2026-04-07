from __future__ import annotations

import re

from robogenma.schemas import ConstraintSpec, EnvironmentSpec, TaskInput


class RKAgent:
    """Requirement knowledge agent: parse free text into structured params."""

    _size_map = {
        "small": (24, 18),
        "medium": (40, 30),
        "large": (64, 48),
    }

    def parse(
        self,
        task_text: str,
        robot_type: str = "microrobot",
        drive_mode: str = "magnetic",
    ) -> tuple[TaskInput, EnvironmentSpec, ConstraintSpec]:
        txt = task_text.lower()
        task = TaskInput(task_text=task_text, robot_type=robot_type, drive_mode=drive_mode)

        width, height = self._infer_size(txt)
        start = self._extract_point(txt, "start") or (1, 1)
        goal = self._extract_point(txt, "goal") or (width - 5, height - 5)
        density = 0.25 if "complex" in txt else 0.15
        if "easy" in txt or "simple" in txt:
            density = 0.1
        disturbance = 0.35 if "disturb" in txt else 0.2

        env = EnvironmentSpec(width=width, height=height, start=start, goal=goal, seed=42)
        constraints = ConstraintSpec(
            max_steps=width * height,
            obstacle_density=density,
            disturbance_strength=disturbance,
        )
        return task, env, constraints

    def _infer_size(self, txt: str) -> tuple[int, int]:
        for key, val in self._size_map.items():
            if key in txt:
                return val
        m = re.search(r"(\d+)\s*x\s*(\d+)", txt)
        if m:
            return int(m.group(1)), int(m.group(2))
        return self._size_map["medium"]

    @staticmethod
    def _extract_point(txt: str, key: str) -> tuple[int, int] | None:
        m = re.search(rf"{key}\s*[:=]?\s*\(?\s*(\d+)\s*,\s*(\d+)\s*\)?", txt)
        if not m:
            return None
        return int(m.group(1)), int(m.group(2))

