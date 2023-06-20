#print("ingresa tu nombre")
#nombre = "hernan"
#input()
#print("Tu nombre: " + nombre, type(nombre))


def http_error(status):
        match status:
            case 400:
                return "Solicitud incorrecta"
            case 200: 
                return "OK"
            case _:
                return "Ha ocurrido un error"

print(http_error(-1))

dias = ["lunes", "martes","miercoles","jueves"]
for x in dias:
    if x == "miercoles":
        print(x)
    print(x)

print("---")

for x in dias:
    if x == "miercoles":
        break
    print(x)

print("---")

numero = 5
for x in range(numero):
    print("Hola") 

print("---")

# Generar una secuencia de números de 0 a 9
for num in range(10):
    print(num)
# Salida: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print("---")

# Generar una secuencia de números pares de 0 a 10
for num in range(0, 11, 2):
    print(num)
# Salida: 0, 2, 4, 6, 8, 10

print("---")

# Convertir la secuencia en una lista
numbers = list(range(5))
print(numbers)
# Salida: [0, 1, 2, 3, 4]

for num in range(0):
    print(num)
else:
    print("fin")