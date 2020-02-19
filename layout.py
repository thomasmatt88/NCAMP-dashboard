import dash_html_components as html
import dash_core_components as dcc
import dash_table
import dash_bootstrap_components as dbc
from dataframe import df, df6

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
        columns = [{"name": i, "id": i} for i in df.drop(columns = 'id').columns], #don't need id column
        data = df.drop(columns = 'id').to_dict("rows"),
        style_header = {
            'fontWeight': 'bold'
        }
)

property_table = dash_table.DataTable(
        id = 'material-property-table', #need to reference for callback
        columns = [{"name": i, "id": i} for i in df6.drop(columns = ['material_id']).columns], #don't need id column
        data = df6.drop(columns = ['material_id']).to_dict("rows"),
        style_header = {
            'fontWeight': 'bold'
        },
        sort_action = 'custom',
        sort_mode = 'single',
        sort_by = []
)

test_conditions_modal = html.Div(
        [
            dbc.Button("Test Condition", id="open"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Filter properties by test condition."),
                    dbc.ModalBody(
                        dcc.Checklist(
                            id = 'test-condition-checklist', #need to reference for callback
                            options = [
                                {'label': '-65°F, dry', 'value': 1},
                                {'label': '70°F, dry', 'value': 2},
                                {'label': '250°F, wet', 'value': 3},
                                {'label': '250°F, dry', 'value': 4},
                                {'label': '180°F, dry', 'value': 5},
                                {'label': '180°F, wet', 'value': 6},
                                {'label': '200°F, wet', 'value': 7}
                            
                            ]
                        )
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close", className="ml-auto")
                    ),
                ],
                id="modal",
            ),
        ]
)

#this element will contain all our other elements 
Layout = html.Div([
    html.H1("NCAMP Table"),
    html.H3("Select a Material"),
    material_dropdown,
    html.Div(
        id = "material-selection", #need to reference for callback
        ), 
    material_table,
    html.H3("Select a Filter"),
    test_conditions_modal, 
    html.Div(
        id = "material-property-selection", #need to reference for callback
    ),
    property_table
])