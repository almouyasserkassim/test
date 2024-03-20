import streamlit as st
import pyodbc

st.header("Population totale dans les communes de Seine-Saint-Denis en 2021")

@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

pop_totale = conn.query("SELECT * FROM communes_93.population_totale_2021"
                       )

st.dataframe(pop_totale)
