from dash.dependencies import Input, Output, State

#from other modules
from views.layout import Layout
from dataframe import material_df, property_df
from app import app

dropdown_previous_state = None

"""Property Filter Modals"""
@app.callback(
    [
        Output("property_range_modal_F1tu", "is_open"),
        Output("property_range_modal_F2tu", "is_open")
    ],
    [
        Input('property-dropdown', 'value'), 
        Input("close_property_range_modal_F1tu", "n_clicks"),
        Input("close_property_range_modal_F2tu", "n_clicks")
    ],
    [
        State("property_range_modal_F1tu", "is_open"),
        State("property_range_modal_F2tu", "is_open")
    ],
)
def toggle_property_range_modal(n1, n2, n3, F1tu_is_open, F2tu_is_open):
    global dropdown_previous_state
    # property modals can't be open if no property has been
    # selected from dropdown
    if n1 is None or len(n1) == 0:
        dropdown_previous_state = n1
        return False, False
    
    # if any modal was already open then an update 
    # was meant to close the modal
    if F1tu_is_open or F2tu_is_open:
        dropdown_previous_state = n1
        return False, False
    
    # compare dropdown to previous state
    if dropdown_previous_state is None:
        # if a property is selected from dropdown then
        # that property's modal could be open
        if 1 in n1:
            F1tu_is_open = True
        if 2 in n1:
            F2tu_is_open = True
        dropdown_previous_state = n1
        return F1tu_is_open, F2tu_is_open
    
    # if a property was REMOVED via dropdown
    # then do not open a modal
    if len(dropdown_previous_state) > len(n1):
        dropdown_previous_state = n1
        return False, False
    
    # if a property was ADDED via dropdown
    # then open the modal of property that was selected
    if len(n1) > len(dropdown_previous_state):
        new_property = set(n1) - set(dropdown_previous_state)
        if 1 in new_property:
            F1tu_is_open = True
        if 2 in new_property:
            F2tu_is_open = True
        dropdown_previous_state = n1
        return F1tu_is_open, F2tu_is_open
    
    #if here then callback was triggered by closing modal
    dropdown_previous_state = n1
    return False, False

#F1tu
@app.callback(
    Output('output-container-range-slider-F1tu', 'children'),
    [Input('my-range-slider-F1tu', 'value')])
def update_range_output(value):
    return 'You have selected between {} ksi and {} ksi'.format(value[0], value[1])

#F2tu
@app.callback(
    Output('output-container-range-slider-F2tu', 'children'),
    [Input('my-range-slider-F2tu', 'value')])
def update_range_output_F2tu(value):
    return 'You have selected between {} ksi and {} ksi'.format(value[0], value[1])