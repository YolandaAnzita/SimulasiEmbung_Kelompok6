#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash

dash.register_page(__name__,path='/',title="Simulation Learning App",description="Simulation Learning App",image='logoweb1.png')

layout = html.Div(children=[
    navigation.navbar,
    html.H1(children="Welcome to Simulation Learning App!", style={'textAlign': 'center','margin-top':'40vh','font-size':'4.5em',"color":"orange"}),
     #dcc.Link('Home',href="/"),
     #html.Br(),
     #dcc.Link('model-showcase',href="/showcase")
], style = {'background-image': 'url(../assets/backgroundimageweb1.jpeg)','background-size':'cover','height': '100vh'}
)