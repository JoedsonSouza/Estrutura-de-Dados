#fileName1 = "IFBABAIANO" --> 10 LETRAS
#strPadrao = "IFBA" --> 4 LETRAS (o que vou susbtituir)
#strSubst = "BAHIA"    (pelo o quê vou substituir)

def sed(strPadrao, strSubst, fileName1, fileName2):
    arqTxt = open(fileName1, 'r')
    L = []
    for i in arqTxt:    #percorre cada linha do arquivo e armazena na lista L
        L.append(i)
    arqTxt.close()

    novaLista = [] #Criar nova lista para armazenar as linhas modificadas
    
    for i in range(0, len(L)):  # 0, até a quantidade de linhas do arquivo - percorre as linhas do arquivo que estão armazenadas em indices da lista)
        aux = L[i]              # em cada execução armazena a linha atual na variável aux, para que póssamos posteriormente percorrer cada caracter da linha
        nova = ''               # armazena a linha após as substituições terem sido realizidas
        j = 0                   # Corrigir a inicialização de J para que a cada loop interno, ele percorra a linha desde o inicio.
        while j <= len(aux) - len(strPadrao): # Enquanto 0 <= 6 (10-4) para não estourar a lista de caracteres. (enquanto o índice j não ultrapassar o tamanho da linha atual menos o tamanho da string-padrão.
            v = ''                                  #é usada para coletar os caracteres do texto original que devem ser comparados com a string-padrão
            for k in range(j, j + len(strPadrao)):      #(j, 4) para verificar da posição atual até as próximas 4, que é a quantidade de letras da string que estou procurando
                v += aux[k]                         #percorre a linha atual e concatena o caractere na posição j e os próximos 3 para comparar com a string padrão
            if v == strPadrao:
                nova = nova + strSubst              #strSubst é adicionada a variável nova
                j = j + len(strPadrao)              #j passa a ter a posição logo após a última ocorrência da STRING PADRÃO. J = 0 + 4. Então no loop 'pai' a expressão se torna: enquanto 4<=6
            else:
                nova = nova + aux[j]                #adiciona o caracter atual da linha à linha modificada, já que seus caracteres que não correspondem à string-padrão
                j = j + 1                           #j passa a ter a posição seguinte, para verificar se havera ocorrências nos próximos conjuntos de caracteres
                
        for k in range(j, len(aux)):                # Adiciona os caracteres restantes da linha. Em nosso caso (4,10). BAHIA'BAIANO'
            nova += aux[k]
        novaLista.append(nova)

    arqSaida = open(fileName2, 'w')
    for linha in novaLista:
        arqSaida.write(linha)
    arqSaida.close()

sed('ifba', 'bahia', 'arq1.txt', 'arq2.txt')
