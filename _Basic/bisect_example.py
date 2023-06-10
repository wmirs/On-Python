import bisect

sorted_nums = [1, 2, 2, 3, 3, 4, 4, 4, 4, 12, 18]
# bisect()
print(bisect.bisect(sorted_nums, 3))
print(bisect.bisect(sorted_nums, 5))
# insort()
bisect.insort(sorted_nums, 5)
print(sorted_nums)
bisect.insort(sorted_nums, 2)
print(sorted_nums)
