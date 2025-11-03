import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

tienkung_1 = SimpleNamespace()
tienkung_1.urdf = os.path.join(_MODULE_PATH, "tienkung_1.urdf")
