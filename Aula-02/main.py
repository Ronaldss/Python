# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualisar a base de dados
#display(tabela)

# enterder quais informações estão disponíveis
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)


# Passo 3: Tratamento de dados
# - Valores que estão sendo reconhecidos de forma errada
#   Como a coluna "TotalGasto" estava sendo reconhecida como string, convertemos ela para números float.
#   tbm foi aumentado a quantidade de campos vazios, pois o (errors="coerce") elinima dados errados ou em branco
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# Deletando as colunas vazias 
tabela = tabela.dropna(how="all", axis=1)

# Delentando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela = tabela.info())



# Passo 4: Análise inicial
# - Como estao os nossos cancelamentos?
# - em valor inteiro
print(tabela["Churn"].value_counts())
# - em porcentagem .map
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))



# Passo 5: Anaálise mais complexa
# -  Comparar cada coluna da minha tabela com a coluna cancelameto
import plotly.express as px

# Criar o grafico
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    # Exibir o grafico
    grafico.show()