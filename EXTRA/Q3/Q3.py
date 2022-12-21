fileName = input("Nome do arquivo: ")
arqTxt = open(fileName + '.txt', 'r')
L = []
for i in arqTxt:
    L.append(i)
v = 0
c = 0
for i in range(0, len(L)):
    aux = L[i]
    for j in aux:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            v += 1
        else:
            if j != ' ' and j != '\n':
                c += 1
print(v, ' letras são vogais.')
print(c, ' letras são consoantes.')
