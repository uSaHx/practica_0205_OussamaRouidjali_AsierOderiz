import string
abc = list(string.ascii_lowercase)

for letra in range(len(abc), 1, -1):
    if letra % 3 == 0:
        abc.pop(letra - 1)
print(abc)