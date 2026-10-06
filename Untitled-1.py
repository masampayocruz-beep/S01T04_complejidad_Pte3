student_list = ["Jorda", "Pipen", "Curry", "Shack"]
student_list = ["Mike", "Saul", "Walter", "Jessy"]

#Verificar presencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:  #
                       print("Estudiante encontrado")
            return student

#Si no encuentra el estudiante, se retorna None
        print("🚫Estudiante no encontrado")  #(1)
        return None

#Probando algoritmo
check_student("Walter", student_list)


