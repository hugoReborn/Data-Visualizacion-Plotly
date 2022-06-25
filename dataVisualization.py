import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# creamos una linea simple de graficos
#creamos un dataframecon pandas

df = pd.DataFrame({"Years at Work": [1, 2, 3, 4], "income": [6500, 10000, 12000, 14000]})
print(df.head())


#   Years at Work  income
# 0              1    6500
# 1              2   10000
# 2              3   12000
# 3              4   14000

#generamos un simple dataframe con dos columnas y sus datos
# creamos un objeto fig con plotly express
# asignamos a los ejes partes del diccionario
# le damos un titulo
# le asignamos la funcion show al objeto creado

fig = px.line(df, x="Years at Work", y="income", title="Ingreso Anual") # mensionamos nuestro dataframe y los ejes para graficar y un titulo
fig.show()

# crear un plot multi-lineal

# creamos un arreglo con estudiantes
stud = ['donald', 'hugo', 'paco', 'luis']

# creamos un arreglo con las notas de unas materias
math = [4, 5, 2, 7]
science = [5, 3, 7, 6]
english = [4, 7, 6, 5]
administration = [5, 4, 6, 7]







