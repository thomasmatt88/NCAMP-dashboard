import dash
from dash.dependencies import Input, Output

#from other modules
from app import app
from views.layout import Layout
from ml.recommendation import similar_material
from dataframe import mdf

@app.callback(
    Output('material-recommendation', 'children'), #one output id can have one callback
    [
        Input('material-dropdown', 'value')
    ])
def return_material_recommendation(value):
    # None is not easy to process
    value = [] if value is None else value
    
    if len(value) == 1 and value[0] != "all":
        return "You may also be interested in {}.".format(similar_material(mdf["Material"][value[0]]))

    return ""
