v1 = float(input("Qual o valor da venda 1:"))
v2 = float(input("Qual o valor da venda 2:"))
v3 = float(input("Qual o valor da venda 3:"))
v4 = float(input("Qual o valor da venda 4:"))
v5 = float(input("Qual o valor da venda 5:"))

soma = v1 + v2 + v3 + v4 + v5
media = soma / 5

if media >= 1000:
    print("Bom desempenho, sua média foi:", media)
else:
    print("Desempenho abaixo da meta, sua média foi:", media)

