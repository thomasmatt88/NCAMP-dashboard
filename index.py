import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pymysql
import os

#from other modules
from views.layout import Layout
from dataframe import material_df, property_df
from app import app
import controllers.property_filters

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
    [Input('material-dropdown', 'value'),
    Input('material-table', 'sort_by')])
def update_material_table(value, sort_by):
    dff = material_df
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")
@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [Input('test-condition-checklist', 'value'),
    Input('material-property-table', 'sort_by'),
    Input('material-dropdown', 'value'),
    Input('property-dropdown', 'value'),
    Input('my-range-slider-F1tu', 'value'),
    Input('my-range-slider-F2tu', 'value')
    ]
    )
def update_material_property_table(test_condition_value, sort_by, material_value, \
    properties_to_filter, property_range_value_F1tu, property_range_value_F2tu):
    if len(sort_by):
        dff = property_df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = property_df
    
    #filter by material
    if material_value is None:
        #return dff[dff['material_id'] == material_value].drop(columns = ['material_id']).to_dict("rows") #one value at a time
        dff = dff[dff['material_id'] == material_value].drop(columns = ['material_id']) #one value at a time
    else:
        #return dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id']).to_dict("rows")
        dff = dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id'])
    
    #filter by material property range
    if property_range_value_F1tu is None:
        pass
    else:
        # do no filter by property if property is not chosen from dropdown
        if properties_to_filter is not None:
            if len(properties_to_filter) != 0:
                dff = dff[
                    (property_range_value_F1tu[0] < dff['F1tu (ksi)']) & (dff['F1tu (ksi)'] < property_range_value_F1tu[1])
                ]
    if property_range_value_F2tu is None:
        pass
    else:
        # do no filter by property if property is not chosen from dropdown
        if properties_to_filter is not None:
            if len(properties_to_filter) != 0:
                dff = dff[
                    (property_range_value_F2tu[0] < dff['F2tu (ksi)']) & (dff['F2tu (ksi)'] < property_range_value_F2tu[1])
                ]


    #filter by test condition
    if test_condition_value is None:
        return dff.to_dict("rows")
    else:
        test_condition_value = [int(i) for i in test_condition_value]
        return dff[dff['test_conditions_id'].isin(test_condition_value)].to_dict("rows")
    
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@app.callback(
    Output("property_modal", "is_open"),
    [Input("open_property_modal", "n_clicks"), Input("close_property_modal", "n_clicks")],
    [State("property_modal", "is_open")],
)
def toggle_property_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#app.run_server(debug=True)

if __name__ == '__main__':
    #don't use debug = True on production server
    server = app.server #need to add this line for heroku deployment
    server.secret_key = os.environ.get('secret_key', 'secret')
    app.run_server(debug=True)
