# file: avgscore.py
# 说明：
# 本脚本演示如何用线性回归学习“平均分”的计算。
# 流程包含：造数据 -> 计算真实平均分 -> 划分数据集 -> 训练 -> 评估 -> 预测 -> 查看参数 -> 保存模型。

import numpy as np, pandas as pd  # numpy: 数值计算；pandas: 表格数据处理
from sklearn.model_selection import train_test_split  # 划分训练/测试集的便捷函数
from sklearn.linear_model import LinearRegression      # 线性回归模型
from sklearn.metrics import mean_absolute_error, r2_score  # 回归常用评估指标：MAE 与 R²
import joblib  # 模型的持久化保存与加载
import matplotlib
matplotlib.use('Agg')  # 设置非交互式后端，用于保存图片
import matplotlib.pyplot as plt  # 绘图库

# 1) 造数据：500 行三科成绩（每科 50~100 分的整数）
rng = np.random.default_rng(100)  # 固定随机种子，保证每次运行的数据一致（可复现实验）
scores = rng.integers(50, 101, size=(500, 3))  # 生成形状为 (500,3) 的整数数组，范围 [50,101)
df = pd.DataFrame(scores, columns=["语文", "数学", "英文"])  # 构建数据表，三列分别代表三科成绩

# 2) 计算“真”平均分，作为监督学习的 y（标签）
# DataFrame.mean(axis=1) 表示按行求均值；得到每个学生三科成绩的平均值
df["平均分"] = df[["语文","数学","英文"]].mean(axis=1)

# 3) 划分训练/测试（7:3）
# X 为特征矩阵（语文、数学、英文三列），y 为目标向量（平均分）
X = df[["语文","数学","英文"]].values  # shape: (500, 3)
y = df["平均分"].values                    # shape: (500,)
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=0
)  # test_size=0.3 表示 30% 作为测试集；random_state 固定划分

# 4) 训练线性回归
# 对于线性可加的目标（如平均分），线性回归应能学到接近 1/3 的权重与很小的截距
lr = LinearRegression().fit(X_tr, y_tr)

# 5) 评估（回归经典指标）
y_pred = lr.predict(X_te)  # 在测试集上做预测
print("MAE =", mean_absolute_error(y_te, y_pred))   # 平均绝对误差，越小越好，理想情况下接近 0
print("R2  =", r2_score(y_te, y_pred))               # 决定系数 R²，越接近 1 越好

# 6) 用两组样本试预测（给出三科成绩，预测平均分）
print("分数 58,74,53 -> 预测平均分 =", lr.predict([[58,74,53]])[0])
print("分数 80,90,100 -> 预测平均分 =", lr.predict([[80,90,100]])[0])

# 7) 看学到的“公式系数”（理论上应≈ 1/3, 1/3, 1/3；截距≈ 0）
print("Learned weights:", lr.coef_, "intercept:", lr.intercept_)

# 8) 可视化：真实值 vs 预测值散点图
plt.figure(figsize=(8, 6))
plt.scatter(y_te, y_pred, alpha=0.6, s=30, c='blue', edgecolors='black', linewidth=0.5)
# 绘制完美预测线（y=x）
min_val = min(y_te.min(), y_pred.min())
max_val = max(y_te.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction Line (y=x)')
plt.xlabel('True Average Score', fontsize=12)
plt.ylabel('Predicted Average Score', fontsize=12)
plt.title(f'Linear Regression Prediction Results\nMAE = {mean_absolute_error(y_te, y_pred):.6f}, R² = {r2_score(y_te, y_pred):.6f}', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("avgscore_prediction.png", dpi=150, bbox_inches='tight')
print("✅ 预测效果图已保存为: avgscore_prediction.png")
plt.close()

# 9) 保存模型，后续可直接加载复用
# joblib.dump 会在当前工作目录生成文件，可用 joblib.load 重新加载
joblib.dump(lr, "avgscore_lr.joblib")
print("已保存 -> avgscore_lr.joblib")
