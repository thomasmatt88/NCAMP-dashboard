import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dataframe import property_df, material_df
from models.Dataframe import PropertyDF, MaterialDF

modals = {}
phys_modals = {}

for key, value in PropertyDF.PROPERTIES.items():
    modal = dbc.Modal(
                [
                    dbc.ModalHeader(value),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-' + value,
                                min=property_df[value].min(),
                                max=property_df[value].max(),
                                # step size should depend on range 
                                step=0.1 if property_df[value].min() > 1 else 0.0001,
                                value=[property_df[value].min(), property_df[value].max()]
                            ),
                            html.Div(id='output-container-range-slider-' + value)
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal_" + value, className="ml-auto")
                    ),
                ],
                id="property_range_modal_" + value
            )
    modals[key] = modal

# Tg_modal = dbc.Modal(
#             [
#                 dbc.ModalHeader('Tg'),
#                 dbc.ModalBody(
#                     html.Div([
#                         dcc.RangeSlider(
#                             id='my-range-slider-Tg',
#                             min=material_df['Tg'].min(),
#                             max=material_df['Tg'].max(),
#                             # step size should depend on range 
#                             step=0.1,
#                             value=[material_df['Tg'].min(), material_df['Tg'].max()]
#                         ),
#                         html.Div(id='output-container-range-slider-Tg')
#                     ])
#                 ),
#                 dbc.ModalFooter(
#                     dbc.Button("Close", color = "success", id="close_property_range_modal_Tg", className="ml-auto")
#                 ),
#             ],
#             id="physical_property_range_modal_Tg"
#       )
for key, value in MaterialDF.PROPERTIES.items():
    phys_modal = dbc.Modal(
                [
                    dbc.ModalHeader(value),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-' + value,
                                min=material_df[value].min(),
                                max=material_df[value].max(),
                                # step size should depend on range 
                                step=0.1 if material_df[value].min() > 1 else 0.0001,
                                value=[material_df[value].min(), material_df[value].max()]
                            ),
                            html.Div(id='output-container-range-slider-' + value)
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "success", id="close_property_range_modal_" + value, className="ml-auto")
                    ),
                ],
                id="physical_property_range_modal_" + value
            )
    phys_modals[key] = phys_modal
