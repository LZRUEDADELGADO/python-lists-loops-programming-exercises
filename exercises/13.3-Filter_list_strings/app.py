names = [
    'Liam', 'Emma', 'Noah', 'Olivia', 'William', 'Ava', 'James', 'Isabella',
    'Logan', 'Sophia', 'Benjamin', 'Mia', 'Mason', 'Charlotte', 'Elijah', 'Amelia',
    'Oliver', 'Evelyn', 'Jacob', 'Abigail', 'Lucas', 'Harper', 'Michael', 'Emily',
    'Alexander', 'Elizabeth', 'Ethan', 'Avery', 'Daniel', 'Sofia', 'Matthew', 'Ella',
    'Aiden', 'Madison', 'Henry', 'Scarlett', 'Joseph', 'Victoria', 'Jackson', 'Aria',
    'Samuel', 'Grace', 'Sebastian', 'Chloe', 'David', 'Camila', 'Carter', 'Penelope',
    'Wyatt', 'Riley'
]


def contains_string(name):
    return 'am' in name.lower()

filtered_names = list(filter(contains_string, names))

print(filtered_names)

