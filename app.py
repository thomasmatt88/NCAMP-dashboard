import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from sqlalchemy import create_engine
import pymysql

#app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

db_connection_str = 'mysql+pymysql://root:root@localhost:3306/NCAMP'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM material', con=db_connection)
df1 = pd.read_sql('SELECT * FROM material_properties', con=db_connection)
df2 = pd.read_sql('SELECT * FROM test_conditions', con=db_connection)
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'test_conditions_id', right_on = 'id')
df4 = pd.merge(df, df3, how = 'inner', left_on = 'id', right_on = 'material_id')
df5 = df4

#df preprocessing
#join material and material properties by material 'id'
#drop unneccessary columns 
df6 = pd.merge(df[['id', 'Material']], df1, how = 'inner', left_on = 'id', right_on = 'material_id')
df6 = df6.drop(columns = ['id_x', 'id_y'])

# add units header to df and df6
df = df.rename(columns = {"MOT": "MOT (°F)", "Tg": "Tg (°F)", "WetTg" :"WetTg(°F)", "FAW": "FAW (g/m^2)"})
"""
header_tuples = [('Material', None), ('material_id', None), ('test_conditions_id', None), \
    ('F1tu', 'ksi'), ('F2tu', 'ksi'), ('E1t', 'msi'), ('F1cu', 'ksi'), \
        ('F2cu', 'ksi'), ('F12su', 'ksi'), ('F31sbs', 'ksi'), ('CPT', 'in/ply')]
df6.columns = pd.MultiIndex.from_tuples(header_tuples)
"""
df6 = df6.rename(columns  = {"F1tu": "F1tu (ksi)", "F2tu": "F2tu (ksi)", "E1t": "E1t (msi)", \
    "F1cu": "F1cu (ksi)", "F2cu": "F2cu (ksi)", "F12su": "F12su (ksi)", "F31sbs": "F31sbs (ksi)", \
        "CPT": "CPT (in/ply)"})


#this element will contain all our other elements 
app.layout = html.Div([
    html.H1("NCAMP Table"),
    html.H3("Select a Material"),
    dcc.Dropdown(
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
    ),
    html.Div(
        id = "material-selection", #need to reference for callback
        ), 
    dash_table.DataTable(
        id = 'material-table', #need to reference for callback
        columns = [{"name": i, "id": i} for i in df.drop(columns = 'id').columns], #don't need id column
        data = df.drop(columns = 'id').to_dict("rows"),
        style_header = {
            'fontWeight': 'bold'
        }
    ),
    html.H3("Select a Filter"),
    html.Div(
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
    ),
    html.Div(
        id = "material-property-selection", #need to reference for callback
    ),
    dash_table.DataTable(
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
])

#usually place callbacks near bottom of application
@app.callback(
    Output('material-selection', 'children'),
    [Input('material-dropdown', 'value')])
def update_material_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('material-table', 'data'), #one output id can have one callback
    [Input('material-dropdown', 'value'),
    Input('material-table', 'sort_by')])
def update_material_table(value, sort_by):
    dff = df
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")

@app.callback(
    Output('material-property-selection', 'children'),
    [Input('test-condition-checklist', 'value')])
def update_material_property_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [Input('test-condition-checklist', 'value'),
    Input('material-property-table', 'sort_by'),
    Input('material-dropdown', 'value')])
def update_material_property_table(test_condition_value, sort_by, material_value):
    print("test_condition_value ", test_condition_value)

    if len(sort_by):
        dff = df6.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df6
    
    #filter by material
    if material_value is None:
        #return dff[dff['material_id'] == material_value].drop(columns = ['material_id']).to_dict("rows") #one value at a time
        dff = dff[dff['material_id'] == material_value].drop(columns = ['material_id']) #one value at a time
    else:
        #return dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id']).to_dict("rows")
        dff = dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id'])
    
    #filter by test condition
    if test_condition_value is None:
        return dff.to_dict("rows")
    else:
        test_condition_value = [int(i) for i in test_condition_value]
        print("test_conditions series dtype", dff)
        return dff[dff['test_conditions_id'].isin(test_condition_value)].to_dict("rows")
    
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)