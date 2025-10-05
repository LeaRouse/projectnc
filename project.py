import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide"
)

# --- VIDEO DE FONDO ---
VIDEO_FILE = Path("video.mp4")  # tu archivo se llama video.mp4

def get_video_html():
    if VIDEO_FILE.exists():
        data = VIDEO_FILE.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    else:
        return "<!-- No se encontró video.mp4 -->"

# --- CSS PERSONALIZADO ---
st.markdown("""
<style>
/* Fondo principal con video */
.stApp, .css-18e3th9, .css-1d391kg, .block-container {
    background: transparent !important; 
    color: #d0d0d0 !important;
}

video#bgvid {
    position: fixed;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: -3;
    filter: brightness(0.65) contrast(1.05);
}

.bg-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: -2;
}

/* Barra lateral */
section[data-testid="stSidebar"] {
    background-color: rgba(28,28,28,0.85) !important;
    border-radius: 20px;
    padding: 20px;
    position: relative;
    height: 100vh;
    overflow: visible !important;
}

/* Ocultar botón de colapso */
button[title="Collapse"] {
    display: none;
}

/* Título lateral */
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #e0e0e0;
    text-align: center;
    margin-bottom: 25px;
}

/* Botones del menú */
.stButton>button {
    display: block;
    width: 100%;
    margin-bottom: 15px;
    padding: 12px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    color: #d0d0d0;
    background-color: #2a2a2a;
    transition: 0.2s;
    text-align: left;
    cursor: pointer;
}

.stButton>button:hover {
    background-color: #3a3a3a;
    color: #ffffff;
    transform: scale(1.02);
}

/* Textos principales */
h1, h2, h3, h4, p, span {
    color: #d0d0d0 !important;
}
</style>
""", unsafe_allow_html=True)

# --- Insertar video de fondo ---
st.markdown(get_video_html(), unsafe_allow_html=True)

# --- Menú lateral ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- Navegación ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

st.sidebar.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
st.sidebar.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
st.sidebar.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))
st.sidebar.button("⚙️ Especificaciones", on_click=cambiar_pagina, args=("Especificaciones",))
st.sidebar.button("🧩 Configuración", on_click=cambiar_pagina, args=("Configuracion",))

# --- Contenido según página ---
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
