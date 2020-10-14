import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('agg')
# from fbprophet.plot import plot_plotly, plot_components_plotly
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot

paris = pd.read_csv("../Data/full_paris_emolex_modified.csv")
gnd = pd.read_csv("../Data/full_gnd_emolex_modified.csv")

paris["created_at"] = pd.to_datetime(paris["created_at"])
gnd["created_at"] = pd.to_datetime(gnd["created_at"])
paris["ds"] = paris["created_at"].dt.date
gnd["ds"] = gnd["created_at"].dt.date
paris["y"] = (paris["positive"] - paris["negative"])/2
gnd["y"] = (gnd["positive"] - gnd["negative"])/2

paris_prophet = Prophet()
gnd_prophet = Prophet()
paris_prophet.fit(paris)
gnd_prophet.fit(gnd)

fig = paris_prophet.plot(paris)
a = add_changepoints_to_plot(fig.gca(), paris_prophet, paris)

fig = gnd_prophet.plot(gnd)
a = add_changepoints_to_plot(fig.gca(), gnd_prophet, gnd)