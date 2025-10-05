import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- FUNCIÓN PARA IMÁGENES ---
@st.cache_data
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

# --- CARGA DE IMÁGENES ---
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# --- ESTADO DE PÁGINA ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(p):
    st.session_state.pagina = p

# --- VIDEO DE FONDO ---
VIDEO_FILE = Path("video.mp4")
def get_video_html():
    if VIDEO_FILE.exists():
        b64 = base64.b64encode(VIDEO_FILE.read_bytes()).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    return "<!-- No se encontró video.mp4 -->"

st.markdown(get_video_html(), unsafe_allow_html=True)

# --- CSS ---
st.markdown("""
<style>
.stApp { background: transparent !important; color:#d0d0d0 !important; }
video#bgvid { position:fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform:translate(-50%,-50%); object-fit:cover; z-index:-3; filter:brightness(0.65) contrast(1.05); }
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }
.icon-button { position:fixed; background: rgba(35,35,35,0.75); border-radius:22px; width:180px; height:180px; display:flex; justify-content:center; align-items:center; cursor:pointer; z-index:5; transition: all .25s ease; }
.icon-button:hover { background: rgba(255,255,255,0.08); transform: scale(1.05); }
#btn-home { top:12%; left:25px; }
#btn-craft { top:41%; left:25px; }
#btn-mat { top:70%; left:25px; }
#main-content { position: fixed; left:250px; top:0; bottom:0; right:0; overflow-y:auto; padding:30px; }
</style>
""", unsafe_allow_html=True)

# --- BOTONES VISUALES ---
def img_or_placeholder(data_uri: str):
    if data_uri:
        return f'<img src="{data_uri}" style="width:100%; height:100%; object-fit:cover; border-radius:inherit;">'
    return '<div style="width:100%;height:100%;background:#333;"></div>'

st.markdown(f"""
<div id="btn-home" class="icon-button">{img_or_placeholder(icon_home)}</div>
<div id="btn-craft" class="icon-button">{img_or_placeholder(icon_craft)}</div>
<div id="btn-mat" class="icon-button">{img_or_placeholder(icon_mat)}</div>
""", unsafe_allow_html=True)

# --- BOTONES NATIVOS INVISIBLES PARA FUNCIONAR ---
def click_slot(id, label, target):
    st.markdown(f'<div style="position:fixed; z-index:10; left:25px; top:0;">', unsafe_allow_html=True)
    if st.button(label, key=id):
        cambiar_pagina(target)
    st.markdown('</div>', unsafe_allow_html=True)

click_slot("slot_home",  " ", "Home")
click_slot("slot_craft"," ", "Craft")
click_slot("slot_mat",  " ", "Materiales")

# --- CONTENIDO DINÁMICO ---
pagina = st.session_state.pagina

if pagina=="Home":
    html_home = f"""
    <div style="display:flex; flex-direction:column; align-items:center; padding-top:50px;">
        <h1>AstroCycle</h1>
        <img src="{logo_data}" style="width:600px; max-width:85vw; height:auto; filter:drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
    </div>
    """
    st.markdown(html_home, unsafe_allow_html=True)

elif pagina=="Craft":
    st.markdown('<div style="padding-top:50px;">', unsafe_allow_html=True)
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina=="Materiales":
    st.markdown('<div style="padding-top:50px;">', unsafe_allow_html=True)
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")
    st.markdown('</div>', unsafe_allow_html=True)
