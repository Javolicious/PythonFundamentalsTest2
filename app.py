import streamlit as st
import pandas as pd
import numpy as np

st.title("Análisis FIFA World Cup 2026")
uploaded_file = st.file_uploader(
"Seleccione el archivo CSV",
type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Archivo cargado correctamente")

    st.subheader("Vista previa")
    st.dataframe(df.head())

    st.subheader("Dimensiones")
    st.write(f"Filas: {df.shape[0]}")
    st.write(f"Columnas: {df.shape[1]}")
else:
    st.warning("Por favor cargue un archivo CSV")
