class Calculadora:
    def __init__(self):
        self.resultado = 0
        print("INICIANDO CALCULADORA")

    def sumar(self, num):
        print("... sumando...")
        self.resultado += num

    def restar(self, num):
        self.resultado -= num

    def obtener_resultado(self):
        return self.resultado

# Creación de un objeto
calc = Calculadora()

# Uso de los métodos de la clase
calc.sumar(5)
calc.restar(2)
print(calc.obtener_resultado())  # Salida: 3

