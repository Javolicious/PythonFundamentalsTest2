import streamlit as st
import pandas as pd
import numpy as np
import io

# ==================================================
# MODULO 1 - HOME
# ==================================================

def mostrar_home():

    st.title("⚽ FIFA World Cup 2026 Player Performance Analysis")

    st.markdown("""
    ## Objetivo del Proyecto

    Desarrollar una aplicación interactiva utilizando Streamlit para realizar
    un Análisis Exploratorio de Datos (EDA) sobre el rendimiento de jugadores
    durante la Copa Mundial FIFA 2026.

    El objetivo es analizar métricas ofensivas, defensivas, físicas y de
    rendimiento para identificar patrones, comparaciones y hallazgos relevantes.
    """)

    st.markdown("---")

    st.subheader("👨‍💻 Datos del Autor")

    st.write("**Nombre:** Javier Artieda Burgos")
    st.write("**Curso:** Especialización Python for Analytics")
    st.write("**Año:** 2026")

    st.markdown("---")

    st.subheader("📊 Acerca del Dataset")

    st.write("""
    El dataset contiene información detallada del desempeño de jugadores
    durante la FIFA World Cup 2026.

    Incluye variables relacionadas con:

    - Datos personales del jugador
    - Información de partidos
    - Métricas ofensivas
    - Métricas defensivas
    - Rendimiento físico
    - Calificaciones generales
    - Estadísticas acumuladas del torneo
    """)

    st.markdown("---")

    st.subheader("🛠 Tecnologías Utilizadas")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Python")
        st.success("Pandas")
        st.success("NumPy")

    with col2:
        st.success("Streamlit")
        st.success("Matplotlib")
        st.success("Seaborn")

    st.markdown("---")

    st.info(
        "Utilice el menú lateral para navegar entre los módulos de la aplicación."
    )

# ==================================================
# MODULO 2 - CARGA DATASET
# ==================================================

def cargar_dataset():

    st.header("📂 Carga del Dataset")

    uploaded_file = st.file_uploader(
        "Seleccione el archivo CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("✅ Archivo cargado correctamente")

        st.subheader("Vista previa del dataset")
        st.dataframe(df.head())

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Filas", df.shape[0])

        with col2:
            st.metric("Columnas", df.shape[1])

        return df

    return None

# ==================================================
# POO
# ==================================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def obtener_variables_numericas(self):
        return self.df.select_dtypes(include=["number"]).columns.tolist()

    def obtener_variables_categoricas(self):
        return self.df.select_dtypes(exclude=["number"]).columns.tolist()

    def obtener_estadisticas(self):
        return self.df.describe()

    def contar_nulos(self):
        return self.df.isnull().sum()

    def contar_duplicados(self):
        return self.df.duplicated().sum()

# ==================================================
# MODULO EDA
# ==================================================

def mostrar_eda():

    df = cargar_dataset()

    if df is None:
        st.warning("Debe cargar un archivo CSV para continuar.")
        return

    analizador = DataAnalyzer(df)

    tabs = st.tabs([
        "Ítem 1",
        "Ítem 2",
        "Ítem 3",
        "Ítem 4",
        "Ítem 5",
        "Ítem 6",
        "Ítem 7",
        "Ítem 8",
        "Ítem 9",
        "Ítem 10"
    ])

    # =======================================
    # ITEM 1
    # =======================================

    with tabsst.header("Ítem 1: Información General del Dataset"):

        buffer = io.StringIO()

        df.info(buf=buffer)

        info_text = buffer.getvalue()

        st.subheader("Información General")
        st.text(info_text)

        st.subheader("Valores Nulos")

        st.dataframe(
            analizador.contar_nulos().reset_index().rename(
                columns={
                    "index": "Variable",
                    0: "Nulos"
                }
            )
        )

        st.subheader("Registros Duplicados")

        st.write(
            f"Cantidad de registros duplicados: "
            f"{analizador.contar_duplicados()}"
        )

# ==================================================
# MENU
# ==================================================

st.sidebar.title("⚽ FIFA World Cup 2026")

menu = st.sidebar.selectbox(
    "Seleccione un módulo",
    [
        "Home",
        "Carga del Dataset",
        "EDA"
    ]
)

if menu == "Home":
    mostrar_home()

elif menu == "Carga del Dataset":
    cargar_dataset()

elif menu == "EDA":
    mostrar_eda()
`
