from flask import jsonify

#from other modules
from views.layout import Layout
from app import app
import controllers.property_filters
import controllers.material_property_table
import controllers.material_table
import controllers.filter_modals
from dataframe import material_df, property_df

#this element will contain all our other elements 
app.layout = Layout

#app.run_server(debug=True)

@app.server.route('/rawdata/<table>')
def rawdata(table):
    if table == 'material':
        return jsonify(material_df.to_json(orient = 'records'))
    elif table == 'property':
        return jsonify(property_df.to_json(orient = 'records'))
    return "Valid path parameters are 'material' or 'property'"

if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)
