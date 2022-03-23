import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
Avg = df['Avg Rating'].tolist()

fig = ff.create_distplot([Avg] , ['Average Rating Of Brands'] , show_hist = False)
fig.show()