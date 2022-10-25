palabra = input("Introduzca una palabra: \n")

if palabra == palabra[::-1]:
    print(palabra, "es una palabra palindroma")
else:
    print(palabra, "no es una palabra palindroma")