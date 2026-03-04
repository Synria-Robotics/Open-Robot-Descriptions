import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))


panda = SimpleNamespace()
panda.xml = os.path.join(_MODULE_PATH, "franka_panda.xml")

panda_scene = SimpleNamespace()
panda_scene.xml = os.path.join(_MODULE_PATH, "franka_panda_scene.xml")

panda_nohand = SimpleNamespace()
panda_nohand.xml = os.path.join(_MODULE_PATH, "franka_panda_nohand.xml")

panda_hand = SimpleNamespace()
panda_hand.xml = os.path.join(_MODULE_PATH, "franka_panda_hand.xml")
