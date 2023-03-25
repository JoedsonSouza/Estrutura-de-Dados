def insertionSort(L, L2, L3, L4):
    for i in range(1, len(L)):
        j = 0
        while(L[i]>L[j]) and (j<i):
              j = j+1
        val = L.pop(i)
        val2 = L2.pop(i)
        val3 = L3.pop(i)
        val4 = L4.pop(i)
        L.insert(j, val)
        L2.insert(j, val2)
        L3.insert(j, val3)
        L4.insert(j, val4)

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
def qtdMedalhas(L, L1, x):
    for i in range(x, len(L), 4):
        L1.append(int(L[i]))

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
qtdMedalhas(L, ouro, 1)
qtdMedalhas(L, prata, 2)
qtdMedalhas(L, bronze, 3)

maiorOuro = max(ouro)   #identifica qual o maior valor
pMaiorOuro = ouro.index(maiorOuro)  #verifica a posição do maior valor dentro da lista ouro.

if ouro.count(maiorOuro) == 1:   #se o maior valor aparecer apenas 1 vez, já temos um campeão. Se não, é preciso utilizar outra forma de validar a vitória 
    insertionSort(ouro, nome, prata, bronze)
print(nome)
print(ouro)
print(prata)
print(bronze)
