num = int(input("informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

pares = 0

while num <= num2:

    if num % 2 == 0:
        pares = pares + 1
    num = num + 1
print(pares)
