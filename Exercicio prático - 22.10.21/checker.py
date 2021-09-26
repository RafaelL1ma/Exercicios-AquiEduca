while True:
    print("--------------------------------------")
    letter = input("Informe a letra: ")

    if letter == "f":
        print("--------------------------------------")
        print("O sexo informado é Feminino")
        print("Caso queira sair digite exit")

    elif letter == "F":
        print("--------------------------------------")
        print("O sexo informado é Feminino")
        print("Caso queira sair digite Exit")

    elif letter == "m":
        print("--------------------------------------")
        print("O sexo informado é Masculino")
        print("Caso queira sair digite Exit")

    elif letter == "M":
        print("--------------------------------------")
        print("O sexo informado é Masculino")
        print("Caso queira sair digite Exit")
    elif letter == "exit":
        break
    else:
        print("--------------------------------------")
        print("Sexo inválido")
