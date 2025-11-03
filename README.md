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

## 支持的仿真环境

- **SparkVis (通过 URDF、MJCF) - Synria Robotics 自研的统一机器人可视化交互控制软件**
- ROS/ROS2 (通过 URDF)
- MuJoCo (通过 MJCF)
- Gazebo (通过 URDF)
- PyBullet (通过 URDF)
- Isaac Sim (通过 URDF、MJCF)
