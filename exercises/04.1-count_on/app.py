my_list = [42, True, "towel", [2, 1], 'hello', 34.4, {"name": "juan"}]

new_list = []

for item in my_list:
    if isinstance(item, (dict, list)):
        new_list.append(item)

print(new_list)