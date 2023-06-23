# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido.")

    def que_es(self):
        print(type(self))

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        print("El perro hace: ¡Guau!")

# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, raza, color):
        super().__init__(nombre)
        self.raza = raza
        self.color = color

    def hacer_sonido(self):
        print("El gato hace: Miau!")

# Creación de objetos
animal_generico = Animal("Animal")
perro = Perro("Bobby", "Labrador")
gato = Gato("Bianca", "gato gordo", "Amarillo")
# Llamada a los métodos
animal_generico.hacer_sonido()  # Salida: El animal hace un sonido.
animal_generico.que_es()

perro.hacer_sonido()  # Salida: El perro hace: ¡Guau!
perro.que_es()  # Salida: El animal hace un sonido.

gato.hacer_sonido()
print(gato.nombre)
print(gato.color)
print(gato.raza)
gato.que_es()