import dash
from dash.dependencies import Input, Output, State

#from other modules
from app import app
from views.layout import Layout

@app.callback(
    Output('toggle-switch-label', 'children'),
    [
        Input('predict-toggle-switch', 'value')
    ]
)
def update_toggle_label(value):
    value = False if value is None else value
    if value == False:
        return 'Predicted Material Properties NOT shown.'
    else:
        return 'Predicted Material Properties shown.'