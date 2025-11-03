import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

humanoid_template_local = SimpleNamespace()
humanoid_template_local.xml = os.path.join(_MODULE_PATH, "humanoid_template_local.xml")

mesh_humanoid = SimpleNamespace()
mesh_humanoid.xml = os.path.join(_MODULE_PATH, "mesh_humanoid.xml")

smpl_0_humanoid = SimpleNamespace()
smpl_0_humanoid.xml = os.path.join(_MODULE_PATH, "smpl_0_humanoid.xml")

smpl_1_humanoid = SimpleNamespace()
smpl_1_humanoid.xml = os.path.join(_MODULE_PATH, "smpl_1_humanoid.xml")

smpl_2_humanoid = SimpleNamespace()
smpl_2_humanoid.xml = os.path.join(_MODULE_PATH, "smpl_2_humanoid.xml")

smpl_humanoid = SimpleNamespace()
smpl_humanoid.xml = os.path.join(_MODULE_PATH, "smpl_humanoid.xml")

smpl_humanoid_0 = SimpleNamespace()
smpl_humanoid_0.xml = os.path.join(_MODULE_PATH, "smpl_humanoid_0.xml")

smpl_humanoid_1 = SimpleNamespace()
smpl_humanoid_1.xml = os.path.join(_MODULE_PATH, "smpl_humanoid_1.xml")

smpl_humanoid_xyz = SimpleNamespace()
smpl_humanoid_xyz.xml = os.path.join(_MODULE_PATH, "smpl_humanoid_xyz.xml")

smplh_humanoid = SimpleNamespace()
smplh_humanoid.xml = os.path.join(_MODULE_PATH, "smplh_humanoid.xml")

smplh_humanoid_xyz = SimpleNamespace()
smplh_humanoid_xyz.xml = os.path.join(_MODULE_PATH, "smplh_humanoid_xyz.xml")

smplx_capsule = SimpleNamespace()
smplx_capsule.xml = os.path.join(_MODULE_PATH, "smplx_capsule.xml")
