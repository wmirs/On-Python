"""
conda install matpoltlib
"""
import matplotlib.pyplot as plt
# 使用内置样式
plt.style.use("seaborn-v0_8-darkgrid")
# 设置字体
plt.rcParams["font.family"]=["Microsoft YaHei"]
# "-"负号的乱码问题
# plt.rcParams["axes.unicode_minus"]=False

nums = list(range(1, 6))
squares = [v ** 2 for v in range(1, 6)]

# fig整张图片，ax表示图片中的各个图表
fig, ax = plt.subplots()
# 线条的粗细
ax.plot(nums, squares, linewidth=3)
# 标题
ax.set_title("平方数", fontsize=14)
# x, y轴标签
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值的平方", fontsize=10)
# 刻度标记的大小
ax.tick_params(axis="both", labelsize=8)


# 打开Matplotlib查看器并显示绘制的图表
plt.show()