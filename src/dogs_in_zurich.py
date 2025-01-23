import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

import plotly.graph_objects as go
import plotly.express as px

st.header("Trends in Urban Population: Dogs in Zurich")

# Data Sets -------------------------------------------------------------

# Load dataset dogs_zurich_2015-2024_annual_numbers
data_folder = Path("../data")
csv_annual_numbers_path = data_folder / "dogs_zurich_2015-2024_annual_numbers.csv"

df_dogs_zurich_annual = pd.read_csv(csv_annual_numbers_path)
df_dogs_zurich_annual.StichtagDatJahr = df_dogs_zurich_annual.StichtagDatJahr.astype(str)




# The plots and observing ----------------------------------------------------------------

st.subheader("Development of Dog Population in Zurich 2015-2024", divider="gray")

st.text("The following plots show the development of the dog population in Zurich as a whole, spanning the years "
        "2015-2024. One can have a look at the dataframe which is used to plot the line graphs by checking the box:")

if st.checkbox('Show dataframe'):

    df_dogs_zurich_annual

# Plot no 1: absolute number of dogs in Zurich 2015-2024
fig_1 = px.line(df_dogs_zurich_annual,
              x="StichtagDatJahr",
              y = "AbsoluteNumber",
              width=800, height=600)

# Update layout (title and axis labels)
fig_1.update_layout(
    title="Absolute Number of Dogs in Zurich (2015 - 2024)",
    xaxis_title="Year",
    yaxis_title="Number of Dogs")

# Highlight 2020-2022
fig_1.add_vrect(
    x0=2020, x1=2022,
    fillcolor="green",
    opacity=0.4,
    line_width=0)

# Add annotation for COVID-19
fig_1.add_annotation(
    x=2020.5, y=max(df_dogs_zurich_annual["AbsoluteNumber"]),
    text="COVID-19 Pandemic",
    showarrow=False,
    font=dict(size=12, color="white"),
    xanchor="center", yanchor="bottom")

# Ensure every year is shown on the x-axis
all_years = sorted(df_dogs_zurich_annual['StichtagDatJahr'])
fig_1.update_xaxes(
    tickmode="array",      # Force specific tick values
    tickvals=all_years,    # List of years
    )

st.plotly_chart(fig_1)

st.text("One can observe a decline in number of dogs from 2015 to 2016. But after that the absolute number of dogs "
        "raises year by year. There is an obvious stronger raise in numbers for the years 2020-2022, when Coronavirus "
        "hit. It is known that people bought/ adpoted more animals in general during that time.\n\n"
        "Obviously, both could be due to an increasing (human) population in Zurich (overall raise in human "
        "population, stronger raise in human population for 2020-2022). If one checks the dataframe, "
        "an increasing human population can in fact be observed. So rather than working with absolute numbers, have a "
        "look at the development of number of dogs per 1000 inhabitants.")

fig_2 = px.line(df_dogs_zurich_annual,
              x="StichtagDatJahr",
              y = "DogsPer1000Inhabitants",
              width=800, height=600)

# Update layout (title and axis labels)
fig_2.update_layout(
    title="Number of Dogs Per 1000 Inhabitants in Zurich (2015 - 2024)",
    xaxis_title="Year",
    yaxis_title="Dogs Per 1000 Inhabitants")

# Highlight 2020-2022
fig_2.add_vrect(
    x0=2020, x1=2022,
    fillcolor="green",
    opacity=0.4,
    line_width=0)

# Add annotation for COVID-19
fig_2.add_annotation(
    x=2020.5, y=max(df_dogs_zurich_annual["DogsPer1000Inhabitants"]),
    text="COVID-19 Pandemic",
    showarrow=False,
    font=dict(size=12, color="white"),
    xanchor="center", yanchor="bottom")

# Ensure every year is shown on the x-axis
all_years = sorted(df_dogs_zurich_annual["StichtagDatJahr"])
fig_2.update_xaxes(
    tickmode="array",      # Force specific tick values
    tickvals=all_years,    # List of years
    )

st.plotly_chart(fig_2)