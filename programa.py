from typing import List
import pandas as pd
dfs = pd.read_excel("planilha.xlsx")


df = dfs['Categorias'].str.split(r',\s+')
lista_categorias = df.explode().unique().tolist()


print(lista_categorias)



#nome = input("Digite seu nome: \n")
#print(f"Seja bem vindo {nome}")