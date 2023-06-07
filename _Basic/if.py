cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:     # Audi, BMW, Subaru, toyota, 
    if car.lower() == "bmw":
        print(car.upper(), end=", ")
    elif car.lower() == "toyota":
        print(car.lower(), end=", ")
    else:
        print(car.title(), end=", ")
print()

age = 18
print(age < 16 and age >= 18)  # False and True => False
print(age < 16 or age >= 18)   # False or True  => True

names = []
if names:           # names list is EMPTY.
    print(names)
else:
    print("names list is EMPTY.")