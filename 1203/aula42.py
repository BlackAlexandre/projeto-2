contador_maiores = 0

for i in range(5):
    idade = int(input("Qual a idade: "))

    if idade >= 18:
        contador_maiores = contador_maiores +1

if contador_maiores >= 1:
    print("Temos", contador_maiores, "pessoas maiores de 18 anos")