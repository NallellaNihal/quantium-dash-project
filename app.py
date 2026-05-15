from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Dash Task"),
    html.P("Dash environment configured successfully.")
])

if __name__ == "__main__":
    app.run(debug=True)
