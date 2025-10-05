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

/* Botones flotantes */
.control-button {
    position: fixed;
    background-color: rgba(30,30,30,0.85);
    color: #f1f1f1;
    border: none;
    border-radius: 14px;
    padding: 12px 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
    width: 120px;
    text-align: left;
}
.control-button:hover {
    background-color: rgba(70,70,70,0.95);
    transform: scale(1.05);
}

/* Botones izquierda (vertical) */
#btn-left1 { left: 20px; top: 40%; }
#btn-left2 { left: 20px; top: 50%; }
#btn-left3 { left: 20px; top: 60%; }

/* Botones derecha */
#btn-top-right { right: 20px; top: 80px; }  /* alejado del header de Streamlit */
#btn-bottom-right { right: 20px; bottom: 30px; }

</style>
""", unsafe_allow_html=True)

# --- Video de fondo ---
st.markdown(get_video_html(), unsafe_allow_html=True)

# --- Session state para página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Botones izquierda ---
st.markdown(f"""
<button class="control-button" id="btn-left1" onclick="window.parent.postMessage({{type: 'Home'}}, '*')">🏠 Home</button>
<button class="control-button" id="btn-left2" onclick="window.parent.postMessage({{type: 'Craft'}}, '*')">🛠️ Craft</button>
<button class="control-button" id="btn-left3" onclick="window.parent.postMessage({{type: 'Materiales'}}, '*')">📦 Materiales</button>
""", unsafe_allow_html=True)

# --- Botones derecha ---
st.markdown(f"""
<button class="control-button" id="btn-top-right" onclick="window.parent.postMessage({{type: 'Especificaciones'}}, '*')">⚙️ Especificaciones</button>
<button class="control-button" id="btn-bottom-right" onclick="window.parent.postMessage({{type: 'Configuracion'}}, '*')">🧩 Configuración</button>
""", unsafe_allow_html=True)

# --- Capturar los mensajes de los botones ---
components.html("""
<script>
window.addEventListener('message', (event) => {
    const type = event.data.type;
    if (type) {
        document.dispatchEvent(new CustomEvent('updatePagina', {detail: type}));
    }
});
</script>
""", height=0, width=0)

# Escuchar en Streamlit
if 'last_event' not in st.session_state:
    st.session_state.last_event = None

# Detectar cambio usando button clicks tradicionales de Streamlit
buttons = {
    "Home": "🏠 Home",
    "Craft": "🛠️ Craft",
    "Materiales": "📦 Materiales",
    "Especificaciones": "⚙️ Especificaciones",
    "Configuracion": "🧩 Configuración"
}

for key in buttons:
    if st.button(buttons[key]):
        cambiar_pagina(key)

# --- Contenido dinámico ---
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
elif pagina == "Especificaciones":
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
elif pagina == "Configuracion":
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
