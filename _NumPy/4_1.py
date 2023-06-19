"""
**向量化**
1. 任何在两个等尺寸数组之间的算术操作都应用了逐元素操作的方式
2. 带有标量计算的算术操作，会把计算参数传递给数组的每一个元素
3. 同尺寸数组之间的比较，会产生一个布尔值数组
4. 不同尺寸的数组间的操作，将会用到广播特性
5. 如果你还是想要一份数组切片的拷贝而不是一份视图的话, 你就必须显式地复制这个数组, 例如arr[5:8].copy()
"""
import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr / arr)

print(2 + arr)
print(2 - arr)
print(2 * arr)
print(2 / arr)

arr2 = np.array([[3., 2., 1.], [6., 5., 4.]])
print(arr > arr2)
print(arr == arr2)
print(arr < arr2)

dim_1_list = np.arange(0, 11)
print(dim_1_list)
print(dim_1_list[5:8])
dim_1_list[5:8] = [15, 16, 17]
print(dim_1_list)
dim_1_list_slice = dim_1_list[5:8]
print(dim_1_list_slice)
dim_1_list_slice[:] = [25, 26, 27]
print(dim_1_list)
dim_1_list_slice_copy = dim_1_list[5:8].copy()
dim_1_list_slice_copy[:] = [35, 36, 37]
print(dim_1_list)