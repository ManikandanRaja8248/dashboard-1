from logging import debug
import dash
from dash import dcc, html
app = dash.Dash()
app.layout = html.Div([
    html.Img(src="/assets/logo/duration.png", height=100,
             className="gif-img", style={"position": "relative"}),
    html.Div("00.45", className="duration", style={"position": "absolute",
                                                   "left": "0",
                                                  " right": "0",
                                                   "margin-left": "auto",
                                                   "margin-right": "auto",
                                                  " width":" 100px",
                                                   })
])

app.run_server(debug=True)
