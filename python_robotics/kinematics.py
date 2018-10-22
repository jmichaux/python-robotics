import numpy as np
from utils.transforms import *
from utils.urdf import *

class Kinematics():
    def __init__(self, urdf_str, first_joint, last_joint, world_transform=None):
        self.chain = URDFChain(urdf_str, first_joint, last_joint)
        if world_transform is None:
            self.world_transform = np.eye(4)
        else:
            self.world_transform = world_transform
        return

    def forward_kinematics(self, joint_positions):
        """
        Return forward kinematics
        """
        assert (len(joint_positions) == self.n_active)
        H = self.world_transform
        j = 0
        for i in range(len(self._all_joints)):
            if self._all_joints[i].type == "revolute":
                theta = joint_positions[j]
                j += 1
            else:
                theta = 0
            H = H.dot(self._all_joints[i].transform(theta))
        return H

    def inverse_kinematics(self, ee_pos, ee_orn=None):
        raise NotImplentedError()