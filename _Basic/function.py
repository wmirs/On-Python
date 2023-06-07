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