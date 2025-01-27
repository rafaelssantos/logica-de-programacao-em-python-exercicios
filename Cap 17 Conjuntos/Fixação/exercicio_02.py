n_basquete = int(input("Informe o número de estudantes que praticam basquete: "))
estudantes_basquete = set()

for e in range(n_basquete):
    estudante = input("Informe o nome do próximo aluno que pratica basquete: ")
    estudantes_basquete.add(estudante)



n_atletismo = int(input("Informe o número de estudantes que praticam atletismo: "))
estudantes_atletismo = set()

for e in range(n_atletismo):
    estudante = input("Informe o nome do próximo aluno que pratica basquete: ")
    estudantes_atletismo.add(estudante)

estudantes_ambos_os_esportes = estudantes_atletismo & estudantes_basquete

print("Estudantes que praticam ambos os esportes:")
print(estudantes_ambos_os_esportes)