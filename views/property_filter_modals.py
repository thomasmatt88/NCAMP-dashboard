import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dataframe import property_df
from models.Dataframe import PropertyDF

modals = {}

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