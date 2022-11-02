A = [[1, 2, 3],
     [4, 5, 6]]
B = [[-1, 0],
     [0, 1],
     [1, 1]]
resultado = [[0, 0],
             [0, 0]]

for x in range(len(A)):
    for y in range(len(B[0])):
        for z in range(len(B)):
            resultado[x][y] += A[x][z] * B[z][y]

for r in resultado:
    print(r)
