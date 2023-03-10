def selectionSort(lista):
    for i in range(0, len(lista) - 1):
        menor = lista[i]
        pMenor = i
        for j in range(i, len(lista)):
            if(lista[j] < menor):
               menor = lista[j]
               pMenor = j
        aux = lista[i]
        lista[i] = lista[pMenor]
        lista[pMenor] = aux

def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    # se a lista tiver mais de um elemento
    if inicio < fim:
        # partition divide a lista em duas sub-listas menores
        # o valor retornado em p é o índice do pivô
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quickSort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quickSort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    #inicio até fim-1
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise - linha roxa
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            # se o elemento atual for menor ou igual ao pivô, esse elemento deve ser trocado com o elemento da posição i, ficando à esquerda do Pivot.
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô - linha amarela que sempre avança quando um elemento é trocado de posição
            i = i + 1
    # no final do loop o pivô é colocado na posição correta, onde todos os elementos à esquerda são menores e os à direita são maiores que o pivô.
    lista[i], lista[fim] = lista[fim], lista[i]
    # retorna o índice do pivot
    return i

def buscaBinaria(lista, busca, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == busca:
            return meio
        if busca < lista[meio]:
            return buscaBinaria(lista, busca, inicio, meio-1)   # seleciono a sublista dos elementos à esquerda da metade - elementos menores que o elemento do meio.
        else:
            return buscaBinaria(lista, busca, meio+1, fim)
    return None

def arquivos(L):
    for i in range(0,4):
        fileName = input(f"Nome do {i+1}° arquivo: ")
        arquivo = open(fileName + '.txt', 'r')
        for j in arquivo:
            L.append(j.replace("\n",""))
        arquivo.close()
    print("")
    
def menu():
    print("MENU DE OPÇÕES")
    print("[1] - Busca Binária")
    print("[2] - Selection Sort")
    print("[3] - Quick Sort")
    print("")
def metodoOrdenacao():
    print("MÉTODO DE ORDENAÇÃO")
    print("[1] - Selection Sort")
    print("[2] - Quick Sort")
    print("")

# EXECUÇÃO #
print("SELECIONAR ARQUIVOS:")
L = []
arquivos(L)
menu()
opcao = int(input("Opção escolhida:"))

if opcao == 1:
    busca = input("Digite a palavra que procura: ")
    metodoOrdenacao()
    ordenar = int(input("Opção escolhida:"))
    if ordenar == 1:
        selectionSort(L)
    else:
        quickSort(L)
    x = buscaBinaria(L, busca)
    if x is None:
        print("Palavra não encontrada!")
    else:
        print(f"Palavra encontrada! Localizada na linha {x+1}")
elif opcao == 2:
    selectionSort(L)
    print("Dados ordenados com sucesso!")
else:
    quickSort(L)
    print("Dados ordenados com sucesso!")

dadosOrdenados = open('ordenados.txt', 'w')
for i in range(len(L)):
    dadosOrdenados.write(f'{L[i]}\n')
dadosOrdenados.close()


























    
