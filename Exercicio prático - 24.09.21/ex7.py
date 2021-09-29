print("---------------ADIÇÃO---------------")
while True:
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))

    result = n1 + n2

    print(f"{n1} + {n2} = {result}")

    confirm = input("deseja realizar mais uma soma? [S ou N] ")

    if confirm == "s" or confirm == "S":
        continue
    elif confirm == "n" or confirm == "N":
        print("Adeus!")
        break
