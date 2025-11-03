import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

gr3 = SimpleNamespace()
gr3.xml = os.path.join(_MODULE_PATH, "gr3.xml")
