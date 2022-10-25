lista_ganadores = []

numero_ganador = int(input("Numero Ganador:\n"))

while numero_ganador != 0:
    lista_ganadores.append(numero_ganador)
    numero_ganador = int(input("Numero Ganador:\n"))

lista_ganadores.sort()
print("La lista de los numeors ganadores de menor a mayor es de:")
for numero in lista_ganadores:
    print(numero)