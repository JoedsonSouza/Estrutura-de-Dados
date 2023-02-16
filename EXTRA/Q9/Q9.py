vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeroConvertido = []
numBinario = []

for i in range(0, 10):
    binario = []
    quociente = vetor[i]
    
    while quociente > 0:
        resto = quociente % 2
        binario.append(resto)
        quociente = quociente // 2
    binario.append(quociente)
            
    binario.reverse()
    numeroConvertido.append(binario)

for i in range(10): #representa cada item da lista de número convertidos
    num = ''
    for j in range(0, len(numeroConvertido[i])):    #representa cada sublista da lista de número convertidos
        num += str(numeroConvertido[i][j])          #converte cada item [j] da sublista atual [i] em string e os concatena
    numBinario.append(num)

arqTxt = open('conversao', 'w')
for i in range(10):
    arqTxt.write(f'{vetor[i]} = {numBinario[i]} \n')
arqTxt.close()
