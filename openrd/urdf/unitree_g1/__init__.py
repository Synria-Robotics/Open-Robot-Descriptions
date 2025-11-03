import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

g1 = SimpleNamespace()
g1.urdf = os.path.join(_MODULE_PATH, "g1.urdf")


