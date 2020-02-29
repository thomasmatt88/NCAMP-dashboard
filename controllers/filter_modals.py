import dash
from dash.dependencies import Input, Output, State

#from other modules
from app import app
from views.layout import Layout

@app.callback(
    Output("test_conditions_modal", "is_open"),
    [
        Input("open_test_conditions_modal", "n_clicks"), 
        Input("close_test_conditions_modal", "n_clicks")
    ],
    [
        State("test_conditions_modal", "is_open")
    ],
)
def toggle_test_conditions_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@app.callback(
    Output("property_modal", "is_open"),
    [
        Input("open_property_modal", "n_clicks"), 
        Input("close_property_modal", "n_clicks")
    ],
    [
        State("property_modal", "is_open")
    ],
)
def toggle_property_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open