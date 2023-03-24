
def insertionSort(L):
    for i in range(1, len(L)):
        j = 0
        while(L[i]>L[j]) and (j<i):
              j = j+1
        val = L.pop(i)
        L.insert(j, val)
    print(L)

L = []
for i in range(0, 10):
    x = input("Produto: ")
    L.append(x)
insertionSort(L)

removidos = []
for i in range(0, len(L)-1):
    if(L[i] == L[i+1]):
        L.pop(i)
        L.insert(i, '')

for i in range(0, len(L)):
    if(L[i] != ''):
        removidos.append(L[i])

for i in range(0, len(removidos)):
    print(removidos[i])
