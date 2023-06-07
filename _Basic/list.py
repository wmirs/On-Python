print(range(0, 6))              # range(0, 6)
print(list(range(0, 6)))        # [0, 1, 2, 3, 4, 5]
print(list(range(0, 6, 2)))     # [0, 2, 4]
digits = list(range(6))
# [0, 1, 2, 3, 4, 5] ==> min=0, max=5, sum=15
print(f"{digits} ==> min={min(digits)}, max={max(digits)}, sum={sum(digits)}")


squares_1 = []
for v in range(11):
    squares_1.append(v ** 2)
# 列表解析
squares_2 = [v ** 2 for v in range(11)]
print(squares_1)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares_2)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]