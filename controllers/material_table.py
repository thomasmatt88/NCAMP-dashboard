import dash
from dash.dependencies import Input, Output, State

#from other modules
from dataframe import material_df
from app import app
from views.layout import Layout

@app.callback(
    Output('material-table', 'data'), #one output id can have one callback
    [
        Input('material-dropdown', 'value'),
        Input('material-table', 'sort_by'),
    ])
def update_material_table(value, sort_by):
    dff = material_df
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    if 'all' in value: # if all materials are selected
        return dff.to_dict("rows") 
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")