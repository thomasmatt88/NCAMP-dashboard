import dash
import dash_bootstrap_components as dbc

#app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server #need to add this line for heroku deployment
app.config.suppress_callback_exceptions = True

