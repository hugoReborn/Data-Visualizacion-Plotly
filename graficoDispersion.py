import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plotly
from datetime import datetime, timedelta
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# cargamos un dataframe
iris = sns.load_dataset("iris")
# mostramos el dataframe
# print(iris.head)
# creamos una figura , le pasamos el dataframe y los ejes x,y

fig = px.scatter(iris, x="petal_length", y="petal_width", color="species",
                 size="sepal_width", hover_data=['sepal_length'], title="Iris Scatter Plot")
# mostramos la figura
fig.show()