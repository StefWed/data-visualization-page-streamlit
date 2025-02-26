import streamlit as st

intro_page = st.Page("page_1_intro.py", title="Introduction to Dogs in Zurich Dataset")
first_graphs = st.Page("page_2_first_graphs.py", title="First Impressions")
stadtkreise = st.Page("page_3_stadtkreis.py", title="Dog Population in Each Stadtkreis")
year_2023 = st.Page("page_4_year2023.py", title="Dog Population in the Year 2023")

pg = st.navigation([intro_page, first_graphs, stadtkreise, year_2023])
st.set_page_config(page_title="Dogs in Zurich")
pg.run()
