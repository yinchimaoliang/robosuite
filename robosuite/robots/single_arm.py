"""Backward-compatible SingleArm alias for robosuite>=1.5."""

from robosuite.robots.fixed_base_robot import FixedBaseRobot


class SingleArm(FixedBaseRobot):
    """Compatibility alias for legacy robosuite APIs."""

    pass
