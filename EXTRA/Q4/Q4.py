fileName = input("Nome do arquivo: ")
arqTxt = open(fileName + '.txt', 'r')
char = input("Digite o carácter: ")
L = []
x = 0
for i in arqTxt:
    L.append(i)
for i in range(0, len(L)):
    aux = L[i]
    for j in aux:
        if j == char:
            x += 1
print("'" +char+ "' aparece ", x, " vez(es) dentro do arquivo.")
