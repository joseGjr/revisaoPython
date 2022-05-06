'''funções multiplas'
def soma(*lista):
    soma_num =0
    print(lista)

    for num in lista:
        soma_num += num

    return soma_num

a = (1,2,3,4)
print(soma(1,2,3,4))
'''

x = 10
def incremetna():
    global x
    incremetna = 5
    x+= incremetna
incremetna()
print(x)
