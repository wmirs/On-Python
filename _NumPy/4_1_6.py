import numpy as np

arr2d = np.empty((8, 4))

for i in range(8):
    arr2d[i] = i ** 2
print(arr2d)
print(arr2d[[2, 4, 0, 6]])


arr2d_2 = np.arange(32).reshape(8, 4)
print(arr2d_2)
# [4, 23, 29, 10]
print(arr2d_2[[1, 5, 7, 2], [0, 3, 1, 2]])

print(arr2d_2[[1, 5, 7, 2]])
arr2d_2_0 = arr2d_2[[1, 5, 7, 2]]
"""
[[ 4  5  6  7]
 [20 21 22 23]
 [28 29 30 31]
 [ 8  9 10 11]]
"""
print(arr2d_2_0)
"""
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
"""
print(arr2d_2_0[:])
"""
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
"""
print(arr2d_2[[1, 5, 7, 2]][:, [0, 3, 1, 2]])