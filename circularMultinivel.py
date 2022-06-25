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
# no se pueden poner comillas simples y repetir , luego debemos usar comillas dobles


stud = ['Hugo', 'Paco', 'Luis', 'Donald', 'Goofy', 'Speedy Gonzales']
teachers = ["Juan", "hola", "Maria", "Jose", "Juan", "antonio"]
marks = [4, 6, 5, 3, 2, 1, 7]

fig = go.Figure(go.Sunburst(labels=stud, parents=teachers, values=marks))
fig.update_layout(margin=dict(t=1, l=1, r=1, b=1))

fig.show()
