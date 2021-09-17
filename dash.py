
import plotly.express as px
import pandas as pd
dados_df = pd.read_excel("dados.xlsx") #leitura dos dados

##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total

medalhas = []

for i in range(len(dados_df.values)):    
    atleta = { 
        'Nome':dados_df['Atleta'][i],
        'Ouro': dados_df['Ouro'][i],
        'Prata': dados_df['Prata'][i],
        'Bronze': dados_df['Bronze'][i]
    }
    medalhas.append(atleta)
print(medalhas)
    
