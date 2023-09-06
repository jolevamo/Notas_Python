#Crear un diccionario y añadir elementos al mismo
agenda = {
    "contacto1":
        {"nombre" : "Camilo",
        "telefono" : 3145892314,
        "direccion" : "CR 23 45 69",
        "correo" : "camilo@gmail.com"
        },
    "contacto2":
        {"nombre" : "Juan",
        "telefono" : 3214568974,
        "direccion" : "CR 45 45 83",
        "correo" : "juan@gmail.com"
        },
    "contacto3":
        {"nombre" : "Felipe",
        "telefono" : 3124587914,
        "direccion" : "CR 85 86 41",
        "correo" : "felipe@gmail.com"
        },
    "contacto4":
        {"nombre" : "Stiven",
        "telefono" : 3214569874,
        "direccion" : "CR 23 85 69",
        "correo" : "stiven@gmail.com"
        },
    "contacto5":
        {"nombre" : "David",
        "telefono" : 3051234789,
        "direccion" : "CR 12 45 98",
        "correo" : "david@gmail.com"
        }
}
#Acceder a toda la agenda:
#print(agenda)

#Acceder al nombre utilizando el método Get
# nombre = agenda["contacto1"].get('nombre','No encontrado')
# print(f"Nombre del contacto 1 obtenido utilizando el método Get es: {nombre}")

for i in agenda:
    contacto = agenda.keys()
    print(f"{contacto}")

#Actualiza un elemento en el diccionario
# agenda["contacto1"]["nombre"]="Jaime"

# #Usar el método Key para obtener todas las claves del diccionario

# clavesContacto1 = agenda["contacto1"].keys()
# print(f"Las claves obtenidas del contacto1 son: {clavesContacto1}")

# #Usar el método items para obtener todos los pares del diccionario
# paresContacto1 = agenda["contacto1"].items()
# print(f"Los pares obtenidos del contacto1 son: {paresContacto1}")