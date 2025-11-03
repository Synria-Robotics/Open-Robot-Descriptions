import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

h1 = SimpleNamespace()
h1.xml = os.path.join(_MODULE_PATH, "h1.xml")


