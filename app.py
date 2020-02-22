import dash
import dash_bootstrap_components as dbc
import os

#app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server #need to add this line for heroku deployment
server.secret_key = os.environ.get('secret_key', 'secret')
app.config.suppress_callback_exceptions = True

# index imports app, so import it after app is defined to avoid a circular import
#from dash_test import index

#if __name__ == '__main__':
#import index



