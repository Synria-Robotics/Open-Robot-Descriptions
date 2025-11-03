# OpenRD：开源机器人标准模型文件

本仓库包含开源机器人平台的 URDF（统一机器人描述格式）和 MJCF（MuJoCo 建模格式）模型。

## 仓库结构

```
├── openrd
│   ├── meshes
│   │   ├── unitree_g1
│   │   ├── unitree_h1
│   │   ├── fourier_gr3
│   │   └── ...
│   ├── mjcf
│   │   ├── unitree_g1
│   │   ├── unitree_h1
│   │   ├── fourier_gr3
│   │   └── ...
│   └── urdf
│       ├── unitree_g1
│       ├── unitree_h1
│       ├── fourier_gr3
│       └── ...
```

## 命名规范

Open-Robot-Descriptions 中的机器人模型命名较为灵活，大部分机器人没有明确的版本号和变体标识。文件名和对象名遵循以下原则：

- 对于没有版本和变体的机器人：文件名和对象名通常为机器人名称本身（如 `bruce.urdf`）
- 对于有变体的机器人（如 `smpl`）：文件名和对象名为变体名称（如 `smpl_humanoid.xml`）
- 特殊情况（如 `bruce` 的 MJCF 格式）：文件名可能包含日期或其他标识（如 `bruce_20250220.xml`）

### 使用 API

```python
from openrd import get_model_path, list_available_models

# 获取模型路径
urdf_path = get_model_path("bruce")
mjcf_path = get_model_path("bruce", variant="bruce_20250220", model_format="mjcf")

# 对于有变体的机器人（如 smpl）
smpl_path = get_model_path("smpl", variant="smpl_humanoid", model_format="mjcf")

# 列出所有可用模型
print(list_available_models(model_format="urdf"))
print(list_available_models(model_format="mjcf", show_path=True))
```

## 支持的仿真环境

- **SparkVis (通过 URDF、MJCF) - Synria Robotics 自研的统一机器人可视化交互控制软件**
- ROS/ROS2 (通过 URDF)
- MuJoCo (通过 MJCF)
- Gazebo (通过 URDF)
- PyBullet (通过 URDF)
- Isaac Sim (通过 URDF、MJCF)
