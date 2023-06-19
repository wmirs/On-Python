import numpy as np

# dim_1_list = np.arange(0, 11)
# print(dim_1_list)
# print(dim_1_list[5:8])
# dim_1_list[5:8] = [15, 16, 17]
# print(dim_1_list)
# dim_1_list_slice = dim_1_list[5:8]
# print(dim_1_list_slice)
# dim_1_list_slice[:] = [25, 26, 27]
# print(dim_1_list)
# dim_1_list_slice_copy = dim_1_list[5:8].copy()
# dim_1_list_slice_copy[:] = [35, 36, 37]
# print(dim_1_list)

"""
将0轴看作“行”，将1轴看作“列”
"""
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(len(arr2d))
print(arr2d[2])
print(arr2d[2][2])
print(arr2d[2, 2])