import streamlit as st
import pandas as pd
from pathlib import Path
from plotting_functions import plot_linegraphs_zurich
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Data Set ---------------------------------------------------------------------

data_folder = Path("../data")
csv_annual_numbers_path = data_folder / "dogs_zurich_annual_district.csv"

df_dogs_annual_by_district = pd.read_csv(csv_annual_numbers_path)

# Intro ----------------------------------------------------------------

st.subheader("Development of Dog Population per Stadtkreis", divider="gray")

st.text("The following plots show the development of the dog population in Zurich per Stadtkreis, spanning the years "
        "2015-2024. The Covid19-Pandemic is visible, but it shows as well, that it developed differently over "
        "the two years 2020 - 2021 for the respective Stadtkreis (borough). "
        "One can have a look at the dataframe which is used to plot the following line graphs by checking the box:")

if st.checkbox('Show dataframe'):
    df_dogs_annual_by_district


# Plotting absolute number for each Satdkreis

fig_3 = plot_linegraphs_zurich(df_dogs_annual_by_district,
                               "StichtagDatJahr",
                               "AnzahlHundeStadtkreis",
                               "KreisCd")

fig_3.update_layout(
    title="Absolute Number of Dogs in Zurich per Stadtkreis (2015 - 2024)",
    xaxis_title="Year",
    yaxis_title="Count")

fig_3.update_layout(
    legend_title="Stadtkreis",
    autosize=False,
    width=900,
    height=800,)

st.plotly_chart(fig_3)

# Subplots for each Stadtkreis -----------------------------------------------------------------------------------

rows = 4
cols = 3

# Get unique districts
districts = df_dogs_annual_by_district["KreisCd"].unique()

# Get y-min and y-max to be able to define same interval for y-axis for all plots
y_min = df_dogs_annual_by_district["WachstumsrateHundeStadtkreis"].min()
y_max = df_dogs_annual_by_district["WachstumsrateHundeStadtkreis"].max()

# Create subplots: one plot per district
fig_5 = make_subplots(
    rows=rows, cols=cols,
    shared_xaxes=True,
    shared_yaxes=True,
    subplot_titles=[f"Stadtkreis {district}" for district in districts])  # Titles for each subplot

# Add a line trace for each district in its respective subplot
for i, district in enumerate(districts):
    district_data = df_dogs_annual_by_district[df_dogs_annual_by_district["KreisCd"] == district]  # Filter data for the district
    row = (i // cols) + 1  # Determine the row number
    col = (i % cols) + 1   # Determine the column number
    fig_5.add_trace(
        go.Scatter(
            x=district_data["StichtagDatJahr"],
            y=district_data["WachstumsrateHundeStadtkreis"],
            mode="lines+markers",
            #name=f"District {district}"
        ),
        row=row, col=col)  # Add to the correct subplot
    all_years = sorted(df_dogs_annual_by_district["StichtagDatJahr"])
    fig_5.update_xaxes(title="Year", tickmode="array", tickvals=all_years, showticklabels=True)
    fig_5.update_yaxes(title="Annual Growth Rate")

    fig_5.add_vrect(
    x0="2020", x1="2022",
    fillcolor="green", opacity=0.5, line_width=0,
    xref=f"x{i+1}", yref=f"y{i+1}"  # Specify the exact axis reference
    )


# Update layout
fig_5.update_layout(
    height=300 * rows,  # Adjust the height of the figure based on the number of subplots
    width=500 * cols,
    title="Annual Growth Rate of Number of Dogs in Each Stadtkreis (2015 - 2024)",
    showlegend=False)             # Disable legend (optional, since subplot titles suffice)

# here we define the y-axis interval for all plots, rows to be the same
fig_5.update_yaxes(range=[y_min-1, y_max+1])

st.plotly_chart(fig_5)