n = int(input("digite o numero de elementos da lista: "))
lista=[]
listaFilter = []


for i in range(n):
    elemento = int(input("digite o elemento %i de %i: " %(i+1,n)))
    lista.append(elemento)
    listaFilter.append(elemento)
print(lista)

for ele in listaFilter:
    aparicoes = lista.count(ele)
    for i in range (aparicoes-1):
        lista.remove(ele)
print(lista)
