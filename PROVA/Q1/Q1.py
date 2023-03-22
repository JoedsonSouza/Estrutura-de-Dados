def insertionSort(L):
    for i in range(1, len(L)):
        j = 0
        while(L[i]>L[j]) and (j<i):
              j = j+1
        val = L.pop(i)
        L.insert(j, val)
    print(L)

def quickSort(L, ini, fim):
    if(fim>ini):
        pivo = partition(L, ini, fim)
        quickSort(L, ini, pivo-1)
        quickSort(L, pivo+1, fim)

def partition(L, ini, fim):
    pivo = ini
    if fim > ini:
        for i in range(ini+1, fim+1):
            if(L[i]<L[pivo]):
                aux = L[i]
                L.pop(i)
                L.insert(pivo, aux)
                pivo = pivo+1
        return pivo

def linha(L, L1, x):
    for i in range(x, len(L), 4):
        L1.append(L[i])

nomeArquivo = input("Nome do arquivo:")
arquivo = open(nomeArquivo + '.txt', 'r')
L = []
nome = []
ouro = []
prata = []
bronze = []
for i in arquivo:
    L.append(i)
linha(L, nome, 0)
linha(L, ouro, 1)
linha(L, prata, 2)
linha(L, bronze, 3)

maiorOuro = ouro[0]
pMaiorOuro = 0
for i in range(0, len(L)):
    if ouro[i] > maiorOuro:
        maiorOuro = ouro[i]
        pMaiorOuro = i
print(maiorOuro)
print(pMaiorOuro)
