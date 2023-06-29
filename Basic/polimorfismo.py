class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

# Crear una instancia de la clase Persona
persona = Persona("Juan", 25)

# Acceder a los atributos utilizando los métodos get
print(persona.get_nombre())  # Salida: Juan
print(persona.get_edad())    # Salida: 25

# Intentar acceder directamente a los atributos privados
print(persona.__nombre)  # Generará un error

# Intentar modificar directamente los atributos privados
persona.__edad = -10  # No se modificará el valor correctamente

# Utilizar los métodos set para modificar los atributos
persona.set_nombre("Carlos")
persona.set_edad(30)

# Acceder nuevamente a los atributos utilizando los métodos get
print(persona.get_nombre())  # Salida: Carlos
print(persona.get_edad())    # Salida: 30
