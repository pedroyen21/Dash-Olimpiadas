
import plotly.express as px
import numpy as np
import pandas as pd

dados_df = pd.read_excel(r"dados.xlsx")

for cells in dados_df.values:
    print(cells[1])
##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total



