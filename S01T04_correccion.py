# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack']

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students:
        print("Se le suma 1 al total") # O(1)
        total += 1 # O(n)
        new_list.append(student) # O(n)

    print(new_list) # O(1)
    return total # O(1)

print(f"Tamañao de las lista {len(student_list_01)}")
print(random_function(student_list_01))
print("")

#Calcular o(2n)+o(5) = o(2n+5) = o(n)