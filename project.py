# app.py
import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #0a0a1a;
        color: #03dffc;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #03dffc !important;
    }
    .sidebar .sidebar-content {
        background-color: #111133;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("🌠 AstroCycle")
opcion = st.sidebar.radio("Navegación", ["Inicio", "Pantalla 1", "Pantalla 2"])

# --- FUNCIONES DE CONTENIDO ---
def mostrar_inicio():
    st.title("Bienvenido a AstroCycle 🌌")
    st.write("Explora el universo desde tu pantalla.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/NASA-HS201427a-HubbleUltraDeepField2014-20140603.jpg", use_container_width=True)

def mostrar1():
    st.header("Pantalla 1")
    st.write("🪐 Aquí va el contenido de la pantalla 1 (planetas, datos, o visualizaciones).")
    st.write("Podrías agregar gráficos, tablas, o incluso imágenes del espacio.")

def mostrar2():
    st.header("Pantalla 2")
    st.write("✨ Aquí va el contenido de la pantalla 2 (constelaciones, simulaciones, etc.)")

# --- MOSTRAR CONTENIDO SEGÚN LA OPCIÓN ---
if opcion == "Inicio":
    mostrar_inicio()
elif opcion == "Pantalla 1":
    mostrar1()
elif opcion == "Pantalla 2":
    mostrar2()
