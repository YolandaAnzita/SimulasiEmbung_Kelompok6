#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__,path='/introduction',title="Simulation Learning App",description="Simulation Learning App",image='logoweb1.png')

breadcrumb=dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/","color":"black","external_link": False},
                    
                    {"label": "Introduction", "active": True},
                ],
            ),
        )
    ),
fluid=True)

header_introduction_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(html.B("Introduction of Simulation Learning App"),style={'textAlign': 'center','font-size':'3em'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.P('''Simulation Learning App adalah aplikasi sederhana yang digunakan untuk pembelajaran dalam melakukan simulasi dengan berbagai data tertentu, yang nantinya simulasi tersebut dapat bermanfaat dalam banyak hal, seperti melakukan analisa suatu kejadian, prediksi, dan lain sebagainya.''')
        ],style={'textAlign': 'center','margin-top':'2rem','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em'}
        )
    ]),
],
fluid=True)

body_introduction_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(html.B("Thanks to..."),style={'textAlign': 'center','font-size':'3em','margin-top':'4rem'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.P(html.B('''Bapak Dr. Rifky Fauzi, S.Si., M.Si.'''))
        ],style={'textAlign': 'center','margin-top':'2rem','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em'}
        )
    ]),
    html.P('''Selaku Dosen Pengampu Mata Kuliah''',style ={'margin':0, 'textAlign': 'center','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em'}),
    html.P('''"Kapita Selekta Matematika Komputasi"''',style ={'margin':0,'textAlign': 'center','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em'}),
        
], fluid=True )

layout = html.Div([
    navigation.navbar,
    breadcrumb,
    header_introduction_content,
    body_introduction_content
    ],style = {'background-image': 'url(../assets/backgroundimageweb1.jpeg)','background-size':'cover','height': '100vh'}
)