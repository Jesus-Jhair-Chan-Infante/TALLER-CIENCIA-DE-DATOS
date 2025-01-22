import streamlit as st

st.title("Calidad de vida a nivel mundial")
st.subheader("Indicadores")
st.markdown("""
            En esta aplicación exploraremos la distribución de diferentes indicadores que nos permiten medir la calidad de vida en diferentes países.  
            Exploraremos los siguientes:
            * Índice de calidad de vida.
            * Índice de poder de compra.
            * Índice de seguridad.
            * Índice de salud.
            * Índice de costo de vida.
            * Razón de precios de la propiedad.
            * Índice de tiempo de desplazamiento.
            * Índice de contaminación.
            * Índice climático.
            """)


st.page_link("Tabla_de_datos.py", label="Siguiente", icon="👉")
