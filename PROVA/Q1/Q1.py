def insertionSort(L):
    for i in range(1, len(L)):
        j = 0
        while(L[i]>L[j]) and (j<i):
              j = j+1
        val = L.pop(i)
        L.insert(j, val)

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
ouro2 = []
prata = []
bronze = []

for i in arquivo:
    L.append(i)
linha(L, nome, 0)
qtdMedalhas(L, ouro, 1)
qtdMedalhas(L, ouro2, 1)
qtdMedalhas(L, prata, 2)
qtdMedalhas(L, bronze, 3)

maiorOuro = max(ouro)   #identifica qual o maior valor
pMaiorOuro = ouro.index(maiorOuro)  #verifica a posição do maior valor dentro da lista ouro.

Ordenado = []
nomeOrd = []
prataOrd = []
bronzeOrd = []

if ouro.count(maiorOuro) == 1:   #se o maior valor aparecer apenas 1 vez, já temos um campeão. Se não, é preciso utilizar outra forma de validar a vitória 
    insertionSort(ouro2)
    for i in range(0, len(ouro2)):
        pos = ouro.index(ouro2[i])   #verifica qual a posição do valor atual na lista original
        nomeOrd.append(nome[pos])   #adiciona o nome referente ao valor da medalha na nova lista ordenada
        prataOrd.append(prata[pos])
        bronzeOrd.append(bronze[pos])
else:
    #preciso verificar apenas dentre os valores emapatados em med de ouro, qual tem a maior qtd de medalhas de prata.
    
print(nomeOrd)
print(ouro2)
print(prataOrd)
print(bronzeOrd)

