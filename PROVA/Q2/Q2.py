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

pares = []
impares = []
for i in range(0, 10):
    x = int(input("Número: "))
    if(x % 2 == 0):
        pares.append(x)
    else:
        impares.append(x)
quickSort(pares, 0, len(pares)-1)
quickSort(impares, 0, len(impares)-1)
impares.reverse()
L = []
for i in range(0, len(pares)):
    print(pares[i])
for i in range(0, len(impares)):
    print(impares[i])
