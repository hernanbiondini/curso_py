class MiClase:
    def __init__(self):
        self.__atributo_privado = 42

    def __metodo_privado(self):
        print("Este es un método privado")

    def acceder_atributo(self):
        return self.__atributo_privado

    def llamar_metodo(self):
        self.__metodo_privado()


objeto = MiClase()
print(objeto.acceder_atributo())  # Salida: 42
objeto.llamar_metodo()  # Salida: "Este es un método privado"
#print(objeto.__atributo_privado)  # Error: AttributeError
#objeto.__metodo_privado()  # Error: AttributeError
