import math

strings = ["a", "as", "bat", "car", "dove", "python"]
upper_strings = [item.upper() for item in strings if len(item) > 2]
print(upper_strings)
unique_lengths = {len(item) for item in strings}
print(unique_lengths)
string_length_mapping = {item:len(item) for item in strings}
print(string_length_mapping)

print(set(map(len, strings)))
print(tuple(map(len, strings)))
print(list(map(len, strings)))
print(set(map(math.sqrt, range(0, 11))))


all_data = [["John", "Emily", "Michael", "Mary", "Steven"],
            ["Maria", "Juan", "Javier", "Natalia", "Pilar"]]
print([name for names in all_data for name in names if name.count("e") >= 2])
result_0 = []
for names in all_data:
    result_0.extend([name for name in names if name.count("e") >= 2])
print(result_0)

result_1 = [name for names in all_data for name in names if name.count("e") >= 2]
print(result_1)
