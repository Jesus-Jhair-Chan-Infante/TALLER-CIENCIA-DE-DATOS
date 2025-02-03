import streamlit as st

# Configurar el diseño de la página
st.set_page_config(page_title="Aplicación de Análisis", layout="wide", page_icon="📊")

# Aplicar estilo personalizado
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
        .stTitle {
            color: #2E3B4E;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

pg = st.navigation([
    st.Page("INTRODUCCION.py"),
    st.Page("DISTRIBUCION.py"),
    st.Page("EVOLUCION.py")
])

pg.run()
