

# Funciones con retorno múltiple:
def dividir(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

resultado_division = dividir(10, 3)
print(resultado_division)  # Output: (3, 1)

def imprimirNombre(nombre, apellido):
    return "Hola", nombre, apellido
print(imprimirNombre("Victor", "Hernan")) 


#Uso de funciones como argumentos:
def operar(a, b, operacion):
    resultado = operacion(a, b)
    return resultado

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

resultado_operacion = operar(2, 3, suma)
print(resultado_operacion)  

resultado_operacion = operar(2, 3, resta)
print(resultado_operacion) 

print(suma(3,3)) 

# Funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = 5
resultado_factorial = factorial(numero)
print("Factorial de {}{} ".format(numero, ":"), resultado_factorial)  # Output: 120


