import streamlit as st
from pathlib import Path
import base64
from mimetypes import guess_type
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

# --- Utilidad: PNG/JPG -> data URI ---
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

# --- Cargar imágenes ---
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# --- STATE ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# --- CSS GENERAL ---
st.markdown("""
<style>
/* Fondo y video */
.stApp { background: transparent !important; color: #d0d0d0 !important; }
video#bgvid { position: fixed; top:50%; left:50%; min-width:100%; min-height:100%;
    transform:translate(-50%, -50%); object-fit:cover; z-index:-3;
    filter: brightness(0.65) contrast(1.05); }
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* Línea divisoria */
.sidebar-line { position: fixed; top:0; left:230px; height:100vh; width:2px;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%,
                                      rgba(255,255,255,0.25) 30%,
                                      rgba(255,255,255,0.25) 70%,
                                      rgba(255,255,255,0) 100%);
    z-index:1; backdrop-filter: blur(2px); }

/* Botones flotantes */
.icon-button { position: fixed; background: rgba(35,35,35,0.75); border:2px solid rgba(255,255,255,0.25);
    cursor: pointer; transition: all 0.25s ease; z-index:5;
    display:flex; justify-content:center; align-items:center; overflow:hidden; }
.icon-button:hover { background: rgba(255,255,255,0.08); transform: scale(1.05); border-color: rgba(255,255,255,0.6); }
.icon-button img { width:100%; height:100%; object-fit:cover; border-radius:inherit;
    filter: brightness(0.93) contrast(1.05); transition: all 0.25s ease; }
.icon-button:hover img { filter: brightness(1.05) contrast(1.1); }

/* Izquierda */
#btn-home, #btn-craft, #btn-mat { left:25px; width:180px; height:180px; border-radius:22px; }
#btn-home { top:12%; }
#btn-craft { top:41%; }
#btn-mat { top:70%; }

/* Derecha */
#btn-spec, #btn-config { border-radius:50%; width:80px; height:80px; }
#btn-spec { right:25px; top:80px; }
#btn-config{ right:25px; bottom:30px; }

/* Contenido */
#main-content { margin-left:260px; padding: 20px; }
</style>
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# --- BOTONES VISUALES ---
st.markdown(f"""
<div class="icon-button" id="btn-home"><img src="{icon_home}"></div>
<div class="icon-button" id="btn-craft"><img src="{icon_craft}"></div>
<div class="icon-button" id="btn-mat"><img src="{icon_mat}"></div>
<div class="icon-button" id="btn-spec"><img src="{icon_spec}"></div>
<div class="icon-button" id="btn-config"><img src="{icon_conf}"></div>
""", unsafe_allow_html=True)

# --- BOTONES INVISIBLES DE STREAMLIT PARA CAMBIAR CONTENIDO SIN RECARGAR ---
# Detectamos clicks con botones invisibles colocados estratégicamente

# Colocamos botones invisibles en la página
placeholder_buttons = st.empty()
with placeholder_buttons.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("", key="btn_home", help="Home"):
            st.session_state.pagina = "Home"
    with col2:
        if st.button("", key="btn_craft", help="Craft"):
            st.session_state.pagina = "Craft"
    with col3:
        if st.button("", key="btn_mat", help="Materiales"):
            st.session_state.pagina = "Materiales"
    with col4:
        if st.button("", key="btn_spec", help="Especificaciones"):
            st.session_state.pagina = "Especificaciones"
    with col5:
        if st.button("", key="btn_config", help="Configuración"):
            st.session_state.pagina = "Configuracion"

# --- CONTENIDO DINÁMICO ---
pagina = st.session_state.pagina

st.markdown('<div id="main-content">', unsafe_allow_html=True)

if pagina == "Home":
    if logo_data:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{logo_data}" style="width:1000px; max-width:85vw; height:auto;
            filter: drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
        </div>
        """, unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
