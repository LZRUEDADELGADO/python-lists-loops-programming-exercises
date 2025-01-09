sample_list = [45, 67, 87, 23, 5, 32, 60]

new_list = []

for i in range(len(sample_list) - 1, -1, -1): 
    new_list.append(sample_list[i])

print("lista inicial: ", sample_list)
print("lista final:   ", new_list)
