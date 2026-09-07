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
        return self.df.isnull().sum().sum()

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

    with tabs[0]:

        st.header("Ítem 1: Información del Dataset")
        st.subheader("Tipos de Datos")

        tipos_df = pd.DataFrame({
            "Columna": df.columns,
            "Tipo de Dato": df.dtypes.astype(str)
            })

        st.dataframe(tipos_df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Filas", df.shape[0])

        with col2:
            st.metric("Columnas", df.shape[1])

        with col3:
            st.metric(
            "Duplicados",
            analizador.contar_duplicados()
        )
        with col4:
            st.metric(
            "Valores Nulos",
            analizador.contar_nulos()
        )



    # =======================================
    # ITEM 2
    # =======================================

    with tabs[1]:
        st.header("Ítem 2: Clasificación de Variables")

        variables_numericas = analizador.obtener_variables_numericas()
        variables_categoricas = analizador.obtener_variables_categoricas()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Variables Numéricas")

            st.metric(
            "Total",
            len(variables_numericas)
            )


        with col2:

            st.subheader("Variables Categóricas")

            st.metric(
            "Total",
            len(variables_categoricas)
            )

    # =======================================
    # ITEM 3
    # =======================================
    
    with tabs[2]:

        st.header("Ítem 3: Estadísticas Descriptivas")

        st.markdown("""En esta sección se presentan las principales medidas estadísticas
        de las variables numéricas del dataset.
        """)

        estadisticas = analizador.obtener_estadisticas()

        st.subheader("Resumen Estadístico")

        st.dataframe(
            estadisticas,
            use_container_width=True
        )

        st.subheader("Seleccionar Variable")

        variable = st.selectbox(
        "Seleccione una variable numérica",
        analizador.obtener_variables_numericas()
        )

        col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Media",
            round(df[variable].mean(), 2)
        )

    with col2:
        st.metric(
            "Mediana",
            round(df[variable].median(), 2)
        )

    with col3:
        st.metric(
            "Mínimo",
            round(df[variable].min(), 2)
        )

    with col4:
        st.metric(
            "Máximo",
            round(df[variable].max(), 2)
        )

    st.subheader("Dispersión")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Desv. Estándar",
            round(df[variable].std(), 2)
        )

    with col2:
        st.metric(
            "Rango",
            round(
                df[variable].max() - df[variable].min(),
                2
            )
        )

    
        st.subheader("Detección Preliminar de Valores Extremos")

        q1 = df[variable].quantile(0.25)
        q3 = df[variable].quantile(0.75)

        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        outliers = df[
            (df[variable] < limite_inferior) |
            (df[variable] > limite_superior)
        ]

        st.write(f"Valores extremos detectados: {len(outliers)}")

        porcentaje = (
            len(outliers) / len(df)
        ) * 100

        st.write(
            f"Porcentaje de outliers: {porcentaje:.2f}%"
        )

    if len(outliers) > 0:
        st.dataframe(
            outliers[[variable]].head(20),
            use_container_width=True
        )

    


# ==================================================
# MENU
# ==================================================

st.sidebar.title("⚽ FIFA World Cup 2026")

menu = st.sidebar.selectbox(
    "Seleccione un módulo",
    [
        "Home",
        "EDA"
    ]
)

if menu == "Home":
    mostrar_home()


elif menu == "EDA":
    mostrar_eda()

