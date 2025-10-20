# -*- coding: utf-8 -*-
# file: check_torch.py
# 说明：
# 本脚本用于检查 PyTorch 深度学习框架的安装状态和配置信息
# 主要检查：1) PyTorch 和 torchvision 的版本号；2) CUDA GPU 是否可用

import torch, torchvision  # 导入 PyTorch 核心库和计算机视觉工具库

# 打印 PyTorch 和 torchvision 的版本信息
print("torch", torch.__version__, "torchvision", torchvision.__version__)

# 检查 CUDA GPU 是否可用（用于加速深度学习训练），没有GPU也行，因为这个实验CPU也可以运行
print("cuda_available:", torch.cuda.is_available())
