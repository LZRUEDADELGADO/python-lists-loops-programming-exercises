my_list = [43, 23, 6, 87, 43, 1, 4, 6, 3, 67, 8, 3445, 3, 7, 5435, 63, 346, 3, 456, 734, 6, 34]

def max_integer(numbers):
    max_value = numbers[0]
    
    for num in numbers:
        if num > max_value:  
            max_value = num  
    
    return max_value 

print(max_integer(my_list))