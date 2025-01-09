people = ['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']

def delete_person(person_name):
    
    new_list = [person for person in people if person != person_name]
    return new_list


print(delete_person("daniella"))  
print(delete_person("juan"))  
print(delete_person("emilio")) 
