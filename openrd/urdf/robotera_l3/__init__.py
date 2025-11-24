import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

rel3_4_pelvis_modify_intertial_raw_torso_base_link = SimpleNamespace()
rel3_4_pelvis_modify_intertial_raw_torso_base_link.urdf = os.path.join(_MODULE_PATH, "rel3_4_pelvis_modify_intertial_raw_torso_base_link.urdf")

robotera_l3 = SimpleNamespace()
robotera_l3.urdf = os.path.join(_MODULE_PATH, "robotera_l3.urdf")
