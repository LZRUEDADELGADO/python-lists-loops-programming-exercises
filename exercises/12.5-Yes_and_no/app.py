the_bools = [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

def bool_to_text(value):
    
    return "wiki" if value == 1 else "woko"

new_list = list(map(bool_to_text, the_bools))


print(new_list)
