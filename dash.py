
import plotly.express as px

import pandas as pd

dados_df = pd.read_excel("dados.xlsx") #leitura dos dados

##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total

atletas = dados_df['Atleta']
medalhas = {}

pd.options.display.max_rows=1000
#print(int(dados_df['Ouro'][0]))

print(dados_df[['Ouro','Prata','Bronze']])

#for i in dados_df.values:
 #   medalhas

