import random

my_list = [4, 5, 734, 43, 45]

for _ in range(10):  
    random_number = random.randint(1, 100)  
    my_list.append(random_number) 


print("Lista después de agregar 10 números aleatorios:", my_list)

