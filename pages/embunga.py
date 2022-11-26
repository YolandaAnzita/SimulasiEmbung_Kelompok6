#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__,path='/embunga',title="Simulation Learning App",description="Simulation Learning App",image='logoweb1.png')

breadcrumb=dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/","color":"black","external_link": False},
                    {
                        "label": "Profil"
                    },
                    {"label": "Embung A", "active": True},
                ],
            ),
        )
    ),
fluid=True)

header_embunga_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(html.B("Profil Embung A"),style={'textAlign': 'center','font-size':'3em'})
        ])
    ]),
    html.P('''Luas : 1,95 Ha''',style ={'margin':0, 'textAlign': 'center','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em','font-weight':'bold'}),
    html.P('''Volume : 48,750 m³''',style ={'margin':0,'textAlign': 'center','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em','font-weight':'bold'}),
],
fluid=True)

creator_layout = dbc.Container([
    html.Div
( 
	[
		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('embunga3.jpeg'), height="500px",width ="500px"),
			], style={'width':'fit-content','border': '2px solid black', 'padding':'1rem'}
		),
        html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('embunga2.jpeg'), height="500px",width ="500px"),
			], style={'width':'fit-content','border': '2px solid black', 'padding':'1rem'}
		),
    ]	
	, style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'width':'99%','margin':'auto','justify-items':'center', 'margin-top':'2rem','gap':'3rem 0','margin-bottom':'3rem'}
)
])

definisi_embung_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(html.B("Definisi Embung"),style={'textAlign': 'center','font-size':'3em','margin-top':'4rem'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.P('''Embung adalah bangunan penyimpanan air yang dibangun di daerah dekat sungai. Biasanya digunakan untuk menampung air hujan agar dapat dimanfaatkan oleh masyarakat sekitar ketika musim kemarau.''')
        ],style={'textAlign': 'center','margin-top':'2rem','margin-left':'25vw','margin-right':'25vw','font-size':'1.5em'}
        )
    ]),
])

layout = html.Div([
    navigation.navbar,
    breadcrumb,
    header_embunga_content,
    creator_layout,
    definisi_embung_content
    ],style = {'background-image': 'url(../assets/backgroundimageweb1.jpeg)','background-size':'cover','height': '170vh'}

)