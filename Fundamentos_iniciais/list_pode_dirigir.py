idades = [18,15,25,73,46,25,13,10]
permissoes =[]

def pode_dirigir():
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
            print(f"{idade} Anos! Você pode dirigir!")
        else:
            permissoes.append(False)
            print(f"{idade} Anos! Você não pode dirigir!")

pode_dirigir()

print(permissoes)