import streamlit as st
import pandas as pd
from pathlib import Path
from plotting_functions import plot_linegraphs_zurich

import plotly.graph_objects as go
import plotly.express as px

st.header("Trends in Urban Population: Dogs in Zurich")

# Data Set -------------------------------------------------------------

# Load dataset dogs_zurich_2015-2024_annual_numbers
data_folder = Path("../data")
csv_annual_numbers_path = data_folder / "dogs_zurich_2015-2024_annual_numbers.csv"

df_dogs_zurich_annual = pd.read_csv(csv_annual_numbers_path)
df_dogs_zurich_annual.StichtagDatJahr = df_dogs_zurich_annual.StichtagDatJahr.astype(str)


# Intro ----------------------------------------------------------------

st.subheader("Development of Dog Population in Zurich 2015-2024", divider="gray")

st.text("The following plots show the development of the dog population in Zurich as a whole, spanning the years "
        "2015-2024. There is a focus on the time of the Covid19-Pandemic, trying to answer the question if a "
        "difference can be observed for that time period. "
        "One can have a look at the dataframe which is used to plot the following line graphs by checking the box:")

if st.checkbox('Show dataframe'):
    df_dogs_zurich_annual


# plot absolute number of dogs ---------------------------------------------

fig_1 = plot_linegraphs_zurich(df_dogs_zurich_annual, "StichtagDatJahr", "AnzahlHunde")
fig_1.update_layout(
    title="Absolute Number of Dogs in Zurich (2015 - 2024)",
    xaxis_title="Year",
    yaxis_title="Count")

st.plotly_chart(fig_1)

st.text("One can observe a decline in number of dogs from 2015 to 2016. But after that the absolute number of dogs "
        "raises year by year. There is an obvious stronger raise in numbers for the years 2020-2022, when Coronavirus "
        "hit. It is known that people bought/ adopted more animals in general during that time.\n\n"
        "Both could be due to an increasing (human) population in Zurich (both meaning overall raise in human "
        "population, and stronger raise in human population for 2020-2022). If one checks the dataframe, "
        "an increasing human population can in fact be observed. So rather than working with absolute numbers, have a "
        "look at the development of number of dogs per 1000 inhabitants.")


# plot number of dogs per 1000 inhabitants 2015-2024 -------------------------

fig_2 = plot_linegraphs_zurich(df_dogs_zurich_annual, "StichtagDatJahr", "HundePer1000EW")
fig_2.update_layout(
    title="Number of Dogs per 1000 Inhabitants in Zurich (2015 - 2024)",
    xaxis_title="Year",
    yaxis_title="Count")

st.plotly_chart(fig_2)

st.text("Regarding the changes of number of dogs per 1000 inhabitants from 2015-2024, on can still observe both: an " 
        "overall increase throughout the years plus a stronger raise for the years of the pandemic.")
