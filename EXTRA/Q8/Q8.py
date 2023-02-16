nome = []
numero = []
while True:     #o código será executado pelo menos uma vez e depois o loop continuará enquanto a condição especificada no if
    name = input("Digite o nome do contato: ")
    numberPhone = input("Digite o número do contato: ")

    #if not numberPhone != '0':
    if numberPhone == '0':
        break
    nome.append(name)
    numero.append(numberPhone)

arqSaida = open('agenda', 'w')
for i in range(0, len(nome)):
    arqSaida.write(f'Nome: {nome[i]} \n')   # "f" antes de uma string no Python indica que ela é uma string formatada, o que nos permite inserir valores de variáveis ou expressões dentro de uma string,sem precisar concatencaçãoi
    arqSaida.write(f'Número: {numero[i]} \n\n')
arqSaida.close()
