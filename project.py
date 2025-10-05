import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
from mimetypes import guess_type

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

# --- CSS + línea divisoria + Transiciones (fade-in / fade-out con solo CSS) ---
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
    left: 230px;
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

/* ===== BOTONES FLOTANTES (CAPA VISUAL) ===== */
.icon-button {
    position: fixed;
    background: rgba(35,35,35,0.75);
    border: 2px solid rgba(255,255,255,0.25);
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5; /* la capa click va con z-index:7 */
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}
.icon-button:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}
.icon-button img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.icon-button:hover img { filter: brightness(1.05) contrast(1.1); }

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

/* ===== CAPAS CLICK (ENLACES INVISIBLES SOBRE LA CAPA VISUAL) ===== */
.link-overlay {
    position: fixed;
    z-index: 7;        /* por encima del botón visual */
    display: block;
    background: transparent;
    border-radius: 22px; /* se ajusta en los redondos */
    /* sin target -> misma pestaña */
    text-decoration: none;
}
/* posiciones idénticas a los botones visuales */
#link-home  { left:25px; top:12%;  width:180px; height:180px; border-radius:22px; }
#link-craft { left:25px; top:41%;  width:180px; height:180px; border-radius:22px; }
#link-mat   { left:25px; top:70%;  width:180px; height:180px; border-radius:22px; }
#link-spec  { right:25px; top:80px; width:80px;  height:80px;  border-radius:50%; }
#link-conf  { right:25px; bottom:30px; width:80px; height:80px; border-radius:50%; }

/* ===== TRANSICIONES SUAVES DE PÁGINA ===== */
#main-content {
  opacity: 0;
  transform: scale(0.995);
  animation: pageFadeIn .35s ease-out forwards;
}
@keyframes pageFadeIn {
  from { opacity: 0; transform: scale(0.985); }
  to   { opacity: 1; transform: scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  #main-content {
    animation: none !important;
    transform: none !important;
  }
}

/* --- TEXTOS --- */
h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>

<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# --- Session state para página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Sincronizar con query params (?page=Home, etc.) ---
try:
    # Streamlit >= 1.30
    page_param = st.query_params.get("page", None)
except AttributeError:
    # Streamlit < 1.30
    qp = st.experimental_get_query_params()
    page_param = qp.get("page", [None])[0] if qp.get("page") else None

if page_param:
    st.session_state.pagina = page_param

# Mantener la URL actualizada al estado (útil para refrescos o compartir enlace)
try:
    st.query_params["page"] = st.session_state.pagina
except AttributeError:
    st.experimental_set_query_params(page=st.session_state.pagina)

# --- CAPA VISUAL DE BOTONES (se ve) ---
current = st.session_state.pagina

st.markdown(f"""
<div>
  <div class="icon-button" id="btn-home">
    <img src="{icon_home}"  alt="Home">
  </div>
  <div class="icon-button" id="btn-craft">
    <img src="{icon_craft}" alt="Craft">
  </div>
  <div class="icon-button" id="btn-mat">
    <img src="{icon_mat}"   alt="Materiales">
  </div>
  <div class="icon-button" id="btn-spec">
    <img src="{icon_spec}" alt="Especificaciones">
  </div>
  <div class="icon-button" id="btn-config">
    <img src="{icon_conf}" alt="Configuración">
  </div>
</div>
""", unsafe_allow_html=True)

# --- CAPA CLICKABLE: ENLACES INVISIBLES (MISMA PESTAÑA) ---
st.markdown("""
<a id="link-home"  class="link-overlay" href="?page=Home"            target="_self" aria-label="Home"></a>
<a id="link-craft" class="link-overlay" href="?page=Craft"           target="_self" aria-label="Craft"></a>
<a id="link-mat"   class="link-overlay" href="?page=Materiales"      target="_self" aria-label="Materiales"></a>
<a id="link-spec"  class="link-overlay" href="?page=Especificaciones" target="_self" aria-label="Especificaciones"></a>
<a id="link-conf"  class="link-overlay" href="?page=Configuracion"   target="_self" aria-label="Configuración"></a>
""", unsafe_allow_html=True)

# --- CONTENIDO ---
pagina = st.session_state.pagina

if pagina == "Home":
    # Logo centrado (solo logo)
    if logo_data:
        logo_tag = (
            f'<img src="{logo_data}" alt="AstroCycle logo" '
            f'style="width:1000px; max-width:85vw; height:auto; '
            f'filter:drop-shadow(0 0 35px rgba(255,255,255,0.35)); '
            f'transition:transform 0.6s ease-in-out;" '
            f'onmouseover="this.style.transform=\'scale(1.04)\'" '
            f'onmouseout="this.style.transform=\'scale(1.0)\'" />'
        )
    else:
        logo_tag = '<div style="color:#ccc;">No se encontró logotipoastrocycle2.png</div>'

    html_home = f"""
    <div id="main-content">
      <div style="
          position: fixed;
          left: 260px; right: 0; top: 0; bottom: 0;
          display: flex; justify-content: center; align-items: center;
          text-align: center; z-index: 0;
      ">
          {logo_tag}
      </div>
    </div>
    """
    st.markdown(html_home, unsafe_allow_html=True)

elif pagina == "Craft":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Materiales":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Especificaciones":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Configuracion":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
    st.markdown('</div>', unsafe_allow_html=True)

