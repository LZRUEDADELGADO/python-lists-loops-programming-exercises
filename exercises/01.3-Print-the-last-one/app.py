# Importa el paquete random
import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range(randonlength):
        aux_list.append(random.randint(1, 100))  # Generar números aleatorios para la lista
    return aux_list

my_stupid_list = generate_random_list()

# Encuentra el último elemento de la lista
the_last_one = my_stupid_list[-1]

# Imprime la lista completa (opcional, para verificar)
print("Lista generada:", my_stupid_list)

# Imprime el último elemento
print("El último elemento:", the_last_one)
