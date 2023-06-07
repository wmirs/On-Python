""" 散点图 scatter()
"""
import matplotlib.pyplot as plt
# 使用内置样式
plt.style.use("seaborn-v0_8-darkgrid")
# 设置中文字体
plt.rcParams["font.family"]=["Microsoft YaHei"]


x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

fig, ax = plt.subplots()
# 将数据点的轮廓删除
ax.scatter(x_values, y_values, s=10, edgecolor="none", c=(0, 0, 0.8))

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 标题
ax.set_title("Squares", fontsize=14)
# x, y轴标签
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值的平方", fontsize=10)
# 刻度标记的大小
ax.tick_params(axis="both", labelsize=8)

plt.show()