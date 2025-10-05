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
.stButton>button {width:100%; margin-bottom:12px; padding:12px; border-radius:12px; background: rgba(30,30,30,0.85); color:#f1f1f1; font-weight:bold; border:none; transition:0.2s;}
.stButton>button:hover {background: rgba(70,70,70,0.95);}
</style>
""", unsafe_allow_html=True)

# --- Session state para página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Layout con columnas ---
col_left, col_right = st.columns([1, 4])  # izquierda para botones, derecha para contenido

# --- Botones izquierda ---
with col_left:
    st.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
    st.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
    st.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))

# --- Botones derecha ---
# Podemos mantenerlos flotantes con HTML
st.markdown(f"""
<button style="position:fixed; right:20px; top:80px; z-index:5; width:140px; padding:12px; border-radius:14px; border:none; font-weight:bold; color:#f1f1f1; background-color: rgba(30,30,30,0.85);" onclick="window.location.reload();">⚙️ Especificaciones</button>
<button style="position:fixed; right:20px; bottom:30px; z-index:5; width:140px; padding:12px; border-radius:14px; border:none; font-weight:bold; color:#f1f1f1; background-color: rgba(30,30,30,0.85);" onclick="window.location.reload();">🧩 Configuración</button>
""", unsafe_allow_html=True)

# --- Contenido dinámico en la columna derecha ---
with col_right:
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
