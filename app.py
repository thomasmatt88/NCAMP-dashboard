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
from layout import Layout
from dataframe import df, df6

#app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server #need to add this line for heroku deployment

#this element will contain all our other elements 
app.layout = Layout

#usually place callbacks near bottom of application
@app.callback(
    Output('material-selection', 'children'),
    [Input('material-dropdown', 'value')])
def update_material_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('material-table', 'data'), #one output id can have one callback
    [Input('material-dropdown', 'value'),
    Input('material-table', 'sort_by')])
def update_material_table(value, sort_by):
    dff = df
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")

@app.callback(
    Output('test-condition-selection', 'children'),
    [Input('test-condition-checklist', 'value')])
def update_material_property_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [Input('test-condition-checklist', 'value'),
    Input('material-property-table', 'sort_by'),
    Input('material-dropdown', 'value'),
    Input('my-range-slider', 'value')]
    )
def update_material_property_table(test_condition_value, sort_by, material_value, property_range_value):
    if len(sort_by):
        dff = df6.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df6
    
    #filter by material
    if material_value is None:
        #return dff[dff['material_id'] == material_value].drop(columns = ['material_id']).to_dict("rows") #one value at a time
        dff = dff[dff['material_id'] == material_value].drop(columns = ['material_id']) #one value at a time
    else:
        #return dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id']).to_dict("rows")
        dff = dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id'])
    
    #filter by material property range
    if property_range_value is None:
        pass
    else:
        dff = dff[
            (property_range_value[0] < dff['F1tu (ksi)']) & (dff['F1tu (ksi)'] < property_range_value[1])
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

@app.callback(
    Output('material-property-selection', 'children'),
    [Input('property-dropdown', 'value')])
def update_property_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output("property_range_modal", "is_open"),
    [Input('property-dropdown', 'value'), Input("close_property_range_modal", "n_clicks")],
    [State("property_range_modal", "is_open")],
)
def toggle_property_range_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('output-container-range-slider', 'children'),
    [Input('my-range-slider', 'value')])
def update_range_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)