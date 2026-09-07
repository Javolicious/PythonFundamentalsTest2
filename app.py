import streamlit as st
import pandas as pd
import numpy as np



#Modulo 1 Presentación
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
    - Información de los partidos
    - Métricas ofensivas
    - Métricas defensivas
    - Rendimiento físico
    - Calificaciones y desempeño general
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
        "Utilice el menú lateral para navegar entre los diferentes módulos del análisis."
    )
    



menu = st.sidebar.selectbox(
    "Seleccione un módulo",
    ["Home", "Carga del Dataset", "EDA"]
)

if menu == "Home":
    mostrar_home()

#Modulo 1 Presentación
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
    - Información de los partidos
    - Métricas ofensivas
    - Métricas defensivas
    - Rendimiento físico
    - Calificaciones y desempeño general
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
        "Utilice el menú lateral para navegar entre los diferentes módulos del análisis."
    )
    
uploaded_file = st.file_uploader(
"Seleccione el archivo CSV",
type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Archivo cargado correctamente")

    st.subheader("Vista del dataset")
    st.dataframe(df.head())

    st.subheader("Dimensiones")
    st.write(f"Filas: {df.shape[0]}")
    st.write(f"Columnas: {df.shape[1]}")
else:
    st.warning("Por favor cargue un archivo CSV")


#MENU
menu = st.sidebar.selectbox(
    "Seleccione un módulo",
    ["Home", "Carga del Dataset", "EDA"]
)

if menu == "Home":
    mostrar_home()
