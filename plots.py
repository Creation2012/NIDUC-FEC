import pandas as pd
import plotly.express as px

def boxPlot():
    df = pd.read_csv('data.csv',delimiter=';')
    fig = px.box(df, x='send', y='errors')
    fig.show()


def histograms():
    df = pd.read_csv('data.csv',delimiter=';')
    fig = px.histogram(df, x='errors')
    fig.update_layout(bargap=0.2)
    fig.show()

def line():
    df = pd.read_csv('data.csv',delimiter=';')
    fig = px.line(df, x='errors',y='send')
    fig.show()

boxPlot()
histograms()
line()
