import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff

trace = go.Scatter(
	x=[1,2,3,4,5,6,7],
	y=[10,None,2,15,None,26,11],
        name = 'first',
        connectgaps = True
	)

trace1 = go.Scatter(
	x=[1,2,3,4,5,6,7],
	y=[5,10,None,7,None,14,6],
        name ='second'
	)

pltoff.plot([trace,trace1],filename='my scatter.html')
