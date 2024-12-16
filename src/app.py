import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

import plotly.graph_objects as go

# Data Set
countries = ['India', 'Australia',
             'Japan', 'America',
             'Russia']

values = [4500, 2500, 1053, 500,
          3200]

# The plot
fig = go.Figure(
    go.Pie(
        labels=countries,
        values=values,
        hoverinfo="label+percent",
        textinfo="value"
    ))

st.header("Pie chart")
st.plotly_chart(fig)