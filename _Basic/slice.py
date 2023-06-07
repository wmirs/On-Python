names = ["Remilia", "Flandre", "Cirno", "Sakura"]
print(names)              # ['Remilia', 'Flandre', 'Cirno', 'Sakura']
print(names[0:3:2])       # ['Remilia', 'Cirno']
print(names[:3])          # ['Remilia', 'Flandre', 'Cirno']
print(names[3:])          # ['Sakura']
for name in names[:]:     # Remilia,Flandre,Cirno,Sakura,
    print(name, end=",")
print()
# 复制列表副本
fork_names = names[:]
del names[-1]
del fork_names[0]
print(names)              # ['Remilia', 'Flandre', 'Cirno']
print(fork_names)         # ['Flandre', 'Cirno', 'Sakura']
