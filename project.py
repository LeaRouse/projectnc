import streamlit as st
import streamlit.components.v1 as components
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

# --- CSS PERSONALIZADO ---
st.markdown("""
<style>
/* Fondo con video */
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

/* Contenedor flotante para los botones */
.control-button {
    position: fixed;
    background-color: rgba(30,30,30,0.8);
    color: #f1f1f1;
    border: none;
    border-radius: 14px;
    padding: 12px 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
}

.control-button:hover {
    background-color: rgba(70,70,70,0.9);
    transform: scale(1.05);
}

/* Posiciones específicas */
#btn-left {
    left: 30px;
    top: 50%;
    transform: translateY(-50%);
}

#btn-top-right {
    right: 30px;
    top: 25px;
}

#btn-bottom-right {
    right: 30px;
    bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# --- Insertar video de fondo ---
st.markdown(get_video_html(), unsafe_allow_html=True)

# --- Estado de la página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

# --- BOTONES flotantes personalizados ---
st.markdown(f"""
    <button class="control-button" id="btn-left" onclick="window.parent.location.reload()">🏠 Home</button>
    <form action="#" method="get">
        <button class="control-button" id="btn-top-right" onclick="window.parent.postMessage({{type: 'craft'}}, '*')">🛠️ Craft</button>
    </form>
    <form action="#" method="get">
        <button class="control-button" id="btn-bottom-right" onclick="window.parent.postMessage({{type: 'config'}}, '*')">⚙️ Config</button>
    </form>
""", unsafe_allow_html=True)

# --- Mostrar contenido según selección ---
pagina = st.session_state.pagina

if pagina == "Home":
    st.title("🏠 Home")
    st.write("Bienvenido a **AstroCycle**. Explora todo desde aquí.")
elif pagina == "Craft":
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")
elif pagina == "Configuracion":
    st.header("⚙️ Configuración")
    st.write("Opciones para personalizar tu experiencia.")

