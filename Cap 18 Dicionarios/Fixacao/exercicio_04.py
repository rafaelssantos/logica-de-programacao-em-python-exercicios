n = int(input("Número de alunos da turma: "))

alunos = [] # Lista de alunos

for e in range(n):
    aluno = {}
    aluno["Nome"] = input("Insira o nome do aluno: ")
    aluno["Nota 1"] = float(input("Insira a nota 1: "))
    aluno["Nota 2"] = float(input("Insira a nota 2: "))
    aluno["Nota 3"] = float(input("Insira a nota 3: "))
    alunos.append(aluno)

print("\nMÉDIAS")
for aluno in alunos:
    media = (aluno["Nota 1"] + aluno["Nota 2"] + aluno["Nota 3"]) / 3
    if media >= 7:
        print(aluno["Nome"], f"{media:0.2f}", "APROVADO")
    else:
        print(aluno["Nome"], f"{media:0.2f}", "REPROVADO")           
    