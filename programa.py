import pandas as pd
from time import sleep


#   Import an excel file and convert it in lists
df = pd.read_excel("planilha.xlsx")

col_cursos = df['Nome do curso']
lista_cursos = col_cursos.tolist()

col_duracao = df['Duração (min)']
lista_duracao = col_duracao.tolist()

col_categorias = df['Categorias']
lista_categorias = df['Categorias'].str.split(',').tolist()

col_gratuidade = df['Gratuito']
lista_gratuidade = col_gratuidade.tolist()

#   To convert type string from list values (if necessary)



#   To show unique value of Categorias to user
col_categorias = df['Categorias'].str.split(r',\s+')
unique_lista_categorias = col_categorias.explode().unique().tolist()


#   Username input
nome = input("Seja bem vind@. Como gostaria de ser chamad@? \n")
sleep(1)
print("Que bom que nos procurou, tenho certeza que iremos encontrar os melhores cursos para voce.")
sleep(2)
print("Estou te enviando as categorias disponiveis em nossa escola.\n")
sleep(3)


#   To show a number to each category (it helps user input)
for i in range(len(unique_lista_categorias)):
    lista_numerada = (f"{i}. {unique_lista_categorias[i]}")
    print(lista_numerada)


#   User inputs
numero_das_categorias = input("Digite o numero dos assuntos de seu interesse (use virgulas): \n")
tempo = float(input("Quanto tempo voce possui para estudar? (min)\n"))
gratuidade = input("Mostrar apenas gratuitos?(S/N)\n")


#   Rules to user input
if gratuidade == "N" or gratuidade == "n":
    gratuidade = False
elif gratuidade == "S" or gratuidade == "s":
    gratuidade = True
elif gratuidade != "S" or "N":
    print(nome +" ,nao entendi sua resposta, por favor digite 'S' para cursos gratuitos e 'N' para cursos com mensalidade. /n")


#   To convert values from Gratuidade to True or False




#   Convert user input string to integer list
numero_das_categorias = numero_das_categorias.split(",")
n_user_categorias = []

for x in numero_das_categorias:
    lista_numerada = int(x.strip())
    n_user_categorias.append(lista_numerada)


#   Input type test
print(f"Nome: {nome}")
print(f"User id categorias: {n_user_categorias}")
print(f"Tempo: {tempo}")
print(f"Gratuidade: {gratuidade}")

print(type(nome))
print(type(n_user_categorias))
print(type(tempo))
print(type(gratuidade))


