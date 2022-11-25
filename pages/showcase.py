#import semua modules
import numpy as np
import dash
from dash import dcc, html, Output, Input, State
from flask import Flask
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from apps import navigation
# from main import *

#inisiasi aplikasi
dash.register_page(__name__,path='/showcase',title="Simulation Learning App",description="Simulation Learning App",image='logoweb1.png')

breadcrumb=dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": False},
                    
                    {"label": "Model Showcase", "active": True},
                ],
            )
        )
    ),
fluid=True)

# breadcrumb=html.Div(
#             [
#                 dbc.Container(
#                     dbc.Row(
#         dbc.Col(
#             dbc.Breadcrumb(
#                 items=[
#                     {"label": "Home", "href": "/", "external_link": False},
                    
#                     {"label": "Model Showcase", "active": True},
#                 ],
#             )
#         )
#     ),
#                 )
#             ],
#             style={'margin-left':2}
#         ), 
#membaca file
sheet_inflow = "inflow"
sheet_outflow = "outflow"
url_inflow = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSmp955buqdNrFeoe1MH7EN7MejOApf-MYfBXRTqMAxeunt7-GTBSUZjgYJk5LKuNzs9p3sESQ2BImZ/pub?output=csv"
url_outflow = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQU9YHUTgklL40taF1dLIkJphXJhvB_S36UZ629jypOd_ErOxMNnI8YlCeodvGRR5QvO4HwYmnOLa0a/pub?output=csv"
df_inflow = pd.read_csv(url_inflow)
df_outflow = pd.read_csv(url_outflow)


#membangun komponen
header = html.H1("Aplikasi Simulasi Kapasitas Embung A", style={'textAlign': 'center'})
subtitle = html.H2("MK Kapita Selekta Matematika Komputasi (MA4103)", style={'textAlign': 'center'})
anggota_list = html.Div(
    [
        html.P("Kelompok 6 :", style={'margin':0, 'font-size':'20px', 'font-weight':'bold'}),
        html.P("Juliant Galih Anjanu 118160080",style={'margin':0}),
        html.P("Winny Ouri Pakpahan 119160040",style={'margin':0}),
        html.P("Yolanda Dwi Putri Anzita 119160050",style={'margin':0}),
        html.P("Rizkiyah Karomah 119160068",style={'margin':0}),
        html.P("Callista Wynona Claudea 119160078",style={'margin':0}),
        html.P("Peniel Manoah Judea Hutagalung 119160092",style={'margin':0}),
        html.P("Tri Nova Agnesia 119160110",style={'margin':0})
    ], style={'textAlign':'center'}
)
    

inflow_fig = go.FigureWidget()
inflow_fig.add_scatter(name='Inflow', x=df_inflow['Waktu'], y=df_inflow['Data'])
inflow_fig.layout.title = 'Inflow'

outflow_fig = go.FigureWidget()
outflow_fig.add_scatter(name='Outflow', x=df_outflow['Waktu'], y=df_outflow['Data'])
outflow_fig.layout.title = 'Outflow'

simulation_fig = go.FigureWidget()
# simulation_fig.add_scatter(name='Outflow', x=df_outflow['Bulan'], y=df_outflow['Data'])
simulation_fig.layout.title = 'Simulation'


#layout aplikasi
layout = html.Div(
    [
        navigation.navbar,
        
            # navigation.navbar,
            breadcrumb,
            header,
            subtitle,
            # anggota_list
            
        
        html.Div(
            [
                dcc.Graph(figure=inflow_fig), 
                dcc.Graph(figure=outflow_fig)
            ]
            # style = {"display": "grid",  "grid-template-columns": "1fr 1fr"}
        ), 
         
                #  dcc.Graph(figure=inflow_fig), 
                #  dcc.Graph(figure=outflow_fig)
         
         html.Div(
            [
                html.Button('Run', id='run-button', n_clicks=0)
            ],
            style = {'textAlign': 'center'}
        ), 
        html.Div(id='output-container-button', children='Klik run untuk menjalankan simulasi.', style = {'textAlign': 'center'}),
        
                dbc.Col([dcc.Graph(id='simulation-result', figure=simulation_fig)])
            
            
    ]
)
#interaksi aplikasi
@dash.callback(
    Output(component_id='simulation-result', component_property='figure'),
    Input('run-button', 'n_clicks')
)


def graph_update(n_clicks):
    # filtering based on the slide and dropdown selection
    if n_clicks >=1:
        #program numerik ---start----
        inout = df_inflow["Data"].values - df_outflow["Data"].values
        N = len(inout)
        u = np.zeros(N) #vektor (0,0,0..n)
        u0 = 48750 #volume embung awal yg dihitung/wawancara/buku
        u[0] = u0 #referensi [400,0,0...0]
        dt = 1 #langkah waktu langkah waktu 

        #metode Euler
        for n in range(N-1):
            u[n + 1] = u[n] + dt*inout[n]
        #program numerik ---end----


        # the figure/plot created using the data filtered above 
        simulation_fig = go.FigureWidget()
        simulation_fig.add_scatter(name='Simulation', x=df_outflow['Waktu'], y=u)
        simulation_fig.layout.title = 'Simulation'

        return simulation_fig
    else:
        simulation_fig = go.FigureWidget()
        simulation_fig.layout.title = 'Simulation'

        return simulation_fig

    


