import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dataframe import property_df
from models.Dataframe import PropertyDF

F1tu = dbc.Modal(
                [
                    dbc.ModalHeader("F1tu"),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-F1tu',
                                min=property_df['F1tu'].min(),
                                max=property_df['F1tu'].max(),
                                step=1,
                                value=[property_df['F1tu'].min(), property_df['F1tu'].max()]
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
                                min=property_df['F2tu'].min(),
                                max=property_df['F2tu'].max(),
                                step=1,
                                value=[property_df['F2tu'].min(), property_df['F2tu'].max()]
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
                                min=property_df['E1t'].min(),
                                max=property_df['E1t'].max(),
                                step=1,
                                value=[property_df['E1t'].min(), property_df['E1t'].max()]
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
F1cu = dbc.Modal(
                [
                    dbc.ModalHeader(PropertyDF.PROPERTIES[4]),
                    dbc.ModalBody(
                        html.Div([
                            dcc.RangeSlider(
                                id='my-range-slider-' + PropertyDF.PROPERTIES[4],
                                min=property_df[PropertyDF.PROPERTIES[4]].min(),
                                max=property_df[PropertyDF.PROPERTIES[4]].max(),
                                step=1,
                                value=[
                                    property_df[PropertyDF.PROPERTIES[4]].min(), 
                                    property_df[PropertyDF.PROPERTIES[4]].max()
                                ]
                            ),
                            html.Div(id='output-container-range-slider-' + PropertyDF.PROPERTIES[4])
                        ])
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", color = "secondary", id="close_property_range_modal_" + PropertyDF.PROPERTIES[4], \
                            className="ml-auto")
                    ),
                ],
                id="property_range_modal_" + PropertyDF.PROPERTIES[4]
            )