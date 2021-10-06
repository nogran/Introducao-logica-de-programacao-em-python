from typing import List
import pandas as pd
from time import sleep
from pandas.core.indexes.base import ensure_index
dfs = pd.read_excel("planilha.xlsx")

df = dfs['Categorias'].str.split(r',\s+')
lista_categorias = df.explode().unique().tolist()

nome = input("Seja bem vind@. Como gostaria de ser chamad@? \n")

sleep(1)

print("Que bom que nos procurou, tenho certeza que iremos encontrar os melhores cursos para voce.")

sleep(2)

print("Estou te enviando as categorias disponiveis em nossa escola.\n")

sleep(3)

for i in range(len(lista_categorias)):
    lista_numerada = (f"{i}. {lista_categorias[i]}")
    print(lista_numerada)
numero_das_categorias = input("Digite o numero dos assuntos de seu interesse (use virgulas): \n")

sleep(1)

tempo = input("Quanto tempo voce possui para estudar? (Minutos)\n")

sleep(1)

gratuidade = input("Mostrar apenas gratuitos (S/N)? \n")

sleep(2)
