import re

def my_function(x, y, z=1.5):
    if z > 1.0:
        return z * (x + y)
    else:
        return z / (x + y)

print(my_function(2, 3))
print(my_function(2, 3, 1))

a = None
def func_global_exam():
    global a
    a = [i ** 2 for i in range(1, 11)]
    print(a)
func_global_exam()
print(a)

def func_return_multiple_values(x):
    # 返回的是元组(x, x**2, x**3)
    return x, x**2, x**3
# 元组拆包
val, square, cube = func_return_multiple_values(3)
print(f"value={val}, square={square}, cube={cube}")   # value=3, square=9, cube=27

# 去除空格，移除标点符号，调整适当的大小写。
def clean_string(str):
    str = str.strip()
    str = re.sub("[!#?]", "", str)
    str = str.title()
    return str

strings = ["  Alabama  ", "Georgia! ", "Georgia", "georgia", "FlOrIda", "south     carolina##", "West virginia?  "]
print([clean_string(str) for str in strings])





# def定义函数，:结尾
def greet_user(username):
    """文档字符串(docstring)注释"""
    print(f"Hello {username.title()}!")

greet_user("remilia scarlet")

# 形参(parameter)&实参(argument)
# def $func($parameter):


def describe_pet(pet_name, animal_type="cat"):
    print(f"I hava a {animal_type}, it's name is {pet_name.title()}.")

# 位置实参
describe_pet("tom", "cat")                       # I hava a cat, it's name is Tom.
# 关键字实参，指定形参名，顺序无关紧要
describe_pet(animal_type="cat", pet_name="tom")  # I hava a cat, it's name is Tom.
describe_pet(pet_name="tom", animal_type="cat")  # I hava a cat, it's name is Tom.
# 形参默认值
describe_pet("tom")  # I hava a cat, it's name is Tom.
describe_pet("harry", "dog")  # I hava a dog, it's name is Harry.

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name("remilia", "sCarLet"))