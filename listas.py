modulos = ["Lógica", "Base Datos", "HTML5", "Moviles 1","HTML5"]
# imprimir una lista
print(modulos)
print("Elemento inicial de la lista:",modulos[0])
#Imprimir el último elemento de una lista
print("Elemento final de la lista:",modulos[-1])

print("Número de elementos que contiene la lista:",len(modulos))
print("Elemento final de la lista:",modulos[len(modulos)-1])

#Agregar un elemento a la lista
modulos.append("Metodologias agiles")
print(modulos)

#Agregar un elemento a la lista en una posición especifica
modulos.insert(0,"Moviles 2")
print(modulos)

#Contar las veces que se repite un elemento en una lista
print("La cantidad de veces que se repite HTML5 es: ",modulos.count("HTML5"))

#Ordenar una lista
modulos.sort()
print("La lista ordenada alfabeticamente es: ",modulos)

#Imprimir una lista
i=1
for indice in modulos:
    print(i,".",indice)
    i=i+1
