import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide"
)

st.markdown("""
<style>
/* Fondo principal completo */
.stApp, .css-18e3th9, .css-1d391kg, .block-container {
    background-color: #0a0a1a !important;
    color: #a0c4ff !important;
}

/* Barra lateral */
section[data-testid="stSidebar"] {
    background-color: #1a1a2e !important;
    border-radius: 20px;
    padding: 20px;
    height: 100vh;
}

/* Ocultar botón de colapso */
button[title="Collapse"] {
    display: none;
}

/* Título lateral */
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #a0c4ff;
    text-align: center;
    margin-bottom: 25px;
}

/* Botones del menú: todos iguales */
.stButton>button {
    display: block;
    width: 100%;
    margin-bottom: 15px;
    padding: 12px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    color: #cfd9e0;
    background-color: #2b2b44;
    transition: 0.2s;
    text-align: left;
    cursor: pointer;
}

/* Hover */
.stButton>button:hover {
    background-color: #3a3a5c;
    color: #ffffff;
    transform: scale(1.02);
}

/* Textos principales */
h1, h2, h3, h4, p, span {
    color: #a0c4ff !important;
}
</style>
""", unsafe_allow_html=True)

# --- Menú lateral ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

# Botones
st.sidebar.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
st.sidebar.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
st.sidebar.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))
st.sidebar.button("⚙️ Especificaciones", on_click=cambiar_pagina, args=("Especificaciones",))
st.sidebar.button("🧩 Configuración", on_click=cambiar_pagina, args=("Configuracion",))

# --- Contenido ---
if st.session_state.pagina == "Home":
    st.title("🏠 Home")
    st.write("Bienvenido a AstroCycle. Explora todo desde aquí.")
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg",
        use_container_width=True
    )

elif st.session_state.pagina == "Craft":
    st.header("🛠️ Craft")
    st.write("Contenido relacionado a la construcción y fabricación.")

elif st.session_state.pagina == "Materiales":
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")

elif st.session_state.pagina == "Especificaciones":
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)

elif st.session_state.pagina == "Configuracion":
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
