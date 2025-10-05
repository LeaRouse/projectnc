import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

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

st.markdown(get_video_html(), unsafe_allow_html=True)

# --- CSS ---
st.markdown("""
<style>
.stApp {background: transparent !important; color: #d0d0d0 !important;}
video#bgvid {
    position: fixed; top: 50%; left: 50%;
    min-width: 100%; min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover; z-index: -3;
    filter: brightness(0.65) contrast(1.05);
}
.bg-overlay {position: fixed; inset: 0; background: rgba(0,0,0,0.45); z-index: -2;}

/* Barra lateral */
.sidebar {
    position: fixed; left: 0; top: 80px;
    width: 200px; height: calc(100% - 100px);
    background-color: rgba(28,28,28,0.85);
    padding: 20px; display: flex; flex-direction: column;
    align-items: stretch; z-index: 5; border-radius: 0 12px 12px 0;
}
.sidebar button {
    display: block; margin-bottom: 15px; padding: 12px;
    border: none; border-radius: 12px;
    background-color: #2a2a2a; color: #d0d0d0;
    font-weight: bold; text-align: left; cursor: pointer;
    transition: 0.2s;
}
.sidebar button:hover {background-color: #3a3a3a; color: #fff;}
.sidebar button.active {background-color: #505050; color: #fff;}

/* Contenido principal */
.main-content {margin-left: 220px; padding: 20px;}
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- HTML barra lateral con botones que actualizan st.session_state vía postMessage ---
sidebar_html = f"""
<div class="sidebar">
    <button id="btn-home" class="{'active' if st.session_state.pagina=='Home' else ''}">🏠 Home</button>
    <button id="btn-craft" class="{'active' if st.session_state.pagina=='Craft' else ''}">🛠️ Craft</button>
    <button id="btn-materiales" class="{'active' if st.session_state.pagina=='Materiales' else ''}">📦 Materiales</button>
</div>

<script>
const send_page = (page) => {{
    const streamlitEvent = new CustomEvent("streamlit:custom", {{detail: page}});
    document.dispatchEvent(streamlitEvent);
}};

document.getElementById("btn-home").onclick = () => send_page("Home");
document.getElementById("btn-craft").onclick = () => send_page("Craft");
document.getElementById("btn-materiales").onclick = () => send_page("Materiales");
</script>
"""

# --- Componente HTML para la barra lateral ---
components.html(sidebar_html, height=0, width=0)

# --- Listener en Streamlit ---
# Cada vez que se dispara un CustomEvent, actualizamos st.session_state
if 'page_event' not in st.session_state:
    st.session_state.page_event = None

# Usamos un pequeño truco con componentes para recibir mensajes
components.html("""
<script>
window.addEventListener('message', event => {
    if (event.data.type === 'changePage') {
        window.parent.postMessage(event.data.page, "*");
    }
});
</script>
""", height=0, width=0)

# --- Contenido principal ---
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
