lista = ["SIPA", "DAPI", "SIRC", "GPIT", "SIHD"]
nota = []
for asignatura in lista:
    print("Introduzca su nota de:", asignatura)
    nota.append(input())

for resultado in range(len(lista)):
    print(lista[resultado], "=>", nota[resultado])