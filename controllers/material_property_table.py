import dash
from dash.dependencies import Input, Output, State

#from other modules
from dataframe import property_df
from app import app
from views.layout import Layout
from models.Dataframe import PropertyDF

@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [
        Input('test-condition-checklist', 'value'),
        Input('material-property-table', 'sort_by'),
        Input('material-dropdown', 'value'),
        Input('property-dropdown', 'value'),
        Input('my-range-slider-F1tu', 'value'),
        Input('my-range-slider-F2tu', 'value'),
        Input('my-range-slider-E1t', 'value'),
        Input('my-range-slider-' + PropertyDF.PROPERTIES[4], 'value')
    ]
    )

def update_material_property_table(
    test_condition_value, sort_by, material_value, properties_to_filter, \
    property_range_value_F1tu, property_range_value_F2tu, property_range_value_E1t, property_range_value_F1cu):

    property_range_value_F1tu = [] if property_range_value_F1tu is None else property_range_value_F1tu
    property_range_value_F2tu = [] if property_range_value_F2tu is None else property_range_value_F2tu
    property_range_value_E1t = [] if property_range_value_E1t is None else property_range_value_E1t
    property_range_value_F1cu = [] if property_range_value_F1cu is None else property_range_value_F1cu
    properties_to_filter = [] if properties_to_filter is None else properties_to_filter

    ranges = {1: property_range_value_F1tu, 2: property_range_value_F2tu, 3: property_range_value_E1t, \
            4: property_range_value_F1cu}

    #sort dataframe
    dff = property_df.sort_dataframe(sort_by)
    
    #filter by material
    dff = dff.filter_by_material(material_value)

    #filter by property
    for i in properties_to_filter:
        dff = dff.filter_by_property(i, ranges[i])
    
    #filter by test condition
    if test_condition_value is None:
        return dff.to_dict("rows")
    else:
        test_condition_value = [int(i) for i in test_condition_value]
        return dff[dff['test_conditions_id'].isin(test_condition_value)].to_dict("rows")