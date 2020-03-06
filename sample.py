
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background':'gray',
    'text':'#003320',
}

app.layout = html.Div(children=[
    html.H1(
            children='Hello Dash',
            style={
                'textAlign':'center',
                'color':colors['text'],
                'background-color':colors['background'],
            } 
    ),

    html.Div(
        children='''
            Dash: A web application framework for Python.
        ''',
        style={
            'textAlign':'center',
            'color':colors['text'],
            'background-color':colors['background'],
        }
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':colors['text'],
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
