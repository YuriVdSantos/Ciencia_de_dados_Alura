idades = [18,25,13,45,10]

def verf_pode_dirigir():
    idade = int(input("Por favor, digite sua idade: "))
    if int(idade) >= 18:
        print("Você pode dirigir!")
    else:
        print("Você não pode dirigir!")


for idade in idades:
    verf_pode_dirigir(idades)