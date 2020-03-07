import dash
from dash.dependencies import Input, Output, State

#from other modules
from dataframe import property_df, material_df
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
        Input('physical-property-dropdown', 'value'),
        Input('my-range-slider-Tg', 'value'),
        *[Input("my-range-slider-" + PropertyDF.PROPERTIES[key], 'value') \
        for key, value in PropertyDF.PROPERTIES.items()],
    ]
)

def update_material_property_table(
    test_condition_value, sort_by, material_value, properties_to_filter, \
    physical_properties_to_filter, Tg_range, *args):
    #property_range_value_F1tu, property_range_value_F2tu, property_range_value_E1t, property_range_value_F1cu):

    # convert range slider values into dictionary for property filtering
    ranges = {}
    for i, parameter in enumerate(args):
        # NoneType is difficult to process
        parameter = [] if parameter is None else parameter
        ranges[i + 1] = parameter

    # NoneType is difficult to process
    properties_to_filter = [] if properties_to_filter is None else properties_to_filter
    physical_properties_to_filter = [] if physical_properties_to_filter is None else physical_properties_to_filter

    #sort dataframe
    dff = property_df.sort_dataframe(sort_by)

    # filter material_df by Tg
    # then make sure material_df and property_df contain the same materials
    if 'Tg' in physical_properties_to_filter:
        mdff = material_df.filter_by_Tg(Tg_range)
        dff = dff[dff['Material'].isin(mdff['Material'])]
    
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