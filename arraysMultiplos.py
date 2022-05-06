"""""
cesta = ["banana","pera",["maca","abacaxi"]]

#for i in range(4):
print(len(cesta))
"""
lista = []
num = int(input("digite um valor:  "))

while num != -1:
    lista.append(num)
    num = int(input("digite um valor: "))

elemento = int(input("quantas vezes digitei o numero 5: "))
cont = 0
for i in range(len(lista)):
    if lista [i]== elemento:
        cont+= 1
print("o elemento", elemento,cont)