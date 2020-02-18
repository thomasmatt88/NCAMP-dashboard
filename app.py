import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc

from sqlalchemy import create_engine
import pymysql

app = dash.Dash(__name__)

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

#this element will contain all our other elements 
app.layout = html.Div([
    html.H1("NCAMP Table"),
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
        #columns = [{"name": i, "id": i} for i in df.columns], #don't need id column
        #data = df.to_dict("rows"),
        #sort_action = 'custom',
        #sort_mode = 'single',
        #sort_by = []
    ),
    dcc.Checklist(
        id = 'material-property-checklist', #need to reference for callback
        options = [
            {'label': 'F1tu', 'value': 'F1tu'},
            {'label': 'F2tu', 'value': 'F2tu'},
            {'label': 'E1t', 'value': 'E1t'},
            {'label': 'F1cu', 'value': 'F1cu'},
            {'label': 'F2cu', 'value': 'F2cu'},
            {'label': 'F12su', 'value': 'F12su'},
            {'label': 'F31sbs', 'value': 'F31sbs'},
            {'label': 'CPT', 'value': 'CPT'},
        ]
    ),
    html.Div(
        id = "material-property-selection", #need to reference for callback
    ),
    dash_table.DataTable(
        id = 'material-property-table', #need to reference for callback
        columns = [{"name": i, "id": i} for i in df6.drop(columns = ['material_id']).columns], #don't need id column
        data = df6.drop(columns = ['material_id']).to_dict("rows"),
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
    [Input('material-property-checklist', 'value')])
def update_material_property_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('material-property-table', 'data'), #one output id can have one callback
    [Input('material-property-checklist', 'value'),
    Input('material-property-table', 'sort_by'),
    Input('material-dropdown', 'value')])
def update_material_property_table(property_value, sort_by, material_value):
    if len(sort_by):
        dff = df6.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df6
    
    #dff = df6
    if material_value is None:
        return dff[dff['material_id'] == material_value].drop(columns = ['material_id']).to_dict("rows") #one value at a time
    else:
        return dff[dff['material_id'].isin(material_value)].drop(columns = ['material_id']).to_dict("rows")
    """
    if value is None:
        return dff[dff['id'] == value].to_dict("rows") #one value at a time
    else:
        return dff[dff['id'].isin(value)].to_dict("rows")
    """


if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)