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
    /* Fondo del cuerpo principal */
    [data-testid="stAppViewContainer"] {
        background-color: #0a0a1a;
    }

    /* Fondo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #111133;
    }

    /* Color de texto general */
    html, body, [class*="st-"] {
        color: #03dffc !important;
        font-family: 'Arial', sans-serif;
    }

    /* Colores de títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #03dffc !important;
        font-weight: bold;
    }

    /* Quita la barra blanca superior */
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("🌠 AstroCycle")
opcion = st.sidebar.radio("Navegación", ["Inicio", "Pantalla 1", "Pantalla 2"])

# --- FUNCIONES DE CONTENIDO ---
def mostrar_inicio():
    st.title("Bienvenido a AstroCycle 🌌")
    st.write("Explora el universo desde tu pantalla.")
    # Si quieres una imagen de fondo espacial:
    # st.image("ASA-HS201427a-HubbleUltraDeepField2014-20140603.jpg", use_container_width=True)

def mostrar1():
    st.header("Pantalla 1")
    st.write("🪐 Aquí va el contenido de la pantalla 1")

def mostrar2():
    st.header("Pantalla 2")
    st.write("✨ Aquí va el contenido de la pantalla 2")

# --- MOSTRAR CONTENIDO SEGÚN LA OPCIÓN ---
if opcion == "Inicio":
    mostrar_inicio()
elif opcion == "Pantalla 1":
    mostrar1()
elif opcion == "Pantalla 2":
    mostrar2()






