import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AstroCycle 🌌", layout="wide")

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
video#bgvid {position: fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform: translate(-50%, -50%); object-fit: cover; z-index:-3; filter: brightness(0.65) contrast(1.05);}
.bg-overlay {position: fixed; inset: 0; background: rgba(0,0,0,0.45); z-index: -2;}

/* Barra lateral */
section[data-testid="stSidebar"] {
    width: 220px; position: fixed; top: 80px; left:0; height: calc(100%-80px);
    background-color: rgba(28,28,28,0.85); border-radius:0 12px 12px 0; padding:20px;
}

/* Botones barra lateral */
.stButton>button {
    width: 100%; margin-bottom: 15px; padding:12px; border-radius:12px;
    border:none; font-weight:bold; background-color:#2a2a2a; color:#d0d0d0;
    text-align:left; cursor:pointer; transition:0.2s;
}
.stButton>button:hover {background-color:#3a3a3a; color:#fff;}

/* Contenido principal */
.main-content {margin-left:240px; padding:20px;}

/* Botones flotantes derecha */
.floating-btn {
    position: fixed; z-index: 999; width: 50px; height: 50px; border-radius: 25px;
    border: none; font-size: 24px; cursor: pointer; color: #d0d0d0;
    background-color: rgba(42,42,42,0.85); transition: 0.2s;
}
.floating-btn:hover {background-color: #3a3a3a; color:#fff;}
#btn-about {top: 20px; right: 20px;}
#btn-config {bottom: 20px; right: 20px;}
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- Función para cambiar página ---
def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Barra lateral ---
st.sidebar.title("🌠 AstroCycle")
st.sidebar.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
st.sidebar.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
st.sidebar.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))

# --- Botones flotantes derecha usando HTML + Streamlit ---
components.html(f"""
<div style="position: fixed; top:20px; right:20px; z-index:999;">
    <form method="post">
        <input type="submit" name="about_btn" value="ℹ️" class="floating-btn">
    </form>
</div>
<div style="position: fixed; bottom:20px; right:20px; z-index:999;">
    <form method="post">
        <input type="submit" name="config_btn" value="⚙️" class="floating-btn">
    </form>
</div>
""", height=0, width=0)

# --- Detectar clicks de botones flotantes ---
if "about_btn" in st.session_state:
    st.session_state.pagina = "About"
if "config_btn" in st.session_state:
    st.session_state.pagina = "Configuracion"

# --- Detectar botones usando query_params (reemplazo de experimental) ---
if st.query_params.get("about_btn"):
    cambiar_pagina("About")
if st.query_params.get("config_btn"):
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
elif pagina == "About":
    st.header("ℹ️ Acerca de")
    st.write("Información sobre la aplicación AstroCycle.")
elif pagina == "Configuracion":
    st.header("⚙️ Configuración")
    st.write("Opciones de configuración de la aplicación.")

st.markdown('</div>', unsafe_allow_html=True)
