import plotly.express as px
import csv
import pandas as pd
import pathlib

path_income_csv = pathlib.Path(__file__).parent.parent / 'data/median_income.csv'
data_income = pd.read_csv(path_income_csv)

def make_hist(series, col):
    # Create Histogram
    fig = px.histogram(series, x=col, title=f'Histogram of {col}')
    fig.show()

if __name__ == '__main__':
    make_hist(data_income, 'med_income')