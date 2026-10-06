# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1) - Asignación directa, de volada.

def random_function(students):
    first = students[0] # O(1) - Acceder a un índice es instantáneo.
    total = 0 # O(1) - Crear una variable no cuesta nada.
    new_list = [] # O(1) - Otra creación, todo chill.

    for student in students: # O(n) - Aquí empieza lo bueno. Recorres la lista de tamaño "n".
        total += 1 # O(1) - Sumar es rápido, pero pasa "n" veces.
        new_list.append(student) # O(1) - Agregar al final de una lista es rápido, pero pasa "n" veces.

    print(new_list) # O(n) - Convertir y escupir la lista completa escala con el tamaño "n".
    return total # O(1) - Retornar un resultado y ya.

print(random_function(student_list_01)) # La llamada cuesta lo que cueste la función, o sea O(n).