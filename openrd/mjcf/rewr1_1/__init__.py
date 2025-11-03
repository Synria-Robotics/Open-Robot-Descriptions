import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

rewr1_1 = SimpleNamespace()
rewr1_1.xml = os.path.join(_MODULE_PATH, "rewr1_1.xml")


