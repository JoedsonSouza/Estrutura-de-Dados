fileName = input("Nome do arquivo: ")
arqTxt = open(fileName + '.txt', 'r')
L = []
for i in arqTxt:
    L.append(i)
v = 0
for i in range(0, len(L)):
    aux = L[i]
    for j in aux:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            v += 1
print("O arquivo possui", v, " vogais")
