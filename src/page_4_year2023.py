import streamlit as st
import pandas as pd
from pathlib import Path
from plotting_functions import plot_geoscatter_zurich

# Data and GeoJSON -----------------------------------------------------------------------------------------------


data_folder = Path("../data")
path_csv_zurich_2023 = data_folder / "dogs_zurich_2023_stadtkreis.csv"

df_dogs_2023_stadtkreis = pd.read_csv(path_csv_zurich_2023)

# Intro ----------------------------------------------------------------------------------------------------------

st.subheader("Dog Population for the Year 2023 per Stadtkreis", divider="gray")

st.text("While absolute numbers can give a good first impression, it might make sense to add some more statistical "
        "power by working with percentages (like done with the growth rate), or other ratios to compare each Stadtkreis " 
        "- like dog per inhabitant or dog per square meter. Let's do that for the most recent complete data which is" 
        "available, that is for the year 2023. "
        "For the observations regarding the year 2023, the data is plotted into a map. " 
        "One can have a look at the dataframe which is used to plot the following geo graphs by "
        "checking the box:")

if st.checkbox('Show dataframe'):
    df_dogs_2023_stadtkreis


# Plotting absolute numbers ------------------------------------------------------------------------------------------

fig_7 = plot_geoscatter_zurich("AnzahlHunde")
fig_7.update_layout(title={"text" : "Absolute Number of Dogs per Stadtkreis",
                           "font" : {"size" : 20}},)

st.plotly_chart(fig_7)

st.text("What we can see is that Stadtkreis 11 has most registered dogs in absolute numbers, followed by Stadtkreis 7 "
        "and 9. In central Zurich there are rather less registered dogs to find, but again it might make sense to " 
        "normalize to a certain base like dogs per sqkm or dogs per 1000 inhabitants." )


# Plotting per SQKM ------------------------------------------------------------------------------------------------

fig_8 = plot_geoscatter_zurich("HundeProKM2")
fig_8.update_layout(title={"text" : "Dogs Per SQKM For Each Stadtkreis",
                           "font" : {"size" : 20}})
st.plotly_chart(fig_8)

st.text("And that is a totally different picture. In relation to the area, there are more dogs registered in central "
"Zurich. Stadtkreis 11 is now on 4th place. Let's have a look at number of registered dogs per 1000 inhabitants.")


# Plotting per 1000 inhabitants ------------------------------------------------------------------------------------

fig_9 = plot_geoscatter_zurich("HundePer1000EW")
fig_9.update_layout(title={"text" : "Dogs Per 1000 Inhabitants For Each Stadtkreis",
                           "font" : {"size" : 20}})

st.plotly_chart(fig_9)


st.text("And again we get another picture. Stadtkreis 7, 8 and 2 have most registered dogs per 1000 inhabitants. "
        "Stadtkreis 7 has the biggest area of all boroughs in Zurich, while at the same time having half of the number "
        "of the inhabitants of the second biggest borough, which is Stadtkreis 11. So just from the data one might "
        "assume, that Stadtkreis 7 has rather smaller apartment houses, if not lots of single-family homes and lots "
        "of families are having a dog. ")
