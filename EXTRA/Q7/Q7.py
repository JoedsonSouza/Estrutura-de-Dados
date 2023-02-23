fileName1 = input("Nome do arquivo de origem: ")
arqInput = open(fileName1 + '.txt', 'r')
L = []

for i in arqInput:
    L.append(i)
arqInput.close()

novaLista = []

for i in range(len(L)): #percorre cada linha do arquivo
    aux = L[i]
    nova = ''
    for j in aux:   #percorre cada caracter da linha
        if j == 'a' or j == 'A':
            nova += '@'
            
        elif j == 'e' or j == 'E':
            nova += '&'
            
        elif j == 'i' or j == 'I':
            nova += '1'
            
        elif j == 'o' or j == 'O':
            nova += '0'
            
        elif j == 'u' or j == 'U':
            nova += '#'
            
        else:
            nova += j
            
    novaLista.append(nova)
fileName2 = input("Nome do arquivo de destino: ")
arqOutput = open(fileName2 + '.txt', 'w')
for linha in novaLista:
    arqOutput.write(linha)
arqOutput.close()
