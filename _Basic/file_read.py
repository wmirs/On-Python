"""files/pi_digits.txt
3.1415926535
  8979323846
  2643383279
"""
file_full_path = "/Users/bytedance/Repositories/On-Python/_Basic/files/pi_digits.txt"
# with在不再需要访问文件后将其关闭，也可以通过close()方法进行关闭
# open()函数接受一个参数，需要打开的文件名，返回一个表示文件的对象
# open()函数的参数是路径
with open(file_full_path) as pi_file_obj:
# with open("files/pi_digits.txt") as pi_file_obj:
    contents = pi_file_obj.read()
print(f"\"\n{contents}\n\"")
print()

with open(file_full_path) as pi_file_obj:
    for line in pi_file_obj:
        print(f"\"{line}\"\n")

# readlines()方法，从文件中读取每一行，并将其存储在一个列表中。
with open(file_full_path) as pi_file_obj:
    lines = pi_file_obj.readlines()
print(lines)

# +运算符，拼接字符串
# len()函数返回字符串长度
pi_string = ""
with open(file_full_path) as pi_file_obj:
    for line in pi_file_obj:
        pi_string += line.strip()
print(f"PI: {pi_string}, length: {len(pi_string)}")

# 大文件
PI_MILLION_FULL_PATH = "/Users/bytedance/Repositories/On-Python/_Basic/files/pi_million_digits.txt"
lines = []
with open(PI_MILLION_FULL_PATH) as fileObj:
    lines = fileObj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"PI: {pi_string[:54]}..., length: {len(pi_string)}")

birthday = input("Please enter your birthday, format is 'mmddyy', eg'050796': ")
print(f"Your birthday is {birthday}, is in PI?{birthday in pi_string}")