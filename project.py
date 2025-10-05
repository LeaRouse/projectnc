import streamlit as st
from pathlib import Path
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- VIDEO DE FONDO ---
VIDEO_FILE = Path("video.mp4")

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

# --- CSS ---
st.markdown("""
<style>
/* Fondo */
.stApp {
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

/* Barra lateral fija */
.sidebar {
    position: fixed;
    left: 0;
    top: 80px; /* espacio para que no quede tapada por la barra de Streamlit */
    width: 200px;
    height: calc(100% - 100px);
    background-color: rgba(28,28,28,0.85);
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    z-index: 5;
    border-radius: 0 12px 12px 0;
}

/* Botones barra lateral */
.sidebar button {
    display: block;
    margin-bottom: 15px;
    padding: 12px;
    border: none;
    border-radius: 12px;
    background-color: #2a2a2a;
    color: #d0d0d0;
    font-weight: bold;
    text-align: left;
    cursor: pointer;
    transition: 0.2s;
}
.sidebar button:hover {
    background-color: #3a3a3a;
    color: #fff;
}

/* Contenido principal al costado de la barra */
.main-content {
    margin-left: 220px; /* ancho de la barra + margen */
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Insertar video de fondo ---
st.markdown(get_video_html(), unsafe_allow_html=True)

# --- Session state para la página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- Función para cambiar página ---
def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Barra lateral con solo 3 botones (HTML puro) ---
st.markdown(f"""
<div class="sidebar">
    <button onclick="window.parent.postMessage({{type:'Home'}}, '*')">🏠 Home</button>
    <button onclick="window.parent.postMessage({{type:'Craft'}}, '*')">🛠️ Craft</button>
    <button onclick="window.parent.postMessage({{type:'Materiales'}}, '*')">📦 Materiales</button>
</div>
""", unsafe_allow_html=True)

# --- Botones funcionales con Streamlit --- 
# Capturamos los clicks en Streamlit de forma invisible usando botones ocultos
if st.button("🏠 Home", key="home_hidden"):
    cambiar_pagina("Home")
if st.button("🛠️ Craft", key="craft_hidden"):
    cambiar_pagina("Craft")
if st.button("📦 Materiales", key="materiales_hidden"):
    cambiar_pagina("Materiales")

# --- Contenido principal al costado de la barra ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

pagina = st.session_state.pagina

if pagina == "Home":
    st.title("🏠 Home")
    st.write("Bienvenido a **AstroCycle**. Explora todo desde aquí.")
elif pagina == "Craft":
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")
elif pagina == "Materiales":
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")

st.markdown('</div>', unsafe_allow_html=True)
