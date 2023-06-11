set_1 = {1, 2, 2, 1, 3, 5, 3, 4}
set_2 = set("HelloWorld")
print(f"set_1 = {set_1}, set_2 = {set_2}")

set_a = set(range(1, 6))
set_b = set(range(3, 9))
print(f"Set a={set_a}, b={set_b}")
# 并集
print(f"Union: {set_a.union(set_b)}")
print(f"Union: {set_a | set_b}")
# 交集
print(f"Intersection: {set_a.intersection(set_b)}")
print(f"Intersection: {set_a & set_b}")
# 差集
print(f"difference: {set_a.difference(set_b)}")
print(f"difference: {set_a - set_b}")
print(f"symmetric_difference: {set_a.symmetric_difference(set_b)}")
print(f"symmetric_difference: {set_a ^ set_b}")
print(f"{(set_a | set_b) - (set_a & set_b)}")

print({1, 2, 3}.issubset({1, 2, 3, 4, 5}))
print({1, 2, 3}.issuperset({1, 2, 3, 4, 5}))
print({1, 2, 3, 4, 5}.issubset({1, 2, 3}))
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))





set_x = {1, 2, 3, 4, 5}
print(set_x)
set_x.add(5)
print(set_x)
set_x.add(7)
print(set_x)
# set_x.remove(10)
# print(set_x)
set_x.remove(5)
print(set_x)
set_x.pop()
print(set_x)
set_x.clear()
print(set_x)
# set_x.pop()
print(set_x)