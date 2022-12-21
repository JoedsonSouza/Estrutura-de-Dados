#fileName1 = "IFBABAIANO" --> 10 LETRAS
#strPadrao = "IFBA" --> 4 LETRAS (o que vou susbtituir)
#strSubst = "IF"    (pelo o quê vou substituir)

def sed(strPadrao, strSubst, fileName1, fileName2):
    arqTxt = open(fileName1, 'r')
    L = []
    for i in arqTxt:
        L.append(i)
    for i in range(0, len(L)):  #percorre cada linha do arquivo e armazena na lista L
        aux = L[i]
        nova = ''
        for j in range(0, len(aux)-len(strPadrao)): # range(0, 10-4) para não estourar a lista de caracteres
            v = ''
            for k in range(j, len(strPadrao)):      #(j, 4) para verificar da posição atual até as próximas 4, que é a quantidade de letras da string que estou procurando
                v += aux[k]                         #concatena o caractere na posição j e os próximos 4
            if v == strPadrao:
                nova = nova + strSubst
                j = j + len(strPadrao)       
            else:
                nova = nova + aux[j]                    
        print(nova)

sed('ifba', 'bahia', 'arq1.txt', 'arq2.txt')
