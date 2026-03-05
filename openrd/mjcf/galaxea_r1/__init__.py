import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

galaxea_r1 = SimpleNamespace()
galaxea_r1.xml = os.path.join(_MODULE_PATH, "galaxea_r1.xml")

