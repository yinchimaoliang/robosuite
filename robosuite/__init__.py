from robosuite.environments.base import make

# Manipulation environments
from robosuite.environments.manipulation.lift import Lift
from robosuite.environments.manipulation.stack import Stack
from robosuite.environments.manipulation.nut_assembly import NutAssembly
from robosuite.environments.manipulation.pick_place import PickPlace
from robosuite.environments.manipulation.door import Door
from robosuite.environments.manipulation.wipe import Wipe
from robosuite.environments.manipulation.tool_hang import ToolHang
from robosuite.environments.manipulation.two_arm_lift import TwoArmLift
from robosuite.environments.manipulation.two_arm_peg_in_hole import TwoArmPegInHole
from robosuite.environments.manipulation.two_arm_handover import TwoArmHandover
from robosuite.environments.manipulation.two_arm_transport import TwoArmTransport

from robosuite.environments import ALL_ENVIRONMENTS
from robosuite.controllers import (
    ALL_PART_CONTROLLERS,
    load_part_controller_config,
    ALL_COMPOSITE_CONTROLLERS,
    load_composite_controller_config,
)
from robosuite.robots import ALL_ROBOTS
from robosuite.models.grippers import ALL_GRIPPERS
from robosuite.utils.log_utils import ROBOSUITE_DEFAULT_LOGGER

try:
    import robosuite_models
except:
    ROBOSUITE_DEFAULT_LOGGER.warning(
        "Could not import robosuite_models. Some robots may not be available. "
        "If you want to use these robots, please install robosuite_models from "
        "source (https://github.com/ARISE-Initiative/robosuite_models) or through pip install."
    )

try:
    from robosuite.examples.third_party_controller.mink_controller import WholeBodyMinkIK

except:
    ROBOSUITE_DEFAULT_LOGGER.warning(
        "Could not load the mink-based whole-body IK. Make sure you install related import properly, otherwise you will not be able to use the default IK controller setting for GR1 robot."
    )

__version__ = "1.5.1"
__logo__ = """
      ;     /        ,--.
     ["]   ["]  ,<  |__**|
    /[_]\  [~]\/    |//  |
     ] [   OOO      /o|__|
"""


def load_controller_config(default_controller=None, custom_fpath=None):
    """Backward-compatible API for robosuite<=1.4 callers.

    Older stacks (e.g. LIBERO) expect this function to return a controller
    config directly usable by env creation. In robosuite>=1.5, envs expect
    *composite* controller configs.
    """
    part_cfg = load_part_controller_config(
        default_controller=default_controller, custom_fpath=custom_fpath
    )
    # Convert legacy single-arm part config -> robosuite>=1.5 composite format.
    return {
        "type": "BASIC",
        "body_parts": {
            "right": {
                **part_cfg,
                "gripper": {"type": "GRIP"},
            }
        },
    }
