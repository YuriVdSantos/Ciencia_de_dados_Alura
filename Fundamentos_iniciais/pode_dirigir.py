def verf_pode_dirigir():
    idade = int(input("Por favor, digite sua idade: "))
    if int(idade) >= 18:
        print("Você pode dirigir!")
    else:
        print("Você não pode dirigir!")
verf_pode_dirigir()