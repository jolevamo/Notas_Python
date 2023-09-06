respuesta = 1

while respuesta == 1:
    respuesta = int(input("1. Si\n2. No\nEscriba el Nro para continuar: "))

    while respuesta != 1 and respuesta != 2:
        print("Usted digito mal")
        respuesta = int(input("1. Si\n2. No\nEscriba el Nro para continuar: "))