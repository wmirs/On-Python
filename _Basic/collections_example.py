import collections

queue = collections.deque()
queue.append(1)
queue.insert(0, 2)
print(queue)

dict_0 = collections.defaultdict(list)
dict_0[1].append("remilia")
print(dict_0)