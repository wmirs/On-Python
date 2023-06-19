import numpy as np

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
# 生成一些随机正态分布的数据
data = np.random.randn(7, 4)

print(names)
print(data)

print(names == "Bob")
print(data[names == "Bob"])