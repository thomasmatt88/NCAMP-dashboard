from dash.dependencies import Input, Output, State

#from other modules
from views.layout import Layout
from dataframe import material_df, property_df
from app import app

"""Property Filter Modals"""
#F1tu
@app.callback(
    Output("property_range_modal_F1tu", "is_open"),
    [Input('property-dropdown', 'value'), Input("close_property_range_modal_F1tu", "n_clicks")],
    [State("property_range_modal_F1tu", "is_open")],
)
def toggle_property_range_modal(n1, n2, is_open):
    #None is status before user has even selected property from dropdown
    if n1 is not None:
        # no selection from dropdown does not change property_range_modal status
        if len(n1) == 0:
            return is_open
        # if user selects F1tu then open F1tu property_range_modal
        if n1[0] == 1:
            return not is_open
    # if user presses close property_range_modal then close the modal
    if n2:
        return not is_open
    return is_open

@app.callback(
    Output('output-container-range-slider-F1tu', 'children'),
    [Input('my-range-slider-F1tu', 'value')])
def update_range_output(value):
    return 'You have selected between {} ksi and {} ksi'.format(value[0], value[1])

#F2tu
@app.callback(
    Output("property_range_modal_F2tu", "is_open"),
    [Input('property-dropdown', 'value'), Input("close_property_range_modal_F2tu", "n_clicks")],
    [State("property_range_modal_F2tu", "is_open")],
)
def toggle_property_range_modal_F2tu(n1, n2, is_open):
    #None is status before user has even selected property from dropdown
    if n1 is not None:
        # no selection from dropdown does not change property_range_modal status
        if len(n1) == 0:
            return is_open
        # if user selects F1tu then open F1tu property_range_modal
        if n1[0] == 2:
            return not is_open
    # if user presses close property_range_modal then close the modal
    if n2:
        return not is_open
    return is_open

@app.callback(
    Output('output-container-range-slider-F2tu', 'children'),
    [Input('my-range-slider-F2tu', 'value')])
def update_range_output_F2tu(value):
    return 'You have selected between {} ksi and {} ksi'.format(value[0], value[1])