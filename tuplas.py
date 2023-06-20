tuplanumeros = (1, 2, 3, 4, 5)
tuplaLetras = ("victor", "hernan", "biondini")
tuplaBoolean = (False, True)
tuplaCombinada = ("victor", 2, False)

print(tuplanumeros) 
print(tuplaCombinada)
print(tuplaCombinada[0], tuplaCombinada[1])
print(len(tuplanumeros))
print(len(tuplaLetras))
  
print(tuplaLetras)
print(tuplaLetras[1:3])

x = list(tuplaLetras)
x[1] = "Hernán"
tuplaLetras = tuple(x)
print(tuplaLetras)


(uno, dos, tres, cuatro, cinco) = tuplanumeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

tuplanumeros2 = (1, 2, 3, 4, 5, 4)
num = 4
print("cantidad: {}".format(num) , tuplanumeros2.count(num))
print(tuplanumeros2.index(3))



