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

st.markdown(get_video_html(), unsafe_allow_html=True)

# --- CSS GENERAL ---
st.markdown("""
<style>
/* Fondo */
.stApp { background: transparent !important; color: #d0d0d0 !important; }
video#bgvid {
    position: fixed; top:50%; left:50%;
    min-width:100%; min-height:100%;
    transform:translate(-50%, -50%);
    object-fit:cover;
    z-index:-3;
    filter: brightness(0.65) contrast(1.05);
}
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* ===== BOTONES DE IMAGEN ===== */
.icon-button {
    position: fixed;
    background: rgba(30,30,30,0.6);
    border-radius: 50%;
    border: 2px solid rgba(255,255,255,0.3);
    padding: 10px;
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
    width: 70px;
    height: 70px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.icon-button:hover {
    background: rgba(255,255,255,0.1);
    transform: scale(1.1);
    border-color: rgba(255,255,255,0.7);
}
.icon-button img {
    width: 42px;
    height: 42px;
    filter: brightness(0.9);
}

/* Posiciones */
#btn-home { left: 20px; top: 35%; }
#btn-craft { left: 20px; top: 45%; }
#btn-mat { left: 20px; top: 55%; }
#btn-spec { right: 20px; top: 80px; }
#btn-config { right: 20px; bottom: 30px; }

/* Textos */
h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>
""", unsafe_allow_html=True)

# --- Session state para página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- BOTONES FLOTANTES CON IMÁGENES ---
# Asegúrate de tener tus íconos en la misma carpeta: home.png, craft.png, materiales.png, especificaciones.png, config.png
st.markdown("""
<div>
  <div class="icon-button" id="btn-home"><img src="home.png"></div>
  <div class="icon-button" id="btn-craft"><img src="craft.png"></div>
  <div class="icon-button" id="btn-mat"><img src="materiales.png"></div>
  <div class="icon-button" id="btn-spec"><img src="especificaciones.png"></div>
  <div class="icon-button" id="btn-config"><img src="config.png"></div>
</div>
""", unsafe_allow_html=True)

# --- JS para cambiar de página ---
components.html("""
<script>
const mapping = {
    "btn-home": "Home",
    "btn-craft": "Craft",
    "btn-mat": "Materiales",
    "btn-spec": "Especificaciones",
    "btn-config": "Configuracion"
};
for(const id in mapping){
    const el = document.getElementById(id);
    if(el){
        el.onclick = () => { window.parent.postMessage({type:mapping[id]}, "*"); };
    }
}
window.addEventListener('message', event => {
    const type = event.data.type;
    if(type){
        document.dispatchEvent(new CustomEvent('updatePagina',{detail:type}));
    }
});
</script>
""", height=0, width=0)

components.html("""
<script>
document.addEventListener('updatePagina', e => {
    fetch('/_stcore', {method:'POST', body:e.detail});
});
</script>
""", height=0, width=0)

# --- CONTENIDO ---
pagina = st.session_state.pagina
IMG_FILE = Path("logotipoastrocycle.png")

if pagina == "Home":
    st.markdown("""
    <div style="display:flex; flex-direction:column; justify-content:flex-start; align-items:center; height:90vh; padding-top:20px;">
        <h1 style="color:#ffffff; font-size:120px; margin-bottom:0px;">AstroCycle</h1>
    """, unsafe_allow_html=True)
    if IMG_FILE.exists():
        st.image(str(IMG_FILE), width=700)
    else:
        st.warning("No se encontró logotipoastrocycle.png")
    st.markdown("</div>", unsafe_allow_html=True)

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
