import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Análisis de Esperanza de Vida en la OCDE", page_icon="📊", layout="wide")

# Título
st.title("Bienvenido al Análisis de Esperanza de Vida en la OCDE")

# Descripción breve
st.markdown(
    "Esta aplicación permite analizar y visualizar los datos de esperanza de vida de los países de la OCDE. "
    "Puedes navegar por las secciones de la aplicación usando el menú de la izquierda."
)

# Sidebar con enlaces a las páginas
st.sidebar.header("Navegación")
st.sidebar.page_link("pages/INTRODUCCION.py", label="📘 Introducción")
st.sidebar.page_link("pages/DISTRIBUCION.py", label="📊 Distribución de la Esperanza de Vida")
st.sidebar.page_link("pages/EVOLUCION.py", label="📈 Evolución de la Esperanza de Vida")