import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = sns.load_dataset('titanic')

# creamos un objeto usando la funcion px de plotlyexpress y la funcion area
# le pasamos el data frame que creamos
# entregamos eje x y eje y
# pintaremos este grafico con la cantidad de personas que
# sobrevivieron a la tragedia
# le pasamos a su vez un titulo

fig = px.area(df, x='sex', y='age', color='survived', title="Grafico de Area de Pasajeros por su Estado, Genero y Edad")
fig.show()

# grafico sobrepuesto

# creamos un arreglo

stud = ['Hugo', 'Paco', 'Luis']

# creamos un objeto con go y el metodo figure
# esta vez no le pasamos ningun valor

fig = go.Figure()

# pasamos los valor a graficar

fig.add_trace(go.Scatter(x=stud, y=[40, 10,20], hoverinfo='x+y', mode='lines',line=dict(width=0.2, color='rgb(172,89,200)'),
                         stackgroup='one'))

fig.add_trace(go.Scatter(x=stud, y=[50, 5, 2], hoverinfo='x+y', mode='lines',line=dict(width=2, color='rgb(100,51,190)'),
                         stackgroup='one'))


