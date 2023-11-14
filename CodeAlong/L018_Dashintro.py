from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

my_H1 = html.H1(children='My dash application')
my_H2 = html.H2(children='More info...')
my_dropdown = dcc.Dropdown(options=['Äpple','Päron','Apelsin'], value='Päron')
app.layout = html.Div(children = [my_H1,my_H2,my_dropdown])

app.run(debug=True)