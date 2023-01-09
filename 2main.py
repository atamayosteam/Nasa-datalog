import pandas as pd
import matplotlib.pyplot as plt

Nasa_file = open('NASA_access_log_Jul95')

plt.style.use("seaborn-dark")

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey


dates= []

colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41', # matrix green
]

try:
    for lines in Nasa_file:
        date = lines.split(' ')[3]
        date = date.split(':')[0]
        date=  date.split('[')[1]
        date = date.split('/1995')[0]
        dates.append(date)
except UnicodeDecodeError:
    print('uhoh')

    


plt.show()
