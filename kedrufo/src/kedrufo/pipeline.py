"""
This is a boilerplate pipeline
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_data, draw_ufo_map


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=clean_data,
                inputs=["ufo_data", "params:data_start_year"],
                outputs="map_plot_data",

            ),
            node(func=draw_ufo_map,
                 inputs="map_plot_data"),
                 outputs="map_plot_figure"
        ]
    )
