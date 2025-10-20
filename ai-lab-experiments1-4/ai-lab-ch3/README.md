# 实验3：深度学习入门

## 📋 实验目标
- 学习PyTorch深度学习框架
- 理解神经网络基本原理
- 掌握MNIST手写数字识别
- 学会模型训练和评估

## 🎯 实验内容
1. **环境检查**：使用 `check_torch.py` 检查PyTorch安装
2. **手写数字识别**：使用 `torch_mnist.py` 训练神经网络

## 📦 环境要求

### Python版本
- **Python 3.7+** （推荐Python 3.8或3.9）
- 检查版本：`python --version`

### 需要安装的包

### 安装PyTorch（重要！）
PyTorch安装比较复杂，请根据你的系统选择正确的安装命令：

#### 方法1：访问PyTorch官网查看下载命令
1. 打开浏览器，访问：https://pytorch.org/get-started/locally/
2. 选择你的配置：
   - **OS**: Windows/Mac/Linux
   - **Package**: Pip
   - **Language**: Python
   - **Compute Platform**: CPU（如果没有GPU）
3. 复制生成的安装命令并运行

#### 方法2：使用CPU版本（适合初学者）
```bash
# Windows/Linux
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Mac
pip install torch torchvision torchaudio
```

#### 方法2.1：CPU版本，使用国内镜像源（推荐，速度更快）
```bash
# 方法A：清华镜像 + PyTorch官方CPU源（推荐）
pip install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple --extra-index-url https://download.pytorch.org/whl/cpu

# 方法B：阿里镜像 + PyTorch官方CPU源
pip install torch torchvision torchaudio -i https://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://download.pytorch.org/whl/cpu

# 方法C：豆瓣镜像 + PyTorch官方CPU源
pip install torch torchvision torchaudio -i https://pypi.douban.com/simple/ --extra-index-url https://download.pytorch.org/whl/cpu

# 方法D：中科大镜像 + PyTorch官方CPU源
pip install torch torchvision torchaudio -i https://pypi.mirrors.ustc.edu.cn/simple/ --extra-index-url https://download.pytorch.org/whl/cpu
```

**注意**：PyTorch需要从官方源下载，国内镜像源只提供其他依赖包，所以需要同时指定两个源。如果上述方法失败，请直接使用方法2的官方源。

#### 方法2.2：简化安装（如果上述方法都失败）
```bash
# 直接使用官方源（最稳定）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 或者分步安装
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install torchvision
pip install torchaudio
```

#### 方法3：如果有NVIDIA GPU（想使用GPU来运行可以下载这个库， 但本实验CPU运行也足够了）
```bash
# 需要先安装CUDA，然后使用GPU版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 安装其他依赖包
```bash
# 使用默认源
pip install matplotlib

# 或使用国内镜像源（推荐）
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**注意**：`torchaudio` 在这个实验中不是必需的，但建议一起安装以保持PyTorch生态的完整性。

## 📁 文件结构
```
ai-lab-ch3/
├── check_torch.py      # PyTorch环境检查脚本
├── torch_mnist.py      # MNIST手写数字识别主程序
├── download_mnist.py   # MNIST数据集下载脚本（网络慢时使用）
├── README.md           # 本说明文件
└── data/               # MNIST数据集存储目录（自动创建）
```

## 🚀 运行步骤

### 实验3.1：检查PyTorch环境

1. 进入实验目录：
   ```bash
   cd 实验1~4/ai-lab-ch3
   ```

2. 运行环境检查程序：
   ```bash
   python check_torch.py
   ```

3. 查看输出结果，确认PyTorch安装成功

### 实验3.2：MNIST手写数字识别

1. **运行深度学习程序**：
   ```bash
   python torch_mnist.py
   ```

2. **如果下载失败**，使用下载脚本：
   ```bash
   python download_mnist.py
   python torch_mnist.py
   ```

3. 程序会自动：
   - 下载MNIST数据集（约60MB）
   - 构建神经网络模型
   - 训练模型（1个epoch）
   - 在测试集上评估
   - 保存预测结果图像到 `mnist_predictions.png`

## ✅ 预期结果

### check_torch.py 输出示例：
```
torch 2.0.1 torchvision 0.15.2
cuda_available: False
```
*注意：cuda_available为False是正常的，表示使用CPU运行*

### torch_mnist.py 输出示例：
```
Train acc=0.923, Test acc=0.925
```
同时会显示一个包含6张手写数字图像的窗口，每张图像上方显示预测的数字。

**注意**：由于只训练1个epoch，实际准确率可能在85%-95%之间波动，这是正常的。

## ❌ 常见问题

### 问题1：PyTorch安装失败
**错误信息**：`ERROR: Could not find a version that satisfies the requirement torch`
**解决方案**：
1. 更新pip：`pip install --upgrade pip`
2. 使用国内镜像源（按优先级尝试）：
   ```bash
   # 清华镜像 + PyTorch官方CPU源
   pip install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple --extra-index-url https://download.pytorch.org/whl/cpu
   
   # 阿里镜像 + PyTorch官方CPU源
   pip install torch torchvision torchaudio -i https://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://download.pytorch.org/whl/cpu
   
   # 豆瓣镜像 + PyTorch官方CPU源
   pip install torch torchvision torchaudio -i https://pypi.douban.com/simple/ --extra-index-url https://download.pytorch.org/whl/cpu
   
   # 中科大镜像 + PyTorch官方CPU源
   pip install torch torchvision torchaudio -i https://pypi.mirrors.ustc.edu.cn/simple/ --extra-index-url https://download.pytorch.org/whl/cpu
   ```
3. 如果还是失败，尝试conda安装：`conda install pytorch torchvision -c pytorch`
4. 检查Python版本：确保使用Python 3.7+
5. 尝试指定版本：`pip install torch==2.0.1 torchvision==0.15.2`
6. 增加超时时间：`pip install torch torchvision torchaudio --timeout 1000`

### 问题2：下载MNIST数据集失败
**错误信息**：`ConnectionResetError: [Errno 104] Connection reset by peer` 或 `HTTP Error 404: Not Found` 或网络超时
**解决方案**：

#### 方案1：重新运行程序（推荐）
```bash
# 部分文件可能已下载成功，重新运行可能完成下载
python torch_mnist.py
```

#### 方案2：清理后重新下载
```bash
# 删除不完整的数据，重新下载
rm -rf data/
python torch_mnist.py
```

#### 方案3：手动下载数据集（网络慢时推荐）
1. **创建目录**：
   ```bash
   mkdir -p data/MNIST/raw
   ```

2. **下载文件**（使用浏览器或下载工具）：
   - 训练图像：https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
   - 训练标签：https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
   - 测试图像：https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
   - 测试标签：https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz

3. **解压文件**：
   ```bash
   cd data/MNIST/raw/
   gunzip *.gz
   ```

4. **运行程序**：
   ```bash
   python torch_mnist.py
   ```

#### 方案4：使用下载脚本（推荐）
使用提供的下载脚本，支持多个镜像源：
```bash
python download_mnist.py
```

**脚本特点**：
- ✅ 自动尝试多个镜像源
- ✅ 显示下载进度
- ✅ 自动解压文件
- ✅ 跳过已存在的文件
- ✅ 错误处理和重试机制

#### 方案5：网络优化设置
```bash
# 增加超时时间
export PYTHONUNBUFFERED=1
python torch_mnist.py
```

#### 方案6：使用代理或VPN
如果网络访问受限，可以：
1. 使用VPN连接
2. 配置代理服务器
3. 使用手机热点等更稳定的网络

### 问题3：内存不足
**错误信息**：`RuntimeError: CUDA out of memory` 或内存相关错误
**解决方案**：
1. 程序会自动使用CPU，这是正常的
2. 如果CPU内存不足，可以减小batch_size
3. 关闭其他占用内存的程序

### 问题4：图形显示问题
**错误信息**：图形窗口不显示或显示异常
**解决方案**：
- 确保matplotlib正确安装：`pip install matplotlib`
- 在Windows上可能需要安装tkinter：`pip install tk`
- 在Linux服务器上可能需要设置显示：`export DISPLAY=:0`
- 如果图形不显示，程序仍会正常运行并输出准确率
- 可以尝试修改后端：在代码开头添加 `import matplotlib; matplotlib.use('Agg')`

### 问题5：运行速度慢
**说明**：
- 第一次运行会下载数据集，需要等待
- CPU训练比GPU慢，这是正常的
- 程序只训练1个epoch，所以不会太慢


## 🔧 进阶实验

### 修改网络结构
尝试修改 `torch_mnist.py` 中的网络结构：
```python
# 原始结构：784 -> 256 -> 128 -> 10
# 可以尝试：784 -> 512 -> 256 -> 128 -> 10
```

### 调整超参数
1. **学习率**：修改 `lr=1e-3` 为其他值
2. **批量大小**：修改 `batch_size=64`
3. **训练轮数**：增加epoch数量

### 添加更多功能
1. 保存训练好的模型
2. 绘制训练曲线
3. 测试自己的手写数字

## 💡 实验提示

1. **第一次运行**：需要下载MNIST数据集（约60MB），请耐心等待
2. **准确率**：CPU训练1个epoch通常能达到85%-95%的准确率
3. **可视化**：程序会显示6张测试图像的预测结果
4. **GPU加速**：如果有NVIDIA GPU，可以安装CUDA版本的PyTorch
5. **数据存储**：MNIST数据集会保存在 `data/` 目录下，下次运行无需重新下载
6. **模型简单**：这是一个基础的多层感知机，适合学习深度学习概念

## 🔍 代码理解要点

### 关键概念解释
- **张量（Tensor）**：PyTorch中的多维数组，类似于numpy数组但支持GPU加速
- **自动求导**：PyTorch自动计算梯度，无需手动实现反向传播
- **DataLoader**：批量加载数据，提高训练效率
- **交叉熵损失**：多分类问题的标准损失函数
- **Adam优化器**：自适应学习率的优化算法

