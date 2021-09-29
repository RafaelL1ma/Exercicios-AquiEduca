num = int(input("informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
pares = []
soma = 0
while num <= num2:
    if num % 2 == 0:
        pares.append(num)
    num = num + 1

for par in pares:
    soma += par

print(f"A soma dos números pares é {soma}")
