L = []
fileName = input("Nome do arquivo: ")
arqTxt = open(fileName + '.txt', 'r')
for i in arqTxt: #percorre cada linha do arquivo
    L.append(i)
print("O arquivo possui ", len(L), "linhas.")
