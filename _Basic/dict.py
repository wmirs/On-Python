alien = {"color": "green", "points": 5}
print(alien)              # {'color': 'green', 'points': 5}
print(alien["color"])     # green
print(alien["points"])    # 5
alien["x_position"] = 5
alien["y_position"] = 10
print(alien)              # {'color': 'green', 'points': 5, 'x_position': 5, 'y_position': 10}
alien["color"] = "red"
print(alien)              # {'color': 'red', 'points': 5, 'x_position': 5, 'y_position': 10}
del alien["color"]
print(alien)              # {'points': 5, 'x_position': 5, 'y_position': 10}
del alien["x_position"]
print(alien)              # {'points': 5, 'y_position': 10}

favorite_languages = {
    "Sakura": "Java",
    "Remilia": "Python",
    "Cirno": "Go",
    "Flandre": "Python"
}
""" items()
Sakura favorite language is Java.
Remilia favorite language is Python.
Cirno favorite language is Go.
Flandre favorite language is Python.
"""
for name, language in favorite_languages.items():
    print(f"{name.title()} favorite language is {language}.")
""" keys()
Sakura    Remilia    Cirno    Flandre    
"""
for name in favorite_languages.keys(): 
    print(name.title(), end="    ")
print()
""" 隐式调用了keys()方法
Sakura    Remilia    Cirno    Flandre    
"""
for name in favorite_languages: 
    print(name.title(), end="    ")
print()
""" values()
dict_values(['Java', 'Python', 'Go', 'Python'])
"""
print(favorite_languages.values())
# ['Java', 'Python', 'Go', 'Python']
print(list(favorite_languages.values()))
# {'Java', 'Go', 'Python'}
print(set(favorite_languages.values()))

#update()方法
dict1 = {"remilia": "scarlet", "flanre": "scarlet", "cirno": "sakura", "address": "koumakan"}
dict2 = {"ages": [500, 495, 9]}
print(dict1)
dict1.update(dict2)
print(dict1)

dict_0 = {}
for key, value in zip(range(5), reversed(range(5))):
    dict_0[key] = value
dict_1 = dict(zip(range(5), reversed(range(5))))
print(dict_0)
print(dict_1)

dict_2 = {"remilia": 500, "flandre": 495, "cirno": 9}
if "sakura" in dict_2:
    print(f"sakura={dict_2['sakura']}")
else:
    print("'sakura' not exists.")
print(dict_2.get("sakura"))
print(dict_2.get("sakura", 18))
if "sakura" in dict_2:
    poped_age_1 = dict_2.pop("sakura")
else:
    poped_age_1 = 3
poped_age_2 = dict_2.pop("sakura", 28)
print(f"poped_1 = {poped_age_1}, poped_2 = {poped_age_2}")


words = ["apple", "bat", "bar", "atom", "book"]
by_letter = {}
for word in words:
    letter = word[0]
    # 更新
    by_letter.setdefault(letter, []).append(word)
print(by_letter)

dict_3 = {123: "123", 123.0: "123.0"}
print(dict_3)