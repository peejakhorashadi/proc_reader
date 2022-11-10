import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

INTERVAL_TIME = 2
X = deque(maxlen = 10)
X.append(1)

Y = deque(maxlen = 10)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
	[
		dcc.Graph(id = 'live-graph', animate = True),
		dcc.Interval(
			id = 'graph-update',
			interval = INTERVAL_TIME * 1000,
			n_intervals = 0
		),
	]
)


@app.callback(
	Output('live-graph', 'figure'),
	[ Input('graph-update', 'n_intervals') ]
)
def update_graph_scatter(n):
	X.append(X[-1]+ INTERVAL_TIME)
	Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))

	data = plotly.graph_objs.Scatter(
			x=list(X),
			y=list(Y),
			name='Scatter',
			mode= 'lines+markers'
	)

	return {'data': [data],
			'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
