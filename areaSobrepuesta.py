import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


stud = ['Hugo', 'Paco', 'Luis']

# creamos un objeto con go y el metodo figure
# esta vez no le pasamos ningun valor

fig = go.Figure()

# pasamos los valor a graficar

fig.add_trace(go.Scatter(x=stud, y=[40, 10, 20], hoverinfo='x+y', mode='lines', line=dict(width=0.6, color='rgb(172,89,200)'),
                         stackgroup='one'))

fig.add_trace(go.Scatter(x=stud, y=[50, 5, 2], hoverinfo='x+y', mode='lines', line=dict(width=0.6, color='rgb(100,51,190)'),
                         stackgroup='one'))

fig.show()