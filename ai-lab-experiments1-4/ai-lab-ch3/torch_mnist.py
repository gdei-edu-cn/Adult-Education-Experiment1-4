# -*- coding: utf-8 -*-
# file: torch_mnist.py
# 说明：
# 本脚本演示使用 PyTorch 进行 MNIST 手写数字识别的完整流程：
# 1) 数据加载与预处理；2) 构建多层感知机(MLP)模型；3) 训练与验证；4) 可视化预测结果

import torch, torch.nn as nn, torch.optim as optim  # PyTorch 核心库、神经网络模块、优化器
from torchvision import datasets, transforms  # 计算机视觉数据集和图像变换
from torch.utils.data import DataLoader  # 数据加载器，用于批量处理
import matplotlib.pyplot as plt  # 绘图库，用于可视化结果
import matplotlib
matplotlib.use('Agg')  # 设置matplotlib后端为无头模式，保存图片到文件
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']  # 设置字体，避免中文显示问题

# 1) 数据：下载MNIST到 data/，把 [0,255] 的像素转为 [0,1] 的张量
# transforms.ToTensor() 将 PIL 图像或 numpy 数组转换为张量，并自动归一化到 [0,1] 范围
tfm = transforms.Compose([transforms.ToTensor()])
# 下载并加载 MNIST 训练集（60000张28x28灰度图像，标签0-9）
train_ds = datasets.MNIST(root="data", train=True,  download=True, transform=tfm)
# 下载并加载 MNIST 测试集（10000张28x28灰度图像，标签0-9）
test_ds  = datasets.MNIST(root="data", train=False, download=True, transform=tfm)
# 训练数据加载器：批量大小64，打乱顺序，用于训练时随机采样
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)   # num_workers 默认为0，兼容Windows
# 测试数据加载器：批量大小256，不打乱，用于评估模型性能
test_loader  = DataLoader(test_ds,  batch_size=256)

# 2) 模型（简洁 MLP）：展平28x28 -> 256 -> 128 -> 10
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        # 构建多层感知机网络：输入层 -> 隐藏层1 -> 隐藏层2 -> 输出层
        self.net = nn.Sequential(
            nn.Flatten(),  # 将28x28的二维图像展平为784维向量
            nn.Linear(28*28, 256), nn.ReLU(),  # 全连接层：784 -> 256，ReLU激活函数
            nn.Linear(256, 128), nn.ReLU(),    # 全连接层：256 -> 128，ReLU激活函数
            nn.Linear(128, 10)                 # 输出层：128 -> 10（对应10个数字类别）
        )
    def forward(self, x): return self.net(x)  # 前向传播：输入x经过网络得到预测结果

device = "cuda" if torch.cuda.is_available() else "cpu"  # 自动选择GPU或CPU设备
model = MLP().to(device)  # 将模型移动到指定设备（GPU或CPU）
crit  = nn.CrossEntropyLoss()              # 交叉熵损失函数，适用于多分类任务
opt   = optim.Adam(model.parameters(), lr=1e-3)  # Adam优化器，学习率0.001

# 3) 训练/验证各跑一遍（1个epoch足够课堂展示）
def run_epoch(loader, train=True):
    model.train(train)  # 设置模型为训练模式或评估模式
    total, correct, loss_sum = 0, 0, 0.0  # 初始化统计变量：总样本数、正确预测数、总损失
    for x, y in loader:  # 遍历数据加载器中的每个批次
        x, y = x.to(device), y.to(device)  # 将数据和标签移动到指定设备
        if train: opt.zero_grad()  # 训练时清零梯度（避免梯度累积）
        out = model(x)                    # 前向传播：输入数据通过模型得到预测结果
        loss = crit(out, y)               # 计算损失：预测结果与真实标签的交叉熵
        if train:
            loss.backward()               # 反向传播：计算梯度
            opt.step()                    # 更新参数：根据梯度调整模型权重
        loss_sum += loss.item() * y.size(0)  # 累加损失（乘以批次大小得到总损失）
        preds = out.argmax(1)             # 取最大logit对应的类别作为预测结果
        correct += (preds == y).sum().item()  # 统计正确预测的数量
        total += y.size(0)  # 累加总样本数
    return loss_sum/total, correct/total  # 返回平均损失和准确率

train_loss, train_acc = run_epoch(train_loader, train=True)  # 在训练集上训练一个epoch
test_loss,  test_acc  = run_epoch(test_loader,  train=False)  # 在测试集上评估模型性能
print("Train acc={:.3f}, Test acc={:.3f}".format(train_acc, test_acc))  # 打印训练和测试准确率

# 4) 可视化6张预测结果（灰度图 + 预测标签）
x, y = next(iter(test_loader))  # 从测试集获取一个批次的数据
with torch.no_grad():  # 禁用梯度计算（节省内存，提高推理速度）
    pred = model(x.to(device)).argmax(1).cpu()  # 模型预测并将结果移回CPU
plt.figure(figsize=(12,4))  # 创建12x4英寸的图形窗口
for i in range(6):  # 显示前6张图像
    plt.subplot(1,6,i+1); plt.axis("off")  # 创建子图，关闭坐标轴
    plt.imshow(x[i][0], cmap="gray"); plt.title("Pred: {}".format(int(pred[i])))  # 显示灰度图像和预测标签
plt.tight_layout()  # 调整布局
plt.savefig('mnist_predictions.png', dpi=150, bbox_inches='tight')  # 保存图片到文件
print("预测结果已保存到 mnist_predictions.png 文件中")
print("请查看该文件来查看6张手写数字的预测结果")
