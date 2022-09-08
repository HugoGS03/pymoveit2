from typing import List

MOVE_GROUP_ARM: str = "arm"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.4, 1.4, 0.4, 1.4, 0.4, 1.4]


def joint_names(prefix: str = "j2s6s300_") -> List[str]:
    return [
        prefix + "joint1",
        prefix + "joint2",
        prefix + "joint3",
        prefix + "joint4",
        prefix + "joint5",
        prefix + "joint6",
        prefix + "joint7",
    ]


def base_link_name(prefix: str = "j2s6s300_") -> str:
    return 'j2s6s300_link_base' #prefix + "link0"


def end_effector_name(prefix: str = "j2s6s300_") -> str:
    return prefix + "end_effector"


def gripper_joint_names(prefix: str = "j2s6s300_") -> List[str]:
    return [
        prefix + "joint_finger_1",
        prefix + "joint_finger_tip_1",
        prefix + "joint_finger_2",
        prefix + "joint_finger_tip_2",
        prefix + "joint_finger_3",
        prefix + "joint_finger_tip_3",
    ]
