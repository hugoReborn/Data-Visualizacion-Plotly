import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go



# crear un plot multi-lineal

# creamos un arreglo con estudiantes
stud = ['donald', 'hugo', 'paco', 'luis']

# creamos un arreglo con las notas de unas materias
math = [4, 5, 2, 7]
science = [5, 3, 7, 6]
english = [4, 7, 6, 5]
administration = [5, 4, 6, 7]

# creamos un objeto figura con el metodo go y la funcion Figure

fig = go.Figure()

# creamos un estilo para los plots del grafico
# al objeto , le agregamos el metodo add_trace , que es agregar un plot
# le pasamos go y el metodo scatter como parametros y  las cordenadas
# al eje x le pasamos los estudiantes y al eje y las materia con un verbose name
# agregamos la linea del plot y un color a esta
# agregamos un grosor con width , este es el grosor de la linea del plot
# con dash cambiamos el tipo de plot , el tipo de linea a usar


fig.add_trace(go.Scatter(x=stud, y=math, name="Maths marks", line=dict(color="blue", width=4)))
fig.add_trace(go.Scatter(x=stud, y=science, name="Science marks", line=dict(color="red", dash="dashdot")))
fig.add_trace(go.Scatter(x=stud, y=english, name="English marks", line=dict(color="green", dash= "dot")))
fig.add_trace(go.Scatter(x=stud, y=administration, name="Administration marks", line=dict(color="firebrick", dash= "dash")))

# realizamos un update a nuestra figura
# le damos un titulo a nuestro nuevo plot
# le damos un titulo a eje x y al eje y


fig.update_layout(title='Marks of Students', xaxis_title='Students', yaxis_title='Marks')

# mostramos nuestra figura con metodo show

fig.show()