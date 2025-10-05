import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# --- Configuración ---
st.set_page_config(page_title="AstroCycle 🌌", layout="wide")

# --- Video de fondo ---
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
video#bgvid {position: fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform: translate(-50%, -50%); object-fit: cover; z-index:-3; filter: brightness(0.65) contrast(1.05);}
.bg-overlay {position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2;}

/* Botones izquierda (vertical) */
.left-btn {
    position: fixed; left:20px; width:120px; padding:12px 18px;
    border-radius:14px; border:none; font-weight:bold; cursor:pointer;
    color:#f1f1f1; background-color: rgba(30,30,30,0.85); text-align:left;
    transition: all 0.25s ease; z-index:5;
}
.left-btn:hover {background-color: rgba(70,70,70,0.95); transform: scale(1.05);}
#btn-left1 {top:40%;}
#btn-left2 {top:50%;}
#btn-left3 {top:60%;}

/* Contenido principal */
.main-content {margin-left:160px; margin-right:160px; padding:20px;}
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Botones flotantes izquierda ---
st.markdown(f"""
<button class="left-btn" id="btn-left1" onclick="window.parent.postMessage({{type: 'Home'}}, '*')">🏠 Home</button>
<button class="left-btn" id="btn-left2" onclick="window.parent.postMessage({{type: 'Craft'}}, '*')">🛠️ Craft</button>
<button class="left-btn" id="btn-left3" onclick="window.parent.postMessage({{type: 'Materiales'}}, '*')">📦 Materiales</button>
""", unsafe_allow_html=True)

# --- Botones derecha (NO TOCAR) ---
# Ya estaban en tu código y funcionan, no los modificamos

# --- Capturar mensajes de botones izquierda ---
components.html("""
<script>
window.addEventListener('message', (event) => {
    const type = event.data.type;
    if(type) {
        document.dispatchEvent(new CustomEvent('updatePagina', {detail: type}));
    }
});
</script>
""", height=0, width=0)

# --- Streamlit button fallback para cambiar página ---
buttons = {
    "Home": "🏠 Home",
    "Craft": "🛠️ Craft",
    "Materiales": "📦 Materiales"
}

for key in buttons:
    if st.button(buttons[key], key=f"left_{key}"):
        cambiar_pagina(key)

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
elif pagina == "Especificaciones":
    st.header("ℹ️ Acerca de / Especificaciones")
    st.write("Detalles técnicos del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
elif pagina == "Configuracion":
    st.header("⚙️ Configuración")
    st.write("Opciones de configuración de la app.")

st.markdown('</div>', unsafe_allow_html=True)
