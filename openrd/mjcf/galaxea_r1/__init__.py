import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

r1_pro = SimpleNamespace()
r1_pro.xml = os.path.join(_MODULE_PATH, "r1_pro.xml")

