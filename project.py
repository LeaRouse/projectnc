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

from mimetypes import guess_type

# --- Función para convertir PNG a Base64 ---
@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        st.warning(f"No se encontró {path_str}")
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# --- Cargar las imágenes ---
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data = img_data_uri("logotipoastrocycle2.png")
st.write("Logo cargado:", bool(logo_data))

# --- CSS GENERAL ---
st.markdown("""
<style>
/* ===== FONDO ===== */
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

/* ===== LÍNEA DIVISORIA IZQUIERDA ===== */
.sidebar-line {
    position: fixed;
    top: 0;
    left: 230px;               /* distancia desde el borde izquierdo */
    height: 100vh;
    width: 2px;
    background: linear-gradient(
        to bottom,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.25) 30%,
        rgba(255,255,255,0.25) 70%,
        rgba(255,255,255,0) 100%
    );
    z-index: 1;
    backdrop-filter: blur(2px);
}

/* ===== BOTONES ===== */
.icon-button {
    position: fixed;
    background: rgba(35,35,35,0.75);
    border: 2px solid rgba(255,255,255,0.25);
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

/* --- EFECTO HOVER --- */
.icon-button:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}

/* --- IMÁGENES --- */
.icon-button img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.icon-button:hover img {
    filter: brightness(1.05) contrast(1.1);
}

/* --- BOTONES IZQUIERDA (CUADRADOS GRANDES Y ESPACIADOS) --- */
#btn-home, #btn-craft, #btn-mat {
    left: 25px;
    width: 180px;
    height: 180px;
    border-radius: 22px;
}
#btn-home { top: 12%; }
#btn-craft { top: 41%; }
#btn-mat { top: 70%; }

/* --- BOTONES DERECHA (CÍRCULOS) --- */
#btn-spec, #btn-config {
    border-radius: 50%;
    width: 80px;
    height: 80px;
}
#btn-spec { right: 25px; top: 80px; }
#btn-config { right: 25px; bottom: 30px; }

/* --- TEXTOS --- */
h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>

<!-- Inserta la línea visual -->
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)


# --- Session state para página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- BOTONES FLOTANTES CON IMÁGENES ---
# Asegúrate de tener tus íconos en la misma carpeta: home.png, craft.png, materiales.png, especificaciones.png, config.png
st.markdown(f"""
<div>
  <div class="icon-button" id="btn-home"><img src="{icon_home}" alt="Home"></div>
  <div class="icon-button" id="btn-craft"><img src="{icon_craft}" alt="Craft"></div>
  <div class="icon-button" id="btn-mat"><img src="{icon_mat}" alt="Materiales"></div>
  <div class="icon-button" id="btn-spec"><img src="{icon_spec}" alt="Especificaciones"></div>
  <div class="icon-button" id="btn-config"><img src="{icon_conf}" alt="Configuración"></div>
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
IMG_FILE = Path("logotipoastrocycle2.png")

if pagina == "Home":
    # Diagnóstico rápido (lo puedes dejar o quitar)
    st.write("Archivo existe:", Path("logotipoastrocycle2.png").exists())
    st.write("Data URI generada:", bool(logo_data))

    # 1) Armamos el tag del logo fuera del f-string grande (sin anidar comillas)
    if logo_data:
        logo_tag = (
            f'<img src="{logo_data}" alt="AstroCycle logo" '
            f'style="width:2000px; max-width:170vw; height:auto; '
            f'filter:drop-shadow(0 0 35px rgba(255,255,255,0.35)); '
            f'transition:transform 0.6s ease-in-out;" '
            f'onmouseover="this.style.transform=\'scale(1.04)\'" '
            f'onmouseout="this.style.transform=\'scale(1.0)\'" />'
        )
    else:
        logo_tag = '<div style="color:#ccc;">No se encontró logotipoastrocycle2.png</div>'


    # 2) Contenedor centrado solo en el área principal (a la derecha del menú)
    html_home = f"""
    <div style="
        position: fixed;
        left: 260px;   /* ancho del menú + separación; ajusta si cambias tus botones */
        right: 0;
        top: 0;
        bottom: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        z-index: 0;
    ">
        {logo_tag}
    </div>
    """

    st.markdown(html_home, unsafe_allow_html=True)

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































