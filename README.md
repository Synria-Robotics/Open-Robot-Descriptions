# Synria Robotics 玄雅科技 | 机器人模型文件

[English](README_EN.md) | 中文

本仓库包含 Synria Robotics 玄雅科技机器人平台的 URDF（统一机器人描述格式）和 MJCF（MuJoCo 建模格式）模型。

## 仓库结构

```
├── robot_descriptions
│   ├── meshes
│   │   ├── Alicia_D_v5_5
│   │   ├── Alicia_D_v5_6
│   │   ├── Alicia_M_v1_0
│   │   └── Bessica_D_v1_0
│   ├── mjcf
│   │   ├── Alicia_D_v5_5
│   │   ├── Alicia_D_v5_6
│   │   ├── Alicia_M_v1_0
│   │   └── Bessica_D_v1_0
│   └── urdf
│       ├── Alicia_D_v5_5
│       ├── Alicia_D_v5_6
│       ├── Alicia_M_v1_0
│       └── Bessica_D_v1_0
```

## 产品

### Alicia-D 
- **描述**: 灵动操作臂
- **自由度**： 6
- **夹爪配置**：50mm 和 100mm
- **位置**：[`Alicia_D_v5_5`](robot_descriptions/urdf/Alicia_D_v5_5)和[`Alicia_D_v5_6`](robot_descriptions/urdf/Alicia_D_v5_6)



### Alicia-M 

- **描述**: 云擎操作臂
- **自由度**： 6
- **位置**: [`Alicia_M_v1_0.urdf`](robot_descriptions/urdf/Alicia_M_v1_0/Alicia_M_v1_0.urdf)

### Bessica-D 
- **描述**: 灵越双臂人形机器人
- **自由度**：14 （双 7 自由度机械臂）
- **外观**：无外壳版和外壳版

#### 无外壳版
- **URDF**: [`Bessica_D_v1_0_Skeleton.urdf`](robot_descriptions/urdf/Bessica_D_v1_0/Bessica_D_Skeleton.urdf)


#### 带外壳版
- **URDF**: [`Bessica_D_v1_0_Covered.urdf`](robot_descriptions/urdf/Bessica_D_v1_0/Bessica_D_Covered.urdf)
- **MuJoCo XML**: [`Bessica_D_v1_0_Covered.xml`](robot_descriptions/mjcf/Bessica_D_v1_0/Bessica_D_Covered.xml)


## 支持的仿真环境

- ROS/ROS2 (通过 URDF)
- MuJoCo (通过 MJCF)
- Gazebo (通过 URDF)
- PyBullet (通过 URDF)
- Isaac Sim (通过 URDF、MJCF)


