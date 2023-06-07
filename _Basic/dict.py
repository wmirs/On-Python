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
