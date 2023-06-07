""" 散点图 scatter()
"""
import matplotlib.pyplot as plt
# 使用内置样式
plt.style.use("seaborn-v0_8-darkgrid")
# 设置中文字体
plt.rcParams["font.family"]=["serif"]


fig, ax = plt.subplots()
ax.scatter(2, 4)

# 标题
ax.set_title("Squares", fontsize=14)
# x, y轴标签
ax.set_xlabel("值", fontsize=10)
ax.set_ylabel("值的平方", fontsize=10)
# 刻度标记的大小
ax.tick_params(axis="both", labelsize=8)

plt.show()