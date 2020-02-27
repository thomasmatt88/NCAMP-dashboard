import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pymysql

#from other modules
from views.layout import Layout
from dataframe import material_df
from app import app
import controllers.property_filters
import controllers.material_property_table

#this element will contain all our other elements 
app.layout = Layout
"""
#usually place callbacks near bottom of application
@app.callback(
    Output('material-selection', 'children'),
    [Input('material-dropdown', 'value')])
def update_material_output(value):
    return 'You have selected "{}"'.format(value)
"""
@app.callback(
    Output('material-table', 'data'), #one output id can have one callback
    [
        Input('material-dropdown', 'value'),
        Input('material-table', 'sort_by')
    ])
def update_material_table(value, sort_by):
    dff = material_df
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")
    
@app.callback(
    Output("modal", "is_open"),
    [
        Input("open", "n_clicks"), 
        Input("close", "n_clicks")
    ],
    [
        State("modal", "is_open")
    ],
)
def toggle_modal(n1, n2, is_open):
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

#app.run_server(debug=True)

if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)
