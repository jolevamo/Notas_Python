mensaje = "       Bienvenido...Al curso de Python "

#Método Len, imprime el tamaño de longitud del string, contando los espacios
print("El texto con espacios es: ",mensaje)
print("El tamaño del texto es de, ",len(mensaje))

# STRIP: Quita espacios al inicio y al final
sinEspacios = mensaje.strip()

print("El texto sin espacios es de: ",sinEspacios)
print("El tamaño del texto sin espacios es de: ",len(sinEspacios))

#CONVERTIR EL TEXTO

#upper: Mayuscula sostenida
print("En MAYUSCULA sostenida: ",sinEspacios.upper())

#lower: minuscula
print("En minúscula: ",sinEspacios.lower())

#title: La inicial de cada palabra la pone en mayuscula
print("Texto cómo titulo: ",sinEspacios.title())

#capitalize: Sólo pone la primer inicial en mayuscula
print("La primer inicial en mayuscula: ",sinEspacios.capitalize())

#split: Divide la cadena en una lista de subcadenas usando 'delimiter' como separado
parrafo = sinEspacios.split('...')
print(parrafo[0])
print(parrafo[1])