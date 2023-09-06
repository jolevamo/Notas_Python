# Validar una clave y al tercer intento bloquear

clave = 785
contador = 0

while contador <= 3:
    respuesta = int(input("Ingrese la clave: "))
    if respuesta == clave:
        print("Bienvenido")
        break
    else:
        contador = contador + 1
        print(F"Clave fallida, Cantidad de intentos: {contador}")
    if contador == 3:
        print("Su usuario ha sido bloqueado por 24 horas")
        break