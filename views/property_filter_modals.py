import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dataframe import property_df

modal = dbc.Modal(
                [
                    dbc.ModalHeader("F1tu"),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider',
                                min=property_df['F1tu (ksi)'].min(),
                                max=property_df['F1tu (ksi)'].max(),
                                step=1,
                                value=[property_df['F1tu (ksi)'].min(), property_df['F1tu (ksi)'].max()]
                            ),
                            html.Div(id='output-container-range-slider')
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal", className="ml-auto")
                    ),
                ],
                id="property_range_modal"
            )