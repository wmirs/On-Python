list1 = [2, 3, 7, None]
print(list1)
# list()
list2 = list(tuple("Hello World"))
print(list2)
# list(range())
list3 = list(range(1, 11))
print(list3)
# append()
list4 = ["remilia", "flandre"]
list4.append("cirno")
list4.append("sakuya")
print(list4)
# insert()
list4.insert(1, "wangmu")
print(list4)
# pop()
list4.pop()
print(list4)
list4.pop(1)
print(list4)
# remove()
list4.append("remilia")
print(list4)
list4.remove("remilia")
print(list4)
# del语句
del list4[1]
print(list4)
# in / not in
list5 = ["remilia", "flandre", "cirno", "sakura"]
print("Remilia" in list5)
print("remilia" in list5)
print("Remilia" not in list5)
print("remilia" not in list5)

# +运算符
list6_1 = ["1m", "2m", "5m", "10m"]
list6_2 = ["10s", "30s"]
list6_3 = ["20m", "30m", "60m", "90m"]
print(list6_2 + list6_1 + list6_3) 
# extend()方法
list6_1.extend(list6_3)
list6_1.extend(list6_2)
print(list6_1)
# *运算符
print(list6_1 * 3)

# sort()方法
names = ["Remilia", "Flandre", "Cirno", "Sakura"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.sort(key=len)
print(names)
names.sort(key=len, reverse=True)
print(names)


# 切片
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])
# 替换序列中某些数据
# seq[3:6] = [6, 3, 2, 1, 0]
# 列表反转
print(seq)          # [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[::-1])    # [1, 0, 6, 5, 7, 3, 2, 7]
