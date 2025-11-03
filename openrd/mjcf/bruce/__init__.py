import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

bruce_20250220 = SimpleNamespace()
bruce_20250220.xml = os.path.join(_MODULE_PATH, "bruce_20250220.xml")
