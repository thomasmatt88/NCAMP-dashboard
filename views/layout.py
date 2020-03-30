import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_bootstrap_components as dbc
from dataframe import material_df, property_df
import views.property_filter_modals
from models.Dataframe import PropertyDF, MaterialDF

material_dropdown = dcc.Dropdown(
        id = 'material-dropdown', #need to reference for callback
        options=[
        {'label': 'All Materials', 'value': 'all'},
        {'label': 'Hexcel AS4/8552 unidirectional tape', 'value': 1},
        {'label': 'Hexcel AS4 3k/8552 plain weave', 'value': 2},
        {'label': 'Hexcel IM7/8552 unidirectional tape', 'value': 3},
        {'label': 'Newport MR60H/ NCT4708 unidirectional tape', 'value': 4},
        {'label': 'HTS40 E13 3k/MTM45-1 plain weave fabric', 'value': 5},
        {'label': '6781 S-2/MTM45-1 8-harness satin weave fabric', 'value': 6},
        {'label': 'E-Glass 7781/MTM45-1 8-harness satin weave fabric', 'value': 7},
        {'label': 'Advanced Composites Group - MTM45-1 HTS(12K) Unitape', 'value': 8},
        {'label': 'Advanced Composites Group - MTM45-1/IM7-145 gsm Unitape', 'value': 9},
        {'label': 'Cytec 5320-1 T650 Unitape Gr 145 RC 33%', 'value': 10},
        {'label': 'Cytec 5320-1 T650 3k-PW fabric', 'value': 11},
        {'label': 'EP2202 IM7G Unitape Gr 190 RC 33%', 'value': 12},
        {'label': 'Cytec Cycom EP2202 T650 3k-PW fabric with RC 38%', 'value': 13},
        {'label': 'TenCate BT250E-6 S2 Unitape Gr 284gsm 33% RC', 'value': 14},
        {'label': 'TenCate BT250E-6 IM7 GP 12k Unitape Gr 148gsm 33% RC', 'value': 15},
        {'label': 'TenCate BT250E-6 AS4C 3k-PW Fabric 195gsm 40% RC', 'value': 16},
        {'label': 'TCAC12k HTS SFP OSI-TC250 42% fabric prepreg', 'value': 17},
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
            {"name": [MaterialDF.PROPERTIES[1], "°F"], "id": MaterialDF.PROPERTIES[1]},
            {"name": [MaterialDF.PROPERTIES[2], "°F"], "id": MaterialDF.PROPERTIES[2]},
            {"name": [MaterialDF.PROPERTIES[3], "°F"], "id": MaterialDF.PROPERTIES[3]},
            {"name": [MaterialDF.PROPERTIES[4], "g/m\N{SUPERSCRIPT TWO}"], "id": MaterialDF.PROPERTIES[4]},
            {"name": ["MaterialSpec", ""], "id": "MaterialSpec", "type" : 'text', "presentation" : 'markdown'},
            {"name": ["ProcessSpec", ""], "id": "ProcessSpec", "type" : 'text', "presentation" : 'markdown'}
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
        },
        tooltip={'Material': 'this is a test tooltip' }
)

property_table = dash_table.DataTable(
        id = 'material-property-table', #need to reference for callback
        columns = [
            {"name": ["Material", ""], "id": "Material", "type" : 'text', "presentation" : 'markdown'},
            {"name": ["Test Temperature", "°F"], "id": "Test Temperature"},
            {"name": ["Test Environment", ""], "id": "Test Environment"},
            {"name": [PropertyDF.PROPERTIES[1], "ksi"], "id": PropertyDF.PROPERTIES[1]},
            {"name": [PropertyDF.PROPERTIES[2], "ksi"], "id": PropertyDF.PROPERTIES[2]},
            {"name": [PropertyDF.PROPERTIES[3], "msi"], "id": PropertyDF.PROPERTIES[3]},
            {"name": [PropertyDF.PROPERTIES[4], "ksi"], "id": PropertyDF.PROPERTIES[4]},
            {"name": [PropertyDF.PROPERTIES[5], "ksi"], "id": PropertyDF.PROPERTIES[5]},
            {"name": [PropertyDF.PROPERTIES[6], "ksi"], "id": PropertyDF.PROPERTIES[6]},
            {"name": [PropertyDF.PROPERTIES[7], "ksi"], "id": PropertyDF.PROPERTIES[7]},
            {"name": [PropertyDF.PROPERTIES[8], "in/ply"], "id": PropertyDF.PROPERTIES[8]}
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
                                {'label': '200°F, wet', 'value': 7},
                                {'label': '200°F, dry', 'value': 8}
                            
                            ],
                            inputStyle={"margin-left": "20px", "margin-right": "10px"}
)

property_dropdown = dcc.Dropdown(
        id = 'property-dropdown', #need to reference for callback
        options=[{'label': value, 'value': key} for key, value in PropertyDF.PROPERTIES.items()],
        placeholder="Select a mechanical property",
        multi = True
)

physical_property_dropdown = dcc.Dropdown(
        id = 'physical-property-dropdown', #need to reference for callback
        options=[{'label': value, 'value': key} for key, value in MaterialDF.PROPERTIES.items()],
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
            *[value for key, value in views.property_filter_modals.phys_modals.items()]
        ]
)

material_recommendation = html.P(
    id = "material-recommendation",
    style = {
         'color': '#007bff', 
         'margin-top': '10px',
         'font-style': 'italic',
         'font-size': 'small',
    #     "border-style": "solid", 
    #     "border-width": "1px", 
    #     "display" : "inline-block",
    #     "margin" : "2px", 
    #     "padding" : "2px", 
    #     "background-color" : "#EEF4FF"
    }
)

#this element will contain all our other elements 
Layout = html.Div([
    html.H1("NCAMP Table"),
    html.H3("Select a Material"),
    material_dropdown,
    material_recommendation,
    material_table,
    html.H3("Select a Filter"),
    property_filters, 
    html.Div(id = "filter-selections-container"), # need to reference id for callback
    property_table
])