# 实验2：机器学习基础

## 📋 实验目标
- 学习线性回归算法
- 理解K-means聚类算法
- 掌握数据预处理和模型评估
- 学会使用scikit-learn库

## 🎯 实验内容
1. **线性回归**：使用 `avgscore.py` 学习平均分预测
2. **K-means聚类**：使用 `kmeans_demo.py` 进行数据聚类分析

## 📦 需要安装的包
在运行实验前，需要安装以下Python包：

### 安装方法（选择其中一种）

#### 方法1：使用pip逐个安装（推荐）
```bash
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install joblib
```

#### 方法2：一次性安装所有包
```bash
pip install numpy pandas scikit-learn matplotlib joblib
```

### 验证安装
安装完成后，可以运行以下命令验证：
```python
python -c "import numpy, pandas, sklearn, matplotlib, joblib; print('所有包安装成功！')"
```

## 🚀 运行步骤

### 实验2.1：线性回归（平均分预测）

1. 打开VS Code，并确保左侧资源管理器定位到 `实验1~4/ai-lab-ch2` 目录。

2. 在菜单栏选择“终端” -> “新终端”，或使用快捷键 ``Ctrl + ` `` 打开内置终端。

3. （如未在正确目录，可在终端中输入）
    ```bash
    cd 实验1~4/ai-lab-ch2
    ```

4. 在VS Code终端输入以下命令运行线性回归程序：
    ```bash
    python avgscore.py
    ```

3. 观察输出结果，理解：
   - 数据生成过程
   - 训练/测试集划分
   - 模型评估指标（MAE、R²）
   - 预测结果
   - 学习到的权重系数

### 实验2.2：K-means聚类

1. 运行聚类程序：
   ```bash
   python kmeans_demo.py
   ```

2. 程序会自动：
   - 生成或加载聚类数据
   - 训练K-means模型
   - 显示聚类结果图
   - 展示决策区域
   - 预测新样本的类别

## ✅ 预期结果

### avgscore.py 输出示例：
```
MAE = 0.000123456789
R2  = 0.999999999
分数 58,74,53 -> 预测平均分 = 61.666666666666664
分数 80,90,100 -> 预测平均分 = 90.0
Learned weights: [0.33333333 0.33333333 0.33333333] intercept: 0.0
已保存 -> avgscore_lr.joblib
```

### kmeans_demo.py 输出示例：
```
未找到 kmeans.txt，已自动生成 data/kmeans.txt
新样本 [[0.0, 0.0]] -> 属于簇 2
```
同时会显示两个图形窗口：
- 聚类散点图
- 决策区域图

## ❌ 常见问题

### 问题1：pip命令不存在
**错误信息**：`pip: command not found` 或 `'pip' 不是内部或外部命令`
**解决方案**：
```bash
# 方法1：使用python -m pip
python -m pip install numpy matplotlib

# 方法2：检查pip是否安装
python -m ensurepip --upgrade

# 方法3：重新安装pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# 方法4：使用国内镜像源
python -m pip install numpy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题2：ModuleNotFoundError
**错误信息**：`ModuleNotFoundError: No module named 'numpy'`
**解决方案**：
```bash
# 使用默认源
pip install numpy matplotlib

# 使用国内镜像源（推荐，速度更快）
pip install numpy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用其他镜像源
pip install numpy matplotlib -i https://mirrors.aliyun.com/pypi/simple/
pip install numpy matplotlib -i https://pypi.douban.com/simple/
```

### 问题3：matplotlib显示问题
**错误信息**：图形不显示或报错
**解决方案**：
- **Windows**: 安装tkinter：`pip install tk`
- **Mac**: 可能需要安装：`brew install python-tk`
- **Linux**: 安装：`sudo apt-get install python3-tk`

### 问题4：数据文件问题
**解决方案**：
- 程序会自动生成 `kmeans.txt` 文件
- 如果生成失败，检查当前目录的写入权限

### 问题5：图形窗口关闭
**解决方案**：
- 程序运行时会弹出图形窗口
- 关闭图形窗口后程序会继续运行
- 如果图形不显示，检查matplotlib后端设置

## 📚 学习要点

### 线性回归
- 监督学习概念
- 训练/测试集划分
- 模型评估指标
- 特征工程
- 模型保存和加载

### K-means聚类
- 无监督学习概念
- 聚类算法原理
- 数据可视化
- 决策边界
- 新样本预测

## 🔧 进阶实验

### 修改参数实验
1. **修改数据量**：将500改为1000，观察结果变化
2. **修改聚类数**：将k=4改为k=3或k=5
3. **修改随机种子**：观察结果的可重现性

### 添加新功能
1. 保存聚类结果图
2. 计算聚类评估指标
3. 尝试不同的聚类算法

