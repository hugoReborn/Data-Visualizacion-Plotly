import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# cargamos un dataframe con pandas

df = sns.load_dataset('titanic')

# mostramos la informacion imprimiendo sus cabeceras

#print(df.head())

# comenzar a crear un plot de barras con plotly
# un bar plot muestra la relacion entre un valor y una categoria
# cada entidad de las categorias representa una barra y su tamaño represenya el valor

# creamos un objeto fig con plotly express
# al objeto le pasamos la funcion bar
# como parametros a la funcion bar le pasamos el dataframe df  un eje x y un eje y
# le pasamos un titulo
# le damos un color
# mostramos el plot  de la figura con show

fig = px.bar(df, x='pclass', y='fare', color='sex', title='Bar Plot de Pasajero por Tarifa y Genero')
fig.show()

# lo que se muestra en el grafico de barras es el pago total por clase pintado de un color para las mujeres
# y otro color para los hombres dependiendo de la clase de pasajeros , ademas de la cantidad del pago
# de cada uno de ellos

