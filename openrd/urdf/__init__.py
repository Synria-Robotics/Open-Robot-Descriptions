# This line makes the sub-folders available as attributes of this module
from . import bruce
from . import fourier_gr3
from . import rewr1_1
from . import unitree_g1

# 注意：不要在此处导入具体的 URDF 命名空间对象（例如 bruce.bruce），
# 否则在某些环境下会触发"partially initialized module"循环导入错误。
# 正确用法：通过子包访问，如
#   from openrd import urdf
#   urdf_path = urdf.bruce.bruce.urdf

__all__ = [
    "bruce",
    "fourier_gr3",
    "rewr1_1",
    "unitree_g1",
]


