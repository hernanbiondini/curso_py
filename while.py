
numero = 1

while numero <= 10:
    print(numero)
    if numero == 7:
        break
    numero = numero + 1
print("-###-")

numero = 0
while numero <= 10:
    numero = numero + 1
    if numero == 6:
        continue
    print(numero)

print("---")

numeros = int(input("Introduce un numero natural:"))
result = 0
control = 1
while control <= numeros:
    result += control
    control = control + 1
print("La suma de numeros naturales es: ", result)

