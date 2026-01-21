import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

g1 = SimpleNamespace()
g1.xml = os.path.join(_MODULE_PATH, "g1.xml")

g1_body29_hand14 = SimpleNamespace()
g1_body29_hand14.xml = os.path.join(_MODULE_PATH, "g1_body29_hand14.xml")

g1_body29_hand14_interactive = SimpleNamespace()
g1_body29_hand14_interactive.xml = os.path.join(_MODULE_PATH, "g1_body29_hand14_interactive.xml")
