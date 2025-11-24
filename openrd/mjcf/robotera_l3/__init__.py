import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

robotera_l3 = SimpleNamespace()
robotera_l3.xml = os.path.join(_MODULE_PATH, "robotera_l3.xml")
