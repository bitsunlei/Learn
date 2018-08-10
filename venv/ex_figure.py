import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt


time_x = pd.date_range('09:00',periods=200,freq='4T')
t_list = list(time_x.hour)
fig, ax = plt.subplots(figsize=(16,10),)

tk_gap = range(0,200,40)
ticks  = ax.set_xticks(tk_gap)
# tlabel = ax.set_xticklabels(list(time_x[tk_gap].strftime('%H:%M')))
tlabel = ax.set_xticklabels(time_x[tk_gap].strftime('%H:%M'))

print('The End')