estudiante = ("Linda", "Nuevas metodologias",[4,1.7,4.9])

#Cantidad de elementos
print("La cantidad de elementos que contiene la tupla: ",len(estudiante))

nombreEstudiante = estudiante[0]
nombreAsignatura = estudiante[1]
notaEstudiante = estudiante[2]

print(f"Nombre de estudiante: {nombreEstudiante}\nAsignatura: {nombreAsignatura}\nNotaEsudiante: {notaEstudiante}\nPromedio: {(notaEstudiante[0]+notaEstudiante[1]+notaEstudiante[2])/3}")