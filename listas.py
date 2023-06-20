
lista1 = [1, 2, 3, 4, 5]

print(len(lista1))

for num in lista1:
    print("val: " , num)

lista2 = ["a", "b", "c", "d", "e"]
print(lista2[2])  # Output: "c"
print(lista2[-2])  # Output: "d"
print(lista2[1:3])  

lista3 = [10, 20, 30, 40, 50]
lista3[2] = 35
print(lista3)  # Output: [10, 20, 35, 40, 50]

lista5 = [1, 2, 3, 4, 5]
del lista5[2]
print(lista5)  # Output: [1, 2, 4, 5]

lista6 = [10, 20, 30, 40, 50]
for elemento in lista6:
    print(elemento)

lista7 = ["manzana", "banana", "naranja"]
print("manzana" in lista7)   # Output: True
print("pera" in lista7)      # Output: False

lista4 = ["manzana", "banana", "cereza"]
lista4.append("naranja")
lista4.remove("banana")

print(lista4)  # Output: ["manzana", "cereza", "naranja"]

lista5 = ["manzana", 1.3, True]
print(lista5)
