import pandas as pd

base = pd.read_csv("C:/Users/User/Downloads/para_teste.csv", sep=";")

print("Autorização de uso dos dados")
print(base["Autorizo a utilização dos dados das minhas respostas, desde que não sejam compartilhados meus dados pessoais. "].value_counts())