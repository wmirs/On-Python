current_number = 1
while current_number <= 5:            # 1, 2, 3, 4, 5, 
    print(current_number, end=", ")
    current_number += 1
print()

prompt = "Tell me something, I will repeat it back to you. Enter 'quit' to end the program: "
message = input(prompt)
while message != "quit":
    print(message)
    message = input(prompt)

# break 退出循环
prompt = "Please enter the name of a city you have visited: (Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city.lower() == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}")

# continue 跳过循环, 获取[1, 10]的所有奇数
odd_nums = []
curr_num = 0
while curr_num < 10:
    curr_num += 1
    if curr_num % 2 == 0:
        continue
    odd_nums.append(curr_num)
print(odd_nums)    # [1, 3, 5, 7, 9]

# for 循环是一种遍历列表的有效方式，但不应在 for 循环中修改列表，否则将导致 Python 难 以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用 while 循环。
unconfirmed_users = ["remilia", "flandre", "cirno"]
confirmed_users = []
print(f"Unconfirmed users: {unconfirmed_users}")      # Unconfirmed users: ['remilia', 'flandre', 'cirno']
print(f"Confirmed users: {confirmed_users}")          # Confirmed users: []
"""
Verifying user: Cirno
Verifying user: Flandre
Verifying user: Remilia
"""
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print(f"Unconfirmed users: {unconfirmed_users}")      # Unconfirmed users: []
print(f"Confirmed users: {confirmed_users}")          # Confirmed users: ['cirno', 'flandre', 'remilia']

# 循环删除列表中特定元素
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)   # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while "cat" in pets:
    pets.remove("cat")
print(pets)   # ['dog', 'dog', 'goldfish', 'rabbit']
