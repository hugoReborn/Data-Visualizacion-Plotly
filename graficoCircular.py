import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# creamos los datos con un arreglo de estudiantes
# creamos otro arreglo para las notas

stud = ['Hugo', 'Paco', 'Luis', 'Donald', 'Goofy', 'Speedy Gonzales']
marks = [4, 6, 5, 3, 2, 1]

# creamos el objeto figura , le indicamos que sera un
# grafico circular y le pasamos los datos y pull (separacion)

fig = go.Figure(data=[go.Pie(labels=stud, values=marks, pull=[0, 0, 0, 0, 1, 0])])

# realizamos un update para que el grafico se muestre
# donde indicamos que el texto debe estar dentro y debe mostrar el porcentaje y la etiqueta

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title='Estudiantes y Notas')
fig.show()



