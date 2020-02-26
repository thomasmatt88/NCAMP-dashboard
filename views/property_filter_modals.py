import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dataframe import property_df

F1tu = dbc.Modal(
                [
                    dbc.ModalHeader("F1tu"),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-F1tu',
                                min=property_df['F1tu (ksi)'].min(),
                                max=property_df['F1tu (ksi)'].max(),
                                step=1,
                                value=[property_df['F1tu (ksi)'].min(), property_df['F1tu (ksi)'].max()]
                            ),
                            html.Div(id='output-container-range-slider-F1tu')
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal_F1tu", className="ml-auto")
                    ),
                ],
                id="property_range_modal_F1tu"
            )

F2tu = dbc.Modal(
                [
                    dbc.ModalHeader("F2tu"),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-F2tu',
                                min=property_df['F2tu (ksi)'].min(),
                                max=property_df['F2tu (ksi)'].max(),
                                step=1,
                                value=[property_df['F2tu (ksi)'].min(), property_df['F2tu (ksi)'].max()]
                            ),
                            html.Div(id='output-container-range-slider-F2tu')
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal_F2tu", className="ml-auto")
                    ),
                ],
                id="property_range_modal_F2tu"
            )
            
E1t = dbc.Modal(
                [
                    dbc.ModalHeader("E1t"),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-E1t',
                                min=property_df['E1t (msi)'].min(),
                                max=property_df['E1t (msi)'].max(),
                                step=1,
                                value=[property_df['E1t (msi)'].min(), property_df['E1t (msi)'].max()]
                            ),
                            html.Div(id='output-container-range-slider-E1t')
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal_E1t", className="ml-auto")
                    ),
                ],
                id="property_range_modal_E1t"
            )