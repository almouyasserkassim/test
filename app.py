import streamlit as st

st.header("Population totale dans les communes de Seine-Saint-Denis en 2021")

conn = st.connection("sql")

pop_totale = conn.query("SELECT * FROM communes_93.population_totale_2021"
                       )

st.dataframe(pop_totale)
