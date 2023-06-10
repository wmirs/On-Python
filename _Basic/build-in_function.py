# enumerate()函数
msg = "Hello World"
for index, value in enumerate(msg):
    endStr = "\n"
    if index != len(msg) - 1:
        endStr = "; "
    print(f"{index}:{value}", end=endStr)

seq = [1, 2, 2, 3, 3, 3, 4, 5, 6, 8, 8, 10]
for index, value in enumerate(seq):
    endStr = "\n"
    if index != len(seq) - 1:
        endStr = "; "
    print(f"{index}:{value}", end=endStr)

# sorted()函数
print(sorted(msg))
print(msg)
print(sorted(seq, reverse=True))
print(seq)

# zip()函数
seq1 = ["Remilia", "Flandre", "Cirno"]
seq2 = ["Scarlet", "Scarlet", "Sakura"]
print(list(zip(seq1, seq2)))
seq3 = [True, False]
print(list(zip(seq1, seq2, seq3)))
for i, tup in enumerate(zip(seq1, seq2)):
    endStr = "\n"
    if i != len(list(zip(seq1, seq2))) - 1:
        endStr = "; "
    print(f"{i}: {tup}", end=endStr)
# 行转列, 列转行
row1 = (1, 2, 3)
row2 = (4, 5, 6)
cols = list(zip(row1, row2))
"""
(1, 4)
(2, 5)
(3, 6)
"""
for col in cols:
    print(col)
row3, row4 = zip(*cols)
"""
(1, 2, 3)
(4, 5, 6)
"""
print(f"{row3}\n{row4}")

# reversed()函数
print(range(10))
print(reversed(range(10)))
print(list(reversed(range(10))))

# hash()函数
print(hash(123))
print(hash(123.0))
print(hash("123"))
print(hash((1, 2, 3)))
# 不可哈希化
# print(hash(list(1, 2, 3)))