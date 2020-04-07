import dash
from dash.dependencies import Input, Output, State

#from other modules
from dataframe import property_df, property_df_impute, material_df_links
from app import app
from views.layout import Layout
from models.Dataframe import PropertyDF, MaterialDF

@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [
        Input('test-condition-checklist', 'value'),
        Input('material-property-table', 'sort_by'),
        Input('predict-toggle-switch', 'value'),
        Input('material-dropdown', 'value'),
        Input('property-dropdown', 'value'),
        Input('physical-property-dropdown', 'value'),
        Input('my-range-slider-' + MaterialDF.PROPERTIES[1], 'value'),
        Input('my-range-slider-' + MaterialDF.PROPERTIES[2], 'value'),
        Input('my-range-slider-' + MaterialDF.PROPERTIES[3], 'value'),
        Input('my-range-slider-' + MaterialDF.PROPERTIES[4], 'value'),
        *[Input("my-range-slider-" + PropertyDF.PROPERTIES[key], 'value') \
        for key, value in PropertyDF.PROPERTIES.items()],
    ]
)

def update_material_property_table(
    test_condition_value, sort_by, predict, material_value, properties_to_filter, \
    physical_properties_to_filter, MOT_range, Tg_range, WetTg_range, FAW_range, *args):
    #property_range_value_F1tu, property_range_value_F2tu, property_range_value_E1t, property_range_value_F1cu):
    # convert range slider values into dictionary for property filtering
    ranges = {}
    for i, parameter in enumerate(args):
        # NoneType is difficult to process
        parameter = [] if parameter is None else parameter
        ranges[i + 1] = parameter

    # convert phys range slider values into dictionary for physcial property filtering
    phys_ranges = {}
    phys_ranges[1] = MOT_range
    phys_ranges[2] = Tg_range
    phys_ranges[3] = WetTg_range
    phys_ranges[4] = FAW_range

    # NoneType is difficult to process
    properties_to_filter = [] if properties_to_filter is None else properties_to_filter
    physical_properties_to_filter = [] if physical_properties_to_filter is None else physical_properties_to_filter
    material_value = [] if material_value is None else material_value
    predict = False if predict is None else predict

    #sort dataframe and choose whether to show predicted material properties or not
    print("PREDICT", predict)
    if predict:
        dff = property_df_impute.sort_dataframe(sort_by)
    else:
        dff = property_df.sort_dataframe(sort_by)
    

    mdff = material_df_links
    # filter material_df_links by physical property range
    # then make sure material_df_links and property_df contain the same materials
    for i in range(1, 5):
        if i in physical_properties_to_filter:
            #mdff = material_df.filter_by_Tg(Tg_range)
            mdff = mdff.filter_by_physical_property(i, phys_ranges[i])
            dff = dff[dff['Material'].isin(mdff['Material'])]
    
    # no need to filter by material if 'all materials' selected
    if 'all' not in material_value: 
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