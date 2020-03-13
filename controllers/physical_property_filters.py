import dash
from dash.dependencies import Input, Output, State

#from other modules
from views.layout import Layout
from dataframe import material_df, property_df
from app import app
from models.Dataframe import MaterialDF
import views.property_filter_modals 

dropdown_previous_state = []

"""Property Filter Modals"""
@app.callback(
    [
        Output("physical_property_range_modal_" + MaterialDF.PROPERTIES[key], "is_open") \
        for key, value in MaterialDF.PROPERTIES.items()
    ],
    [
        Input('physical-property-dropdown', 'value'), 
        *[Input("close_property_range_modal_" + MaterialDF.PROPERTIES[key], "n_clicks") \
        for key, value in MaterialDF.PROPERTIES.items()]
    ],
    [
        State("physical_property_range_modal_" + MaterialDF.PROPERTIES[key], "is_open") \
        for key, value in MaterialDF.PROPERTIES.items()
    ],
)
def toggle_property_range_modal_phys(n1, *args):
    global dropdown_previous_state
    ctx = dash.callback_context
    
    # n1 is hard to process as NoneType
    if n1 is None:
        n1 = []

    # identify if property-dropdown triggered callback
    if ctx.triggered[0]['prop_id'] == 'physical-property-dropdown.value':
        # if a property was REMOVED via dropdown
        # then do not open a modal (ie return False for all modals)
        if len(dropdown_previous_state) >= len(n1):
            dropdown_previous_state = n1
            return [False for i in range(len(MaterialDF.PROPERTIES))]
    
        # if a property was ADDED via dropdown
        # then open the modal of property that was selected
        if len(n1) > len(dropdown_previous_state):
            new_property = set(n1) - set(dropdown_previous_state)
            # return True for modal of property that was selected
            # return False for all other property modals
            return [True if i in new_property else False 
                    for i in range(1, len(MaterialDF.PROPERTIES) + 1)]
    
    #if here, then callback was triggered by closing modal
    # therefore, return False for all modals
    dropdown_previous_state = n1
    return [False for i in range(len(MaterialDF.PROPERTIES))]

#all properties with '°F' as units
def phys_update_range_output(value):
    return 'You have selected between {} °F and {} °F'.format(value[0], value[1])
for key, value in MaterialDF.PROPERTIES.items():
    if key == 4:
        continue
    app.callback(
        Output('output-container-range-slider-' + value, 'children'),
        [
            Input('my-range-slider-' + value, 'value')
        ]
    )(phys_update_range_output)

#FAW
@app.callback(
    Output('output-container-range-slider-FAW', 'children'),
    [Input('my-range-slider-FAW', 'value')])
def update_range_output_Tg(value):
    return 'You have selected between {} g/m\N{SUPERSCRIPT TWO} and {} g/m\N{SUPERSCRIPT TWO}'.format(value[0], value[1])
