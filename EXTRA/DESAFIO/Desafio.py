fileName1 = input("Nome do arquivo de origem: ")
arqInput = open(fileName1 + '.txt', 'r')
L = []

for i in arqInput:
    L.append(i)
arqInput.close()

novaLista = []

for i in range(len(L)-1, -1, -1):
    aux = L[i]
    nova = ''
    for j in reversed(aux):
        nova += j
    novaLista.append(nova)

fileName2 = input("Nome do arquivo de destino: ")
arqOutput = open(fileName2 + '.txt', 'w')
for linha in novaLista:
    arqOutput.write(linha)
arqOutput.close()
