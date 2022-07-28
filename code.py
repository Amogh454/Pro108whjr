import plotly.figure_factory as ff
import pandas as pd
import csv 

dat = pd.read_csv('data.csv')


pl = ff.create_distplot([dat['AverageRating'].tolist()], ['Average'], show_hist=True)
pl.show()