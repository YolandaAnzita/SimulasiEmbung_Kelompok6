#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output

from app import app
from apps import home, embunga, showcase, creator, introduction

url_content_layout = html.Div(children=[
     dcc.Location(id="url",refresh=False),
     html.Div(id="output-div")
 ])

app.layout = url_content_layout

app.validation_layout = html.Div([
     url_content_layout,
     home.home_layout,
     showcase.model_showcase_layout,
     embunga.page_layout,
     creator.page_layout,
     introduction.page_layout
 ])


@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
     if pathname == "/showcase":
         return  showcase.model_showcase_layout
     elif pathname == "/embunga":
         return embunga.page_layout
     elif pathname == "/creator":
         return creator.page_layout
     elif pathname == "/introduction":
         return introduction.page_layout
     else:
         return home.home_layout


if __name__ == "__main__":
     app.run_server(debug=True, port = process.env.PORT)