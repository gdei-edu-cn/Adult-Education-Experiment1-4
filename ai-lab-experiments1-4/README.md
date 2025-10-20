# 人工智能导论实验课程

## 📚 课程简介
本课程包含4个实验，从Python基础到AI应用开发，帮助零基础学生逐步掌握人工智能相关技术。

## 🎯 学习目标
- 掌握Python编程基础
- 理解机器学习算法原理
- 学会深度学习框架使用
- 开发AI应用项目

## 📋 实验安排

### 实验1：Python环境测试
- **文件位置**：`ai-lab-ch1/`
- **主要内容**：Python安装验证、基础语法测试
- **难度**：⭐⭐☆☆☆
- **预计时间**：30分钟
- **前置要求**：已安装Python

### 实验2：机器学习基础
- **文件位置**：`ai-lab-ch2/`
- **主要内容**：线性回归、K-means聚类
- **难度**：⭐⭐⭐☆☆
- **预计时间**：2小时
- **前置要求**：完成实验1

### 实验3：深度学习入门
- **文件位置**：`ai-lab-ch3/`
- **主要内容**：PyTorch框架、MNIST手写数字识别
- **难度**：⭐⭐⭐⭐☆
- **预计时间**：3小时
- **前置要求**：完成实验2

### 实验4：AI个人助理开发
- **文件位置**：`ai-lab-ch4/`
- **主要内容**：API调用、多功能AI助理
- **难度**：⭐⭐⭐⭐⭐
- **预计时间**：4小时
- **前置要求**：完成实验3

## 🛠️ 环境准备

### 必需软件
1. **Python 3.7+**
   - 下载地址：https://www.python.org/downloads/
   - 安装时勾选"Add Python to PATH"

2. **文本编辑器**
   - **VS Code**（推荐）：https://code.visualstudio.com/

3. **命令行工具**
   - **Windows**：命令提示符（cmd）或PowerShell
   - **Mac**：终端（Terminal）
   - **Linux**：终端（Terminal）

### 网络要求
- 稳定的互联网连接
- 能够访问GitHub、PyPI等网站
- 实验4需要访问硅基流动API

## 📦 依赖包安装

### 实验1：无需额外包
- 只需要Python基础环境

### 实验2：机器学习包
```bash
pip install numpy pandas scikit-learn matplotlib joblib
```

### 实验3：深度学习包
```bash
# CPU版本（推荐初学者）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install matplotlib

# 或访问 https://pytorch.org/get-started/locally/ 获取适合你系统的安装命令
```

### 实验4：API调用包
```bash
pip install requests
```

## 🚀 快速开始

### 1. 检查Python环境
```bash
python --version
```
应该显示Python 3.7或更高版本。

### 2. 检查pip工具
pip是Python的包管理工具，通常随Python一起安装：
```bash
pip --version
```
如果显示版本信息，说明pip已安装。如果提示"pip不是内部或外部命令"，请参考下面的安装方法。

#### pip安装方法
如果pip未安装，请按以下步骤安装：

**Windows用户**：
1. 重新安装Python，确保勾选"Add Python to PATH"
2. 或手动安装pip：下载 https://bootstrap.pypa.io/get-pip.py
3. 运行：`python get-pip.py`

**Mac用户**：
```bash
# 使用Homebrew安装
brew install python

# 或使用系统Python
python3 -m ensurepip --upgrade
```

**Linux用户**：
```bash
# Ubuntu/Debian
sudo apt-get install python3-pip

# CentOS/RHEL
sudo yum install python3-pip
```

### 3. 进入实验目录
```bash
cd 实验1~4
```

### 4. 按顺序完成实验
1. 先完成 `ai-lab-ch1/` 中的实验
2. 然后依次完成 `ai-lab-ch2/`、`ai-lab-ch3/`、`ai-lab-ch4/`
3. 每个实验都有详细的README说明


## ❌ 常见问题

### 安装问题
1. **Python安装失败**
   - 确保从官网下载
   - 安装时勾选"Add Python to PATH"
   - 重启命令行工具

2. **pip命令不存在**
   - **Windows**: 重新安装Python，确保勾选"Add Python to PATH"
   - **Mac**: 运行 `python3 -m ensurepip --upgrade`
   - **Linux**: 安装 `sudo apt-get install python3-pip`
   - 或尝试使用 `python -m pip` 代替 `pip`

3. **包安装失败**
   - 更新pip：`pip install --upgrade pip`
   - 使用国内镜像：`pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple`
   - 检查网络连接
   - 尝试使用 `python -m pip install 包名`

4. **权限问题**
   - Windows：以管理员身份运行命令行
   - Mac/Linux：使用sudo（谨慎使用）
   - 或使用用户安装：`pip install --user 包名`

### 运行问题
1. **文件路径错误**
   - 确保在正确的目录下运行命令
   - 使用 `dir`（Windows）或 `ls`（Mac/Linux）查看文件

2. **编码问题**
   - 确保文件保存为UTF-8编码
   - Windows设置：`chcp 65001`

3. **图形显示问题**
   - 安装matplotlib后端：`pip install tk`
   - 或使用在线环境如Google Colab

