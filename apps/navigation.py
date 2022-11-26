import dash_bootstrap_components as dbc
#import dash_html_components as html
from dash import html
#from app import app
from dash.dependencies import Input, Output, State
import dash

#navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(dbc.NavLink("Home", href="/")),
 #        dbc.NavItem(dbc.NavLink("Model Showcase", href="/showcase")),
#         dbc.DropdownMenu(
 #            children=[
 #                dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Model Showcase", href="/showcase")
#             ],
#             nav=True,
#             in_navbar=True,
 #            label="More",
#         ),
 #    ],
 #    brand="Plotly Deep Learning App",
#     brand_href="/",
 #    color="primary",
 #    dark=True,
 #    fluid=True,
 #    links_left=True,
 #    sticky='Top'  
 #)

navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('logoweb1.png'), height="40px"),
                            dbc.NavbarBrand("Simulation Learning App", className="ms-2")
                        ],
                        width={"size":"auto"}
                        )
                    ],
                    align="center",
                    className="g-0"),

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Home", href="/")),
                                dbc.NavItem(dbc.NavLink("Introduction", href="/introduction")),
                                dbc.NavItem(dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("Embung A", href="/embunga")
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="Profil",
                                )),
                                dbc.NavItem(dbc.NavLink("Model Showcase", href="/showcase")),
                                dbc.NavItem(dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("More pages", header=True),
                                            dbc.DropdownMenuItem("About Creator", href="/creator")
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="More Information ",
                                ))
                            ],
                            navbar=True
                            )
                        ],
                        width={"size":"auto"})
                    ],
                    align="center"),
                    dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                    
                    dbc.Row([
                        dbc.Col(
                             dbc.Collapse(
                                dbc.Nav([
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/siddharthajuprod07/algorithms/tree/master/plotly_deep_learning_app",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi bi-twitter"), href="https://twitter.com/ntganj",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-youtube"), href="https://youtube.com/@Saryzano",external_link=True) ),
                                    # dbc.Input(type="search", placeholder="Search"),
                                    # dbc.Button( "Search", color="primary", className="ms-2", n_clicks=0 ),
                                ]
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True
                             )
                        )
                    ],
                    align="center")
                ],
            fluid=True
            ),
    color="black",
    dark=True
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open