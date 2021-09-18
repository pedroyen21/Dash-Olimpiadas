
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
print(atletas.keys())
 
#fig = px.bar(atletas, x=atletas.keys(), y=["atletas['ouro']", "atletas['prata']", "atletas['bronze']"], title="Wide-Form Input")
#fig.show()
    




    
