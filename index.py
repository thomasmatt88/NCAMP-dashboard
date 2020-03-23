#from other modules
from views.layout import Layout
from app import app
import controllers.property_filters
import controllers.physical_property_filters
import controllers.material_property_table
import controllers.material_table
import controllers.filter_modals
import controllers.filter_selections_div

#this element will contain all our other elements 
app.layout = Layout

#app.run_server(debug=True)


if __name__ == '__main__':
    #don't use debug = True on production server
    app.run_server(debug=True)
