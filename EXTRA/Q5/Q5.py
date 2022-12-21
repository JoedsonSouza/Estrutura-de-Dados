fileName = input("Nome do arquivo: ")
arqTxt = open(fileName + '.txt', 'r')
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cont = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
L =[]
for i in arqTxt:    #percorre cada linha do arquivo e armazena na lista L
    L.append(i)
for i in range(0, len(L)):  # (0, até a quantidade de linhas do arquivo - percorre as linhas do arquivo que estão armazenadas em indices da lista)
    aux = L[i]              # adiciona cada linha à variável aux em cada execução, para que póssamos posteriormente percorrer cada caracter da linha 
    for j in aux:           # percorre cada letra da linha do arquivo
        for k in range(0, len(alfabeto)):   # percorre cada letra do alfabeto para comparar com as letras presentes no arquivo
            if j == alfabeto[k]:            # se cada letra da linha for igual a uma das letras do alfabeto, faça:
                cont[k] += 1                # contado de cada letra recebe 1 ao seu valor total

for i in range(0, len(alfabeto)):
    print(alfabeto[i] + " = ", cont[i])
