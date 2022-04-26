from random import seed, randrange
import matplotlib.pyplot as plt

seed(11)
randrange(0,11)

notas_aluno = []

for notas in range(8):
    notas_aluno.append(randrange(0,11))

x = list(range(1, 9))
y = notas_aluno
plt.plot(x, y, marker='o')
plt.title('Notas de alunos')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
