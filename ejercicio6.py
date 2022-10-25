lista = ["SIPA", "DAPI", "SIRC", "GPIT", "SIHD"]
nota = []
for asignatura in lista:
    print("Introduzca su nota de:", asignatura)
    nota.append(int(input()))

print("Tienes que recuperar:")
for resultado in range(len(lista)):
    if nota[resultado] < 5:
        print(lista[resultado], "=>", nota[resultado])