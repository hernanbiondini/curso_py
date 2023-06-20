# Esta función suma dos números
def sumar(x, y):
    return x + y

# Esta función resta dos números
def restar(x, y):
    return x - y

# Esta función multiplica dos números
def multiplicar(x, y):
    return x * y

# Esta función divide dos números
def dividir(x, y):
    return x / y

print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Solicitar la elección al usuario
opcion = input("Ingrese la opción (1/2/3/4): ")

# Verificar si la opción es válida
if opcion in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
    else:
        if opcion == '1':
            print(num1, "+", num2, "=", sumar(num1, num2))
        elif opcion == '2':
            print(num1, "-", num2, "=", restar(num1, num2))
        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))
        elif opcion == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", dividir(num1, num2))
            else:
                print("Error: No se puede dividir entre cero.")
else:
    print("Opción inválida.")
