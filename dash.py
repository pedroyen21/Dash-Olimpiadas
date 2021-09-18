
import plotly.express as px
import pandas as pd
dados_df = pd.read_excel("dados.xlsx") #leitura dos dados

##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total

medalhas = {}
atletas = {}

for i in range(len(dados_df.values)): 
    
    
    medalhas = {       
        'ouro' : dados_df['Ouro'][i],
        'prata' : dados_df['Prata'][i],
        'bronze' : dados_df['Bronze'][i]
    }
    atletas[dados_df['Atleta'][i].replace('\xa0', '')]= medalhas
camelo = px.data.medals_wide()
print(len(atletas))
print(medalhas['ouro'])
fig = px.bar(camelo, x=atletas.keys() ,y="ouro", title="Wide-Form Input")
fig.show()
    




    
