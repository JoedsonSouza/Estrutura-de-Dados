#x = 'danilo'
#sub='andrea'
#linha = 'hauhduadguagsuadanilo'
#for k in range(0,len(linha)):
#    aux = linha[k:k+len(x)]
#    if aux == x:
#        for i in range(k,k+len(x)):
#            linha[i] = sub[i-k]
#print(linha)
arqTxt = open('teste.txt', 'r')
L = []
for i in arqTxt:
    L.append(i)
for i in range(0, len(L)):
    aux = L[i]
    for j in range(0, len(aux)-):
        
