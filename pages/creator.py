#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__,path='/creator',title="Simulation Learning App",description="Simulation Learning App",image='logoweb1.png')

breadcrumb=dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/","color":"black","external_link": False},
                    {
                        "label": "More Information"
                    },
                    {"label": "About Creator", "active": True},
                ],
            ),
        )
    ),
fluid=True)

creator_layout = dbc.Container([
    dbc.Row([

            html.H1(html.B("Created By :",),style={'textAlign': 'center'})
        ])
    ,
    html.Div
( 
	[
		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('juliant1.png'), height="300px",width ="300px"),
				html.P("Juliant Galih Anjanu", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("118160080", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
        html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('winny1.png'), height="300px",width ="300px"),
				html.P("Winny Ouri Pakpahan", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160040", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
        html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('yola1.png'), height="300px",width ="300px"),
				html.P("Yolanda Dwi Putri Anzita", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160050", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
        		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('kiki1.png'), height="300px",width ="300px"),
				html.P("Rizkiyah Karomah", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160068", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
        		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('sarah2.png'), height="300px",width ="300px"),
				html.P("Callista Wynona Claudea", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160078", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
        		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('logo8.png'), height="300px",width ="300px"),
				html.P("Peniel Manoah Judea Hutagalung", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160092", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
    ]	
	, style={'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr', 'width':'99%','margin':'auto','justify-items':'center', 'margin-top':'2rem','gap':'3rem 0','margin-bottom':'3rem'}
),
    html.Div
( 
	
		html.Div
		( 
			[
				html.Img(src=dash.get_asset_url('agnes1.png'), height="300px",width ="300px"),
				html.P("Tri Nova Agnesia", style={'textAlign': 'center','margin':0,'margin-top':'1rem'}),
				html.P("119160110", style={'textAlign': 'center','margin':0})
			], style={'width':'fit-content','border': '2px solid orange', 'padding':'1rem'}
		),
		
	 style={'display': 'flex', 'justify-content':'center','margin-top':'2rem','padding-bottom':'2rem'}
)
],
fluid=True)

layout = html.Div([
    navigation.navbar,
    breadcrumb,
    creator_layout,
    #dl_content
    ]
)

# layout = html.Div(children=[
#     navigation.navbar,
#     breadcrumb,
#     html.H1(children="Created By :", style={'textAlign': 'center'}),
#     html.Img(src=dash.get_asset_url('logo1.png'), height="120px"),
#      #dcc.Link('Home',href="/"),
#      #html.Br(),
#      #dcc.Link('model-showcase',href="/showcase")
# ])
