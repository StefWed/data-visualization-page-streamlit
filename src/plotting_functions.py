# plotting functions used in the dogs_in_zurich app

import plotly.express as px
from pathlib import Path
import pandas as pd
import json

# Function for Page 2 and 3 ------------------------------------------------------------------------------------


def plot_linegraphs_zurich(df, x_values, y_values, color=None):

    fig_ = px.line(df,
              x=x_values,
              y=y_values,
              color=color,
              width=800, height=600)

    # Highlight 2020-2022
    fig_.add_vrect(
        x0=2020, x1=2022,
        fillcolor="green",
        opacity=0.5,
        line_width=0)

    # Add annotation for COVID-19
    fig_.add_annotation(
        x=2021.2, y=max(df[y_values]),
        text="COVID-19 Pandemic",
        showarrow=False,
        font=dict(size=12, color="white"),
        xanchor="center", yanchor="bottom")

    # Ensure every year is shown on the x-axis
    all_years = sorted(df[x_values])
    fig_.update_xaxes(
        tickmode="array",      # Force specific tick values
        tickvals=all_years,    # List of years
        )

    return fig_


# Function for Page 4 ---------------------------------------------------------------------------------------------

data_folder = Path("../data")
path_zurich_geojson = data_folder / "stzh.adm_stadtkreise_a.json"

path_csv_zurich_2023 = data_folder / "dogs_zurich_2023_stadtkreis.csv"

df_dogs_2023_stadtkreis = pd.read_csv(path_csv_zurich_2023)
with open(path_zurich_geojson) as f:
    zurich = json.load(f)


def plot_geoscatter_zurich(color=None):
    fig_ = px.choropleth_map(
        df_dogs_2023_stadtkreis,
        geojson=zurich,
        color=color,
        locations="KreisCd",
        featureidkey="properties.name",
        # projection="mercator",
        map_style="carto-positron",
        hover_name="StadtQuartiere",
        color_continuous_scale=[(0, "lightblue"), (1, "darkblue")])

    fig_.update_geos(fitbounds="locations", visible=False)
    fig_.update_layout(map_zoom=11, map_center={"lat": 47.3852, "lon": 8.5269})
    fig_.update_layout(autosize=False, width=800, height=800)

    return fig_
