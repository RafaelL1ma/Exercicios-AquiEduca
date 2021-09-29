list = []
n = 1
while True:
    name = input(f"Funcionário {n}: ")
    n = n + 1

    list.append(name)

    if name == "0":
        list.remove('0')
        print("------Cadastro concluído------")
        print(list)
        break
