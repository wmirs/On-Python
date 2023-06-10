# 元组：固定长度、不可变的Python对象序列
tuple1 = 3, 4, 5
tuple2 = (1, 2), (3, 4)
print(f"{tuple1}")  # Tuple: (3, 4, 5)
print(f"{tuple2}")  # ((1, 2), (3, 4))
# tuple()函数
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(tuple("Hello World"))  # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
# [$index]
tuple3 = (1, 2, 3, 4, 5, 6)
print(f"index_0={tuple3[0]}, index_3={tuple3[3]}, index_-1={tuple3[-1]}") # index_0=1, index_3=4, index_-1=6
# +, * 运算符
tuple4_1, tuple4_2 = (1, 2, 3), (4, 5, 6)
print(tuple4_1 + tuple4_2)   # (1, 2, 3, 4, 5, 6)
print(tuple4_1 * 3)          # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# count()方法
print((1, 2, 2, 3, 2, 4).count(2))  # 3
print(((1, 2), (3, 4), (1, 2), (2, 1), (5, 6)).count((1, 2))) # 2

# 拆包：将元组型的表达式赋值给变量，Python会对等号右边的值进行拆包。
# 变量交换
a, b = 1, 2
print(f"a={a}, b={b}")  # a=1, b=2
b, a = a, b
print(f"a={a}, b={b}")  # a=2, b=1
# 遍历元组或列表组成的序列
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
"""
1, 2, 3
4, 5, 6
7, 8, 9
"""
for a, b, c in seq:
    print(f"{a}, {b}, {c}")
# *rest语法
x1, y1, z1, *rest = (11, 12, 13, 14, 15, 16)
print(f"x={x1}, y={y1}, z={z1}, rest={rest}")  # x=11, y=12, z=13, rest=[14, 15, 16]
x2, y2, z2, *_ = (1, 2, 3, 4, 5, 6)
print(f"x={x2}, y={y2}, z={z2}")               # x=1, y=2, z=3
