# Adding the sum of all elements in a row at the end of the list

matriz = [
    [2, 4, 3],
    [8, 3, 4],
    [7, 1, 3],
    [9, 2, 1]
]

""" Applying the append method """
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))
print(matriz)

# Previous operation should be commented to apply following resolution
""" Applying slicing """
matriz[0][len(matriz):] = [sum(matriz[0])]
matriz[1][len(matriz):] = [sum(matriz[1])]
matriz[2][len(matriz):] = [sum(matriz[2])]
matriz[3][len(matriz):] = [sum(matriz[3])]
print(matriz)