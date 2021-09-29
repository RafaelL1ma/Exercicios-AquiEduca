age = int(input("Informe sua idade: "))

if age >= 16 and age < 18:
    print("Voto opcional!")

elif age >= 18 and age <= 70:
    print("Voto obrigatório!")
elif age > 70:
    print("Voto opcional!")
else:
    print("Voto inválido!")
