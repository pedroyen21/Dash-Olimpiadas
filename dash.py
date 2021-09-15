import plotly.express as px
import numpy as np


nx = np.arange(start = 0, stop=100,step=.25)
grafico= px.line(x= nx, y= -np.cos(nx), height=400)
grafico.show()
