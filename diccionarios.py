

#Creación de un diccionario:
diccionario1 = {"clave1": 1, "clave2": 2, "clave3": 3}
diccionarion = {"clave1": 1, "clave2": 2, "clave3": 3}


#Acceso a valores mediante claves:
diccionario2 = {"nombre": "Juan", "edad": 30, "país": "España"}
print(diccionario2["nombre"])  # Output: "Juan"
print(diccionario2["edad"])    # Output: 30


#Modificación de valores:
diccionario3 = {"a": 1, "b": 2, "c": 3}
diccionario3["b"] = 4
print(diccionario3)  # Output: {"a": 1, "b": 4, "c": 3}

print("diccionarion: ", diccionarion)
diccionarion.update({"clave3": "HERNAN"})
print("diccionarion: ", diccionarion)


#Agregar nuevos pares clave-valor:
diccionario4 = {"nombre": "María", "edad": 25}
diccionario4["país"] = "México"
print(diccionario4)  # Output: {"nombre": "María", "edad": 25, "país": "México"}


#Eliminación de elementos:
diccionario5 = {"a": 1, "b": 2, "c": 3}
del diccionario5["b"]
print(diccionario5)  # Output: {"a": 1, "c": 3}


#Iteración sobre claves y valores:
diccionario6 = {"a": 1, "b": 2, "c": 3}
for clave in diccionario6:
    valor = diccionario6[clave]
    print(clave, valor)


#Verificación de existencia de una clave:
diccionario7 = {"nombre": "Ana", "edad": 35}
print("nombre" in diccionario7)  # Output: True
print("ciudad" in diccionario7)  # Output: False

print(diccionario1)
clave = "clave2"
if clave in diccionario1:
        print("Existe la clave: ", clave, " con valor: ", diccionario1[clave])
else:
        print("No existe la clave: ", clave)

print(diccionario1.keys())
diccionario1.pop(clave)
print(diccionario1.keys())

print(diccionario1.values())
print(diccionario1.items())

