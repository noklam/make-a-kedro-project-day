"""
This is a boilerplate pipeline
generated using Kedro 0.18.3
"""

import logging
from typing import Any, Dict, Tuple
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # visualization library
from chart_studio import plotly
import matplotlib.pyplot as plt # visualization library
import plotly.offline as pyoff
import plotly.graph_objs as go
import warnings
from plotly.offline import init_notebook_mode, iplot # plotly offline mode
warnings.filterwarnings("ignore") # if there is a warning after some codes, this will avoid us to see them.
plt.style.use('ggplot') # style of plots. ggplot is one of the most used style, I also like it.
# Any results you write to the current directory are saved as output.
import numpy as np
import pandas as pd


def clean_data(
    data: pd.DataFrame, start_year: int
) :
    """Cleaning the raw data

    Args:
        data (pd.DataFrame): the raw UFO data
        parameters (Dict[str, Any]): _description_

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]: _description_
    """

    data = data.rename(columns = {'longitude ':'longitude' })
    data["country"].fillna("missing" ,inplace = True)
    data["shape"].fillna("empty" ,inplace = True)
    data['color'] = ["" for x in data.country]
    data["year"] = [int(each.split()[0].split('/')[2]) for each in data.iloc[:, 0]]
    map_plot_data = data[data.year > 2010]
    map_plot_data = map_plot_data[map_plot_data.country != "missing"]
    return map_plot_data

def draw_ufo_map(map_plot_data):
    map_plot_data.color[map_plot_data.country == "us"] = "rgb(0, 116, 217)"
    map_plot_data.color[map_plot_data.country == "gb"] = "rgb(255, 65, 54)"
    map_plot_data.color[map_plot_data.country == "ca"] = "rgb(133, 20, 75)"
    map_plot_data.color[map_plot_data.country == "au"] = "rgb(255, 133, 27)"
    map_plot_data.color[map_plot_data.country == "de"] = "rgb(255, 7, 4)"
    map_plot_data.color[map_plot_data.country == "missing"] = "rgb(255, 255, 255)"

    mapData = [dict(
        type = 'scattergeo',
        lon = map_plot_data.longitude,
        lat = map_plot_data.latitude,
        hoverinfo = 'text',
        text = "Sigth Location: " + map_plot_data.country,
        mode = 'markers',
        marker = dict(
            sizemode = 'area',
            sizeref = 1,
            size= 10 ,
            line = dict(width = 1, color = "white"),
            color = map_plot_data["color"],
            opacity = 0.7),
    )]
    layout = dict(
        title = 'UFO Sightings Between 2011 - 2014',
        hovermode = 'closest',
        width = 1500,
        height = 900,
        geo = dict(showframe = False,
                showland = True,
                showcoastlines = True,
                showcountries = True,
                countrywidth = 1,
                projection = dict(type = 'mercator'),
                landcolor = 'rgb(217, 217, 217)',
                subunitwidth = 1,
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)',
                countrycolor = "rgb(5, 5, 5)")
    )

    fig = go.Figure(data = mapData, layout = layout)
    return fig