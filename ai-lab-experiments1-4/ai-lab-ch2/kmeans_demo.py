# file: kmeans_demo.py
# 说明：
# 本脚本演示 KMeans 聚类的完整流程：
# 1) 智能数据加载：优先读取 data/kmeans.txt 或 kmeans.txt，如果文件不存在则自动生成80个二维数据点；
# 2) 训练 KMeans 聚类模型（4个簇）；3) 画出聚类散点图；
# 4) 可视化决策区域（不同簇的划分边界）；5) 对一个新点进行簇预测。
# 
# 数据来源说明：
# - 优先使用：data/kmeans.txt（如果存在）
# - 备选使用：kmeans.txt（如果存在）
# - 自动生成：如果上述文件都不存在，使用 make_blobs 生成80个样本，4个中心点，保存到 data/kmeans.txt

import os, numpy as np  # os: 文件与路径操作；numpy: 数组与数值计算
import matplotlib
matplotlib.use('Agg')  # 设置非交互式后端，用于保存图片
import matplotlib.pyplot as plt  # matplotlib: 绘图
from sklearn.cluster import KMeans  # KMeans 聚类算法
from sklearn.datasets import make_blobs  # 生成可控簇结构的模拟数据

# 1) 智能数据加载函数：按优先级读取或生成数据
def load_or_make():
    """
    数据加载策略（按优先级）：
    1. 优先读取：data/kmeans.txt（推荐位置）
    2. 备选读取：kmeans.txt（当前目录）
    3. 自动生成：如果都不存在，生成新数据并保存
    """
    path_a = "data/kmeans.txt"; path_b = "kmeans.txt"  # 两个候选路径：优先 data 目录
    if os.path.exists(path_a):
        print("📁 从 data/kmeans.txt 加载数据")
        return np.genfromtxt(path_a, delimiter=" ")  # 从文件读取空格分隔的二维数据
    if os.path.exists(path_b):
        print("📁 从 kmeans.txt 加载数据")
        return np.genfromtxt(path_b, delimiter=" ")  # 退而求其次，从当前目录读取
    # 若无文件，自动生成 80×2 的 4 簇数据
    print("🔧 未找到数据文件，正在自动生成...")
    # make_blobs 便于生成可控中心与方差的聚类数据；这里 80 个样本，4 个中心点，二维特征
    X, _ = make_blobs(n_samples=80, centers=4, n_features=2,
                      cluster_std=0.60, random_state=13)
    os.makedirs("data", exist_ok=True)  # 确保 data 目录存在
    np.savetxt("data/kmeans.txt", X, fmt="%.4f")  # 持久化保存，便于下次直接读取
    print("✅ 已自动生成 data/kmeans.txt（80个样本，4个簇）")
    return X

data = load_or_make()  # 加载（或生成）数据，shape 约为 (80, 2)

# 2) 训练 KMeans（4 类）
k = 4  # 预期的簇数量
km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(data)  # 训练模型；n_init 指不同初始中心的重启次数
centers = km.cluster_centers_  # 学到的簇中心坐标，shape: (k, 2)
labels  = km.predict(data)     # 每个样本的簇标签，整数 0..k-1

# 3) 散点簇图
colors = np.array(["#e41a1c","#377eb8","#4daf4a","#ff7f00"])  # 4 个簇的配色
plt.figure(figsize=(6,5))  # 新建画布
for i in range(k):
    # 绘制属于第 i 簇的样本点
    plt.scatter(data[labels==i,0], data[labels==i,1],
                s=25, alpha=0.85, c=colors[i], label=f"cluster {i}")
# 以星号标出簇中心
plt.scatter(centers[:,0], centers[:,1], s=180, marker="*",
            edgecolors="k", c=colors, label="centers")
plt.legend(); plt.title("KMeans Clusters (scatter)")  # 添加图例与标题
plt.tight_layout(); plt.savefig("kmeans_clusters.png", dpi=150, bbox_inches='tight')  # 保存图片
print("✅ 聚类散点图已保存为: kmeans_clusters.png")
plt.close()  # 关闭图形以释放内存

# 4) 决策区域（等高线式着色）
# 为绘图构建一个覆盖数据范围的网格，并对每个网格点预测其所属簇
x_min, x_max = data[:,0].min()-1, data[:,0].max()+1  # x 轴边界向外扩 1 个单位，便于显示
y_min, y_max = data[:,1].min()-1, data[:,1].max()+1  # y 轴边界向外扩 1 个单位
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))  # 生成网格采样点
Z = km.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)  # 预测每个网格点的簇并重塑回网格形状

plt.figure(figsize=(6,5))  # 新建画布用于决策区域
plt.contourf(xx, yy, Z, alpha=0.35, levels=k, colors=colors)  # 用不同颜色填充不同簇的区域
for i in range(k):
    # 在决策区域上再次叠加训练样本，便于对照
    plt.scatter(data[labels==i,0], data[labels==i,1],
                s=20, c=colors[i], edgecolors="k")
plt.scatter(centers[:,0], centers[:,1], s=180, marker="*",
            edgecolors="k", c=colors)  # 突出显示中心
plt.title("KMeans Decision Regions")
plt.tight_layout(); plt.savefig("kmeans_decision_regions.png", dpi=150, bbox_inches='tight')  # 保存图片
print("✅ 决策区域图已保存为: kmeans_decision_regions.png")
plt.close()  # 关闭图形以释放内存

# 5) 预测一个新点属于哪一簇（课堂互动）
new_pt = np.array([[0.0, 0.0]])  # 一个二维新样本（可修改数值尝试不同位置）
print("新样本", new_pt.tolist(), "-> 属于簇", int(km.predict(new_pt)[0]))
