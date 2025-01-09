def filter_greater_than_ten(numbers):

    return list(filter(lambda x: x > 10, numbers))

numbers = [23, 12, 35, 54, 21, 534, 23, 42]

filtered_numbers = filter_greater_than_ten(numbers)
print(filtered_numbers)

