import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

#from other modules
from dataframe import material_df
from app import app
from views.layout import Layout
from data import process_spec, material_spec, material

def Table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            # update this depending on which
            # columns you want to show links for
            # and what you want those links to be
            if col == 'ProcessSpec':
                cell = html.Td(html.A(href = process_spec.link_map[value], children = value))
            elif col == 'MaterialSpec':
                cell = html.Td(html.A(href = material_spec.link_map[value], children = value))
            elif col == 'Material':
                cell = html.Td(html.A(href = material.link_map[value], children = value))
            else:
                cell = html.Td(children=value)
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(
        # Header
        [html.Tr([html.Th(col, className = "Header") for col in dataframe.columns])] +
        [html.Tr(
            [
                html.Th("", className = "Material_Header"), html.Th("", className = "Fiber_Header"), html.Th("", className = "Header"), \
                html.Th("°F", className = "Header"), html.Th("°F", className = "Header"), html.Th("°F", className = "Header"), \
                html.Th("g/m\N{SUPERSCRIPT TWO}", className = "Header"), \
                html.Th("", className = "Header"), html.Th("", className = "Header")
            ]
        )] +
        rows
    )

@app.callback(
    Output('material-table', 'children'), #one output id can have one callback
    [
        Input('material-dropdown', 'value')
    ])
def update_material_table(value):
    dff = material_df
    if value is None:
        return Table(dff[dff['id'] == value].drop(columns = ["id"])) #one value at a time
    if 'all' in value: # if all materials are selected
        return Table(dff.drop(columns = ["id"]))
    else:
        return Table(dff[dff['id'].isin(value)].drop(columns = ["id"]))


#Table(material_df.drop(columns = ["id"]))