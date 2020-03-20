import dash
from dash.dependencies import Input, Output

#from other modules
from views.layout import Layout
from app import app
import views.property_filter_modals 

dropdown_previous_state = []

@app.callback(
    Output('filter-selections-container', 'children'),
    [
        Input('test-condition-checklist', 'value'),
        Input('property-dropdown', 'value'),
        Input('physical-property-dropdown', 'value'), 
    ]
)
def toggle_property_range_modal_phys(n1, n2, n3):
    return "Test Conditions: {}, Property Dropdown: {}, Physical Property Dropdown: {}".format(n1, n2, n3)