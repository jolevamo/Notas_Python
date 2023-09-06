print("-----------Calcular nota definitiva-----------")
nombre = input("Nombre esudiante:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
definitva = (nota1 + nota2 + nota3)/3
# print("Nommbre: ", nombre," Nota 1 -->",nota1," Nota 2 -->",nota2," Nota 3 -->",nota3," Definitiva -->",definitva)

print(F"Nommbre:  {nombre} \nNota 1 -->{nota1} \nNota 2 -->{nota2} \nNota 3 -->{nota3} \nDefinitiva -->{definitva}")

# if definitva >= 3:
#     print("Felicitaciones")
# else: 
#     print("Perdio por vago")

if definitva <0 or definitva >5:
    print("Error, revise las notas ingresadas, deben estar entre 0 y 5")
elif definitva <= 2:
    print("El estudiante tiene problemas de atención")
elif definitva < 3:
    print("Puede recuperar")
elif definitva <= 4:
    print("Muy bien, gano")
elif definitva <= 4.6:
    print("Eres genial")
else:
    print("Eres el mejor")

