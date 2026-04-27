"""Backward-compatible SingleArmEnv for robosuite>=1.5.

This module restores the legacy import path used by older projects:
`robosuite.environments.manipulation.single_arm_env.SingleArmEnv`.
"""

from robosuite.environments.manipulation.manipulation_env import ManipulationEnv


class SingleArmEnv(ManipulationEnv):
    """Compatibility wrapper around ManipulationEnv.

    robosuite 1.5 removed `single_arm_env.py` and renamed some constructor
    arguments. Older stacks (e.g. LIBERO) still instantiate `SingleArmEnv`
    and pass `mount_types`. We map that to the new `base_types`.
    """

    def __init__(
        self,
        robots,
        env_configuration="default",
        controller_configs=None,
        mount_types="default",
        gripper_types="default",
        initialization_noise="default",
        use_camera_obs=True,
        has_renderer=False,
        has_offscreen_renderer=True,
        render_camera="frontview",
        render_collision_mesh=False,
        render_visual_mesh=True,
        render_gpu_device_id=-1,
        control_freq=20,
        horizon=1000,
        ignore_done=False,
        hard_reset=True,
        camera_names="agentview",
        camera_heights=256,
        camera_widths=256,
        camera_depths=False,
        camera_segmentations=None,
        renderer="mujoco",
        renderer_config=None,
        seed=None,
        **kwargs,
    ):
        # robosuite<=1.4 used "mount_types"; robosuite>=1.5 uses "base_types".
        base_types = kwargs.pop("base_types", mount_types)

        # Keep legacy behavior (pre-1.5 physics stepping) unless overridden.
        lite_physics = kwargs.pop("lite_physics", False)

        super().__init__(
            robots=robots,
            env_configuration=env_configuration,
            controller_configs=controller_configs,
            base_types=base_types,
            gripper_types=gripper_types,
            initialization_noise=initialization_noise,
            use_camera_obs=use_camera_obs,
            has_renderer=has_renderer,
            has_offscreen_renderer=has_offscreen_renderer,
            render_camera=render_camera,
            render_collision_mesh=render_collision_mesh,
            render_visual_mesh=render_visual_mesh,
            render_gpu_device_id=render_gpu_device_id,
            control_freq=control_freq,
            lite_physics=lite_physics,
            horizon=horizon,
            ignore_done=ignore_done,
            hard_reset=hard_reset,
            camera_names=camera_names,
            camera_heights=camera_heights,
            camera_widths=camera_widths,
            camera_depths=camera_depths,
            camera_segmentations=camera_segmentations,
            renderer=renderer,
            renderer_config=renderer_config,
            seed=seed,
            **kwargs,
        )
