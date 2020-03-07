import dash
from dash.dependencies import Input, Output, State

#from other modules
from views.layout import Layout
from dataframe import material_df, property_df
from app import app
from models.Dataframe import PropertyDF
import views.property_filter_modals 

dropdown_previous_state = []

"""Property Filter Modals"""
@app.callback(
    
    Output("physical_property_range_modal_Tg", "is_open")
    ,
    [
        Input('physical-property-dropdown', 'value'), 
        Input("close_property_range_modal_Tg", "n_clicks")
    ],
    [
        State("physical_property_range_modal_Tg", "is_open")
    ]
    ,
)
def toggle_property_range_modal_Tg(n1, *args):
    global dropdown_previous_state
    ctx = dash.callback_context
    
    # n1 is hard to process as NoneType
    if n1 is None:
        n1 = []

    # identify if 'physical-property-dropdown' triggered callback
    if ctx.triggered[0]['prop_id'] == 'physical-property-dropdown.value':
        # if a property was REMOVED via dropdown
        # then do not open a modal (ie return False for all modals)
        if len(dropdown_previous_state) >= len(n1):
            dropdown_previous_state = n1
            return False
    
        # if a property was ADDED via dropdown
        # then open the modal of property that was selected
        if len(n1) > len(dropdown_previous_state):
            # return True for modal of property that was selected
            return True
    
    #if here, then callback was triggered by closing modal
    # therefore, return False for all modals
    dropdown_previous_state = n1
    return False

#Tg
@app.callback(
    Output('output-container-range-slider-Tg', 'children'),
    [Input('my-range-slider-Tg', 'value')])
def update_range_output_Tg(value):
    return 'You have selected between {} °F and {} °F'.format(value[0], value[1])
