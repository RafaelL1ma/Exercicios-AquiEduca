i = 0
list = []
while i < 3:
    num = int(input("Informe um número inteiro: "))
    list.append(num)
    i = i + 1

print(f"O maior número é: {max(list)}")
print(f"O menor número é: {min(list)}")
