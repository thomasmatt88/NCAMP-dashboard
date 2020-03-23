import dash
from dash.dependencies import Input, Output
import dash_html_components as html

#from other modules
from views.layout import Layout
from app import app
import views.property_filter_modals 
from models.Dataframe import PropertyDF, MaterialDF
from dataframe import test_conditions_df

dropdown_previous_state = []

@app.callback(
    Output('filter-selections-container', 'children'),
    [
        Input('test-condition-checklist', 'value'),
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
def toggle_property_range_modal_phys(n1, n2, n3, n4, n5, n6, n7, *args):
    n1 = [] if n1 is None else n1
    n2 = [] if n2 is None else n2
    n3 = [] if n3 is None else n3
    
    phys_props_ranges = [n4, n5, n6, n7]
    mech_props_ranges = [None]*len(args)
    for i, parameter in enumerate(args):
        mech_props_ranges[i] = parameter
    
    test_conds = ["{}, {}\t".format(test_conditions_df.iloc[i - 1]["temperature"], test_conditions_df.iloc[i - 1]["environment"]) for i in n1]
    mech_props = ["{}: {}, {}\t".format(PropertyDF.PROPERTIES[i], mech_props_ranges[i - 1][0], mech_props_ranges[i - 1][1]) for i in n2]
    phys_props = ["{}: {}, {}\t".format(MaterialDF.PROPERTIES[i], phys_props_ranges[i - 1][0], phys_props_ranges[i - 1][1]) for i in n3]

    # turn lists into html
    test_conds_html = [
                        html.P(test_cond, 
                        style = {"color": "#007bff", "border-style": "solid", \
                                "border-width": "1px", "display" : "inline-block", \
                                "margin" : "2px", "padding" : "2px", "background-color" : "#EEF4FF"}) 
                        for test_cond in test_conds
                    ]
    mech_props_html = [
                        html.P(mech_prop, 
                        style = {"color": "#6c757d", "border-style": "solid", \
                                "border-width": "1px", "display" : "inline-block", \
                                "margin" : "2px", "padding" : "2px", "background-color" : "#E8E8E8"})
                        for mech_prop in mech_props
                    ]
    phys_props_html = [
                        html.P(phys_prop, 
                        style = {"color": "#28a745", "border-style": "solid", \
                                "border-width": "1px", "display" : "inline-block", \
                                "margin" : "2px", "padding" : "2px", "background-color" : "#d7fcdf"})
                        for phys_prop in phys_props
                    ]

    return html.Div([
        *test_conds_html,
        *mech_props_html,
        *phys_props_html
    ], style = {"margin-top" : "35px"})