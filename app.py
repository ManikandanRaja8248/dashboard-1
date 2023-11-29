import dash
from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
from datetime import datetime
from dash_extensions import WebSocket
import circular_progress_bar
import socket

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./dataset").resolve()

service_history = pd.read_csv(DATA_PATH.joinpath("service_history.csv"))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width-device-width, initial-scale=1.0'}]
                )
app.title = "Maruti Suzuki"

bolt = 0
dev_status = False
activity_status = False
activity_duration = 0
is_success = False
# service_history=pd.read_csv("service_history.csv")


def service_history_table(dataframe, max_rows=len(service_history) + 1):
    return html.Div([
        html.Table(
        # Header
        [html.Tr([html.Th(col, className="table-head") for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ], className="table-data") for i in range(min(len(dataframe), max_rows))]
    )


def bolt_fixed(bolt):
    if bolt == 1:
        return html.Div([
            html.Img(src="/assets/bolts/1_active_bolt.png",height=100),
            html.Div(f'{bolt} out of 4',style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])
    elif bolt == 2:
        return html.Div([
            html.Img(src="/assets/bolts/2_active_bolts.png",height=100),
             html.Div(f'{bolt} out of 4',style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])
    elif bolt == 3:
        return html.Div([
            html.Img(src="/assets/bolts/3_active_bolts.png",height=100),
            html.Div(f'{bolt} out of 4',style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])
    elif bolt == 4:
        return html.Div([
            html.Img(src="/assets/bolts/4_active_bolts.png",height=100),
             html.Div(f'{bolt} out of 4',style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])
    else:
        return html.Div([
            html.Img(src="/assets/bolts/4-disactive-bolts.png",height=100),
             html.Div(f'{bolt} out of 4',style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])


def device_status(status):
    if status:
        return html.Div([
            html.Img(src="/assets/device/connected.png",height=100),
             html.Div("Connected",style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
        ])
    else:
         return html.Div([
            html.Img(src="/assets/device/disconnected.png",height=100),
             html.Div("Disconnected",style={"color":"red",
                                           "margin-top":'0.5rem'})
        ])
        

def display_duration(seconds):
    global activity_duration

    if dev_status:
        activity_duration += 1
    m, s = divmod(activity_duration, 60)
    return f'{m:02d}:{s:02d}'

def display_efficiency(efficiency):
    return f'{efficiency} %'
    
    
        


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width-device-width, initial-scale=1.0'}]
                )


# service_history=html.Div([
#     html.Table([
#         html.Tr([
#             html.Th("Date"),
#             html.Th("Time"),
#             html.Th("Efficiency"),

#         ],className="table-head"),
#              html.Tr([
#              html.Td("Date"),
#              html.Td("Time"),
#              html.Td("Efficiency"),
#         ])

#     ])
# ],className="service-history-table-content")

app.layout = dbc.Container([
    html.Div([
        html.Img(src="/assets/logo/maruti_suzuki.png", height=30),
        html.Img(src="/assets/logo/vicara.png", height=30)
    ], className="top-bar"
    ),
    dbc.Row([
        dbc.Col([
            html.Div([html.H3("Activity Status")], className="text-center"),
            html.Div(html.Img(src="/assets/logo/Torquing.gif",
                     height=450, ), className="torquing"),
            dbc.Row([
                dbc.Col([
                    html.Div("Server", className="tool-name"),
                    html.Img(src="/assets/logo/server.png", height=100),
                    html.Div("Connected")], className="text-center"),
                dbc.Col([
                    html.Div("Device", className="tool-name"),
                    # html.Img(src="/assets/logo/divice.png", height=100),
                    # html.Div("Connected"),
                   device_status(False)

                    ],className="text-center"),
                dbc.Col([
                    html.Div("Bolts Fixed", className="tool-name"),
                    # html.Img(src="/assets/logo/bolt.png", height=150)
                     bolt_fixed(0)
                    ], className="text-center"),
                dbc.Col([
                    html.Div("Durations", className="tool-name"),
                    html.Img(src="/assets/logo/duration.png", height=100),
                    html.Div(display_duration(100),style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
                    ], className="text-center"),
                dbc.Col([
                    html.Div("Efficiency", className="tool-name"),
                    html.Img(src="/assets/logo/efficiency.png", height=100),
                    html.Div(display_efficiency(75),style={"color":"#00539E",
                                           "margin-top":'0.5rem'})
                    ], className="text-center")
            ]),
        ], className="first-column "),
        dbc.Col([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/logo/person.png", height=100,
                                 ),
                        html.Div("Age : 45", className=" text-center")
                    ], width={"size": 2}),

                    dbc.Col([
                        dbc.Row([
                            dbc.Col([
                                html.Div("Name", className="emp-lable"),
                                html.Div(
                                    "jeni", className="emp-data emp-lable")
                            ]),
                            dbc.Col([
                                html.Div("Service Center",
                                         className="emp-lable"),
                                html.Div(
                                    "PASCO", className="emp-data emp-lable")
                            ]),
                            dbc.Col([
                                html.Div("Expriance", className="emp-lable"),
                                html.Div(
                                    "10 years", className="emp-data emp-lable")
                            ])
                        ]),

                        dbc.Row([
                            dbc.Row(
                                dbc.Col(html.Div("Training Completed",
                                        className="emp-lable"))
                            ),
                            dbc.Col(html.Div("SSQS level 1",
                                    className="emp-data emp-lable")),
                            dbc.Col(html.Div("SSQS Bronze",
                                    className="emp-data emp-lable")),
                            dbc.Col(html.Div("Nexa Training",
                                    className="emp-data "))
                        ]),
                    ],
                    )
                ])
            ], className="emp-details"),
            html.Div([

                dbc.Row([
                    dbc.Row(
                        dbc.Col(html.Div("Suggested Training", className="emp-lable"))),
                    dbc.Col(html.Div("SSQS Silver",
                            className="emp-data emp-lable")),
                    dbc.Col(html.Div("SSQS Gold", className="emp-data emp-lable")),
                    dbc.Col(html.Div("Nexa Platinum",
                            className="emp-data emp-lable"))
                ])

            ]),
            dbc.Row([
                dbc.Row([
                    dbc.Col(html.Div("Service History", className="emp-lable")),
                    html.Div(service_history_table(service_history),
                             className="service-history")


                ]),
            ])
        ], className="second-column")
    ], className="content-container"),



], fluid=True, )
if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True, host="0.0.0.0")

# host="0.0.0.0"