import streamlit as st
import pandas as pd

# Función para calcular métricas estadísticas
def calcular_metricas(df):
    return {
        "Promedio": round(df["Life_exp"].mean(), 2),
        "Desviación Estándar": round(df["Life_exp"].std(), 2),
        "Mínimo": df["Life_exp"].min(),
        "Máximo": df["Life_exp"].max()
    }

# Función optimizada para mostrar métricas
def mostrar_metricas(metricas, titulo):
    st.subheader(titulo)
    cols = st.columns(4)
    nombres_metricas = ["Promedio", "Desviación Estándar", "Mínimo", "Máximo"]
    
    for col, nombre in zip(cols, nombres_metricas):
        col.metric(nombre, metricas[nombre])

# Función que evita mostrar métricas si el DataFrame está vacío
def mostrar_metricas_si_existe(df, titulo):
    if not df.empty:
        metricas = calcular_metricas(df)
        mostrar_metricas(metricas, titulo)
    else:
        st.warning(f"No hay datos disponibles para: {titulo}")

# Cargar datos
df = pd.read_csv("OECD.csv", sep=",")

# Título
st.title("Análisis de Expectativa de Vida en la OECD")

# Información
st.markdown("Observaremos los datos de expectativa de vida en la OECD, identificando la recolección de información por género y membresía en la OECD.")

# Selección de año
year = st.radio("Seleccione el año", options=range(2015, 2024), index=8)

# Filtros de agrupamiento
st.write("Opciones de filtrado:")
filter_oecd = st.checkbox("Diferenciar por membresía en la OCDE")
filter_gender = st.checkbox("Diferenciar por género")

# Filtrar datos por año
df_year = df[df["Year"] == year]

# Diccionario con los filtros aplicados
filtros_aplicados = {
    "Métricas para todos los países": df_year[df_year["Gender"] == "Total"],
    "Métricas para países miembros de la OCDE": df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == True)],
    "Métricas para países no miembros": df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == False)],
    "Métricas para Hombres": df_year[df_year["Gender"] == "Male"],
    "Métricas para Mujeres": df_year[df_year["Gender"] == "Female"],
    "Hombres - OCDE": df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == True)],
    "Hombres - No OCDE": df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == False)],
    "Mujeres - OCDE": df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == True)],
    "Mujeres - No OCDE": df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == False)]
}

# Mostrar métricas según los filtros seleccionados
if not filter_oecd and not filter_gender:
    mostrar_metricas_si_existe(filtros_aplicados["Métricas para todos los países"], "Métricas para todos los países")

if filter_oecd and not filter_gender:
    mostrar_metricas_si_existe(filtros_aplicados["Métricas para países miembros de la OCDE"], "Métricas para países miembros de la OCDE")
    mostrar_metricas_si_existe(filtros_aplicados["Métricas para países no miembros"], "Métricas para países no miembros")

if not filter_oecd and filter_gender:
    mostrar_metricas_si_existe(filtros_aplicados["Métricas para Hombres"], "Métricas para Hombres")
    mostrar_metricas_si_existe(filtros_aplicados["Métricas para Mujeres"], "Métricas para Mujeres")

if filter_oecd and filter_gender:
    st.subheader("Métricas por género y membresía en la OCDE")
    mostrar_metricas_si_existe(filtros_aplicados["Hombres - OCDE"], "Hombres - OCDE")
    mostrar_metricas_si_existe(filtros_aplicados["Hombres - No OCDE"], "Hombres - No OCDE")
    mostrar_metricas_si_existe(filtros_aplicados["Mujeres - OCDE"], "Mujeres - OCDE")
    mostrar_metricas_si_existe(filtros_aplicados["Mujeres - No OCDE"], "Mujeres - No OCDE")



