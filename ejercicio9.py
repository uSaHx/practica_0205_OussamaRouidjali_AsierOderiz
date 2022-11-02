palabra = input("Introduzca una palabra: \n")
vocales = ["a", "e", "i", "o", "u"]

for n in vocales:
    contador = palabra.count(n)
    print("La palabra", palabra, "contiene la vocal", n, contador, "veces")
