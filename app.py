import streamlit as st


st.header("Population totale dans les communes de Seine-Saint-Denis en 2021")

conn_db_dirfi = st.connection("postgresql")


pop_totale = conn_db_dirfi.query("SELECT * FROM communes_93.population_totale_2021"
                       )

st.dataframe(pop_totale)
