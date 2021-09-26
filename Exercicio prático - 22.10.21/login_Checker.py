while True:
    print("-------------------LOGIN-------------------")
    user_name = input("Informe o username: ")
    if user_name == "exit":
        break
    password = input("Informe a senha: ")

    if password != user_name:
        print("--------------------------------------")
        print("logado com sucesso")
        while True:
            print("--------------------------------------")
            exit = input("deseja sair?(s/n)")
            if exit == "s":
                print("Você saiu!")
                break
            else:
                print("Você continua logado!")
    else:
        print("--------------------------------------")
        print("Senha inválida")
