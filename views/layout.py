import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_bootstrap_components as dbc
from dataframe import material_df, property_df
import views.property_filter_modals
from models.Dataframe import PropertyDF

material_dropdown = dcc.Dropdown(
        id = 'material-dropdown', #need to reference for callback
        options=[
        {'label': 'Hexcel AS4/8552 unidirectional tape', 'value': 1},
        {'label': 'Hexcel AS4 3k/8552 plain weave', 'value': 2},
        {'label': 'Hexcel IM7/8552 unidirectional tape', 'value': 3},
        {'label': 'Newport MR60H/ NCT4708 unidirectional tape', 'value': 4},
        {'label': 'HTS40 E13 3k/MTM45-1 plain weave fabric', 'value': 5},
        {'label': '6781 S-2/MTM45-1 8-harness satin weave fabric', 'value': 6},
        {'label': 'E-Glass 7781/MTM45-1 8-harness satin weave fabric', 'value': 7}
        ],
        placeholder="Select a material",
        multi = True
)

material_table = dash_table.DataTable(
        id = 'material-table', #need to reference for callback
        columns = [
            {"name": ["Material", ""], "id": "Material"},
            {"name": ["Fiber", ""], "id": "Fiber"},
            {"name": ["Resin", ""], "id": "Resin"},
            {"name": ["MOT", "°F"], "id": "MOT"},
            {"name": ["Tg", "°F"], "id": "Tg"},
            {"name": ["WetTg", "°F"], "id": "WetTg"},
            {"name": ["FAW", "g/m\N{SUPERSCRIPT TWO}"], "id": "FAW"},
            {"name": ["MaterialSpec", ""], "id": "MaterialSpec"},
            {"name": ["ProcessSpec", ""], "id": "ProcessSpec"}
        ], 
        data = material_df.drop(columns = 'id').to_dict("rows"),
        style_header = {
            'fontWeight': 'bold'
        },
        style_table={
            'margin-top': '35px',
            'margin-bottom': '35px',
            "maxWidth": '85%',
            "margin-left": 'auto',
            "margin-right": 'auto'
        }
)

property_table = dash_table.DataTable(
        id = 'material-property-table', #need to reference for callback
        columns = [
            {"name": ["Material", ""], "id": "Material"},
            {"name": ["Test Temperature", "°F"], "id": "Test Temperature"},
            {"name": ["Test Environment", ""], "id": "Test Environment"},
            {"name": [PropertyDF.PROPERTIES[1], "ksi"], "id": PropertyDF.PROPERTIES[1]},
            {"name": [PropertyDF.PROPERTIES[2], "ksi"], "id": PropertyDF.PROPERTIES[2]},
            {"name": [PropertyDF.PROPERTIES[3], "msi"], "id": PropertyDF.PROPERTIES[3]},
            {"name": [PropertyDF.PROPERTIES[4], "ksi"], "id": PropertyDF.PROPERTIES[4]},
            {"name": ["F2cu", "ksi"], "id": "F2cu"},
            {"name": ["F12su", "ksi"], "id": "F12su"},
            {"name": ["F31sbs", "ksi"], "id": "F31sbs"},
            {"name": ["CPT", "in/ply"], "id": "CPT"}
        ], 
        data = property_df.drop(columns = ['material_id']).to_dict("rows"),
        style_header = {
            'fontWeight': 'bold',
            'whiteSpace': 'normal'
            #'height': 'auto'
        },
        style_table={
            'padding-top': '35px',
            "maxWidth": '85%',
            "margin-left": 'auto',
            "margin-right": 'auto'
        },
        
        style_cell_conditional = [
            {'if': {'column_id': 'Test Temperature'},
            'maxWidth': '90px'},
            {'if': {'column_id': 'Test Environment'},
            'maxWidth': '90px'}
        ],
        
        sort_action = 'custom',
        sort_mode = 'single',
        sort_by = []
)

test_conditions_checklist = dcc.Checklist(
                            id = 'test-condition-checklist', #need to reference for callback
                            options = [
                                {'label': '-65°F, dry', 'value': 1},
                                {'label': '70°F, dry', 'value': 2},
                                {'label': '250°F, wet', 'value': 3},
                                {'label': '250°F, dry', 'value': 4},
                                {'label': '180°F, dry', 'value': 5},
                                {'label': '180°F, wet', 'value': 6},
                                {'label': '200°F, wet', 'value': 7}
                            
                            ],
                            inputStyle={"margin-left": "20px", "margin-right": "10px"}
)

property_dropdown = dcc.Dropdown(
        id = 'property-dropdown', #need to reference for callback
        options=[ {'label': value, 'value': key} for key, value in PropertyDF.PROPERTIES.items()],
        placeholder="Select a mechanical property",
        multi = True
)

physical_property_dropdown = dcc.Dropdown(
        id = 'physical-property-dropdown', #need to reference for callback
        options=[ {'label': 'Tg', 'value': 'Tg'}],
        placeholder="Select a physical property",
        multi = True
)

property_filters = html.Div(
        [
            dbc.Button("Test Condition", color = "primary", id="open_test_conditions_modal", style={'margin-right': 10}),
            dbc.Button("Mechanical Property", color = "secondary", id = "open_property_modal", style={'margin-right': 10}),
            dbc.Button("Physical Property", color = "success", id = "open_physical_property_modal", style={'margin-right': 10}),
            dbc.Modal(
                [
                    dbc.ModalHeader("Filter by test condition."),
                    dbc.ModalBody(
                        test_conditions_checklist
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "primary", id="close_test_conditions_modal", className="ml-auto")
                    ),
                ],
                id="test_conditions_modal",
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader("Filter by mechanical property range."),
                    dbc.ModalBody(
                        property_dropdown
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_modal", className="ml-auto")
                    ),
                ],
                id="property_modal",
            ),
            *[value for key, value in views.property_filter_modals.modals.items()],
            dbc.Modal(
                [
                    dbc.ModalHeader("Filter by physical property range."),
                    dbc.ModalBody(
                       physical_property_dropdown
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "success", id = "close_physical_property_modal", className = "ml-auto")
                    )
                ],
                id = "physical_property_modal"
            ),
            views.property_filter_modals.Tg_modal
        ]
)

#this element will contain all our other elements 
Layout = html.Div([
    html.H1("NCAMP Table"),
    html.H3("Select a Material"),
    material_dropdown,
    material_table,
    html.H3("Select a Filter"),
    property_filters, 
    property_table
])