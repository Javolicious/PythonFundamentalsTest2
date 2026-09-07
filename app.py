import pandas as pd
import streamlit as st

st.title("Análisis FIFA World Cup 2026")
archivo = st.file_uploader(
"Selecciona el archivo FIFA",
type=["csv"])
 
if archivo is not None:
st.success("Archivo cargado correctamente")
