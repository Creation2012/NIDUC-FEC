import plotly.express as px

def boxPlot(self, data):
    fig = px.box(data)
    fig.show()


def histograms(self, data):
    fig = px.histogram(data)
    fig.update_layout(bargap=0.2)
    fig.show()
