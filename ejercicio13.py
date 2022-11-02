lista_numeros = []
numero_intr = int(input("Introduzca un numero:\n"))
valores_abs = 0

while numero_intr != 0:
    lista_numeros.append(numero_intr)
    numero_intr = int(input("Introduzca un numero:\n"))

media = sum(lista_numeros) / len(lista_numeros)

for i in range(len(lista_numeros)):
    valores_abs += abs(lista_numeros[i] - media) ** 2

desviacion = (valores_abs / len(lista_numeros)) ** 0.5

print("Su lista es:", lista_numeros)
print("La media de la lista es:", media)
print("La desviacion tipica es:", desviacion)