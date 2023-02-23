fileName = input("Nome do arquivo: ")
arquivo = open(fileName + '.txt', 'r')
dataHoje = input("Informe a data atual (DD MM AAAA): ")

L = []

for i in arquivo:   #percorre cada linha do arquivo e armazena na lista L
    L.append(i)
arquivo.close()

nomes = []
datas = []
idades = []

for i in range(len(L)): # (0, até a quantidade de linhas do arquivo - percorre as linhas do arquivo que estão armazenadas em indices da lista)
    aux = L[i]
    letras = ''
    numeros = ''
    for j in aux:   #percorre cada caracter da linha
        if j == '0':
            numeros += '0'
            
        elif j == '1': 
            numeros += '1'
            
        elif j == '2':
            numeros += '2'
            
        elif j == '3':
            numeros += '3'
            
        elif j == '4':
            numeros += '4'

        elif j == '5':
            numeros += '5'

        elif j == '6':
            numeros += '6'

        elif j == '7':
            numeros += '7'

        elif j == '8':
            numeros += '8'

        elif j == '9':
            numeros += '9'
            
        else:
            letras += j
    nomes.append(letras)
    datas.append(numeros)

for i in range(len(datas)):
    nascimento = int(datas[i])
    dia_nasc = nascimento // 1000000
    resto = nascimento % 1000000
    mes_nasc = resto // 10000
    ano_nasc = resto % 10000

    dataHojeFormatada = ''
    for i in dataHoje:
        if i != ' ':
            dataHojeFormatada += i

    atual = int(dataHojeFormatada)
    dia_atual = atual // 1000000
    restoA = atual % 1000000
    mes_atual = restoA // 10000
    ano_atual = restoA % 10000

    idade = ano_atual - ano_nasc
    if mes_atual < mes_nasc or (mes_atual == mes_nasc and dia_atual < dia_nasc):
        idade -= 1

    idades.append(idade)

novoArquivo = open('idades.txt', 'w')
for i in range(len(idades)):
    novoArquivo.write(f'Nome: {nomes[i]}\nIdade: {idades[i]} \n\n')
novoArquivo.close()
