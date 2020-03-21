import dash
from dash.dependencies import Input, Output

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
    print("test conditions df ", test_conditions_df)
    print("n4 ", n4)
    print("n5 ", n5)
    print("n6 ", n6)
    print("n7 ", n7)
    for i, parameter in enumerate(args):
        print("i ", i)
        print("parameter", parameter)
    test_conds = [(test_conditions_df.iloc[i - 1]["temperature"], test_conditions_df.iloc[i - 1]["environment"]) for i in n1]
    mech_props = [PropertyDF.PROPERTIES[i] for i in n2]
    phys_props = [MaterialDF.PROPERTIES[i] for i in n3]
    return "Test Conditions: {}, Property Dropdown: {}, Physical Property Dropdown: {}".format(test_conds, mech_props, phys_props)