import streamlit as st
from pathlib import Path
import base64

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

/* Botones flotantes */
.floating-btn {
    position: fixed; z-index:999; width:120px; padding:12px 18px;
    border-radius:14px; border:none; font-weight:bold; cursor:pointer;
    color:#f1f1f1; background-color: rgba(30,30,30,0.85); text-align:left;
    transition: all 0.25s ease;
}
.floating-btn:hover {background-color: rgba(70,70,70,0.95); transform: scale(1.05);}

/* Izquierda */
#btn-left1 {left:20px; top:40%;}
#btn-left2 {left:20px; top:50%;}
#btn-left3 {left:20px; top:60%;}

/* Derecha */
#btn-top-right {right:20px; top:80px;}
#btn-bottom-right {right:20px; bottom:30px;}

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
if st.button("🏠 Home", key="btn-left1"):
    cambiar_pagina("Home")
if st.button("🛠️ Craft", key="btn-left2"):
    cambiar_pagina("Craft")
if st.button("📦 Materiales", key="btn-left3"):
    cambiar_pagina("Materiales")

# --- Botones flotantes derecha ---
if st.button("ℹ️ Especificaciones", key="btn-top-right"):
    cambiar_pagina("Especificaciones")
if st.button("⚙️ Configuración", key="btn-bottom-right"):
    cambiar_pagina("Configuracion")

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
    st.components.v1.iframe(viewer_url, height=600, width="100%", scrolling=True)
elif pagina == "Configuracion":
    st.header("⚙️ Configuración")
    st.write("Opciones de configuración de la app.")

st.markdown('</div>', unsafe_allow_html=True)
