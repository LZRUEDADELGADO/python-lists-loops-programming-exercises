mix = [42, True, "towel", [2, 1], 'hello', 34.4, {"name": "juan"}]

def print_types(input_list):
    for item in input_list:
        print(type(item))

print_types(mix)
