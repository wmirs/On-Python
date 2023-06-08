# 元组：固定长度、不可变的Python序列。用逗号分割序列值
tuple1 = 3, 4, 5                              # 元组: (3, 4, 5), 长度: 3
print(f"元组: {tuple1}, 长度: {len(tuple1)}")
# 用圆括号括起来，创建较为复杂的元组表达式
tuple2 = (1, 2, 3), (4, 5, 6)                 # 元组: ((1, 2, 3), (4, 5, 6)), 长度: 2
print(f"元组: {tuple2}, 长度: {len(tuple2)}")
# tuple()函数将任意序列或迭代器转换为元组
tuple3 = tuple([1, 2, 3])
tuple4 = tuple("hello")
print(f"元组: {tuple3}, 长度: {len(tuple3)}")   # 元组: (1, 2, 3), 长度: 3
print(f"元组: {tuple4}, 长度: {len(tuple4)}")   # 元组: ('h', 'e', 'l', 'l', 'o'), 长度: 5
# 通过"[$index]"可以获取元组中对应索引位置的元素
print(tuple3[-1])  # 3
print(tuple4[1])   # e
# "+"运算符可以将元组拼接成更长的元组
tuple5 = tuple3 + tuple4
print(f"元组: {tuple5}, 长度: {len(tuple5)}")   # 元组: (1, 2, 3, 'h', 'e', 'l', 'l', 'o'), 长度: 8
# "*"运算符生成含有多份拷贝的元组
tuple6 = tuple4 * 3
print(f"元组: {tuple4}, 长度: {len(tuple4)}")   # 元组: ('h', 'e', 'l', 'l', 'o'), 长度: 5
print(f"元组: {tuple6}, 长度: {len(tuple6)}")   # 元组: ('h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o'), 长度: 15

# 元组拆包
tuple7 = (1, 2, 3)
a, b, c = tuple7
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3
tuple8 = (1, 2, (3, 4))
h, i, (j, k) = tuple8
print(f"h={h}, i={i}, j={j}, k={k}")
# 交换变量名
a, b = 1, 2
print(f"a={a},b={b}")
