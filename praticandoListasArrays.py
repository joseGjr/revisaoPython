alunos = 8
medias = []

for i in range(1,alunos+1):
    notas = 0
    for j in range(1,5):
        notas += float(input("digite a nota%i de 4 notas do aluno %i aluno de %i"%(j,i,alunos)))
    notas /=4
    medias.append(notas)
num = 0
for media in medias:
    if media>=6 :
        num+=1
print("o numero de alunos com media maior que 6 é igual a :, ",num)