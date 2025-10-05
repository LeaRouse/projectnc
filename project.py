import streamlit as st
from pathlib import Path
import base64
from mimetypes import guess_type

# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# -----------------------------------------------------------------------------
# UTILS
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

def bg_video_html():
    video = Path("video.mp4")
    if video.exists():
        data = video.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
          <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    return "<!-- no video.mp4 -->"

# -----------------------------------------------------------------------------
# ASSETS
# -----------------------------------------------------------------------------
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# -----------------------------------------------------------------------------
# STATE
# -----------------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# -----------------------------------------------------------------------------
# BACKGROUND + GLOBAL CSS
# -----------------------------------------------------------------------------
st.markdown(bg_video_html(), unsafe_allow_html=True)

st.markdown("""
<style>
/* Fondo persistente */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background: transparent !important;
  color: #d0d0d0 !important;
}
video#bgvid {
  position: fixed; top:50%; left:50%;
  min-width:100%; min-height:100%;
  transform:translate(-50%, -50%);
  object-fit:cover;
  z-index:-3;
  filter: brightness(0.65) contrast(1.05);
}
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* Línea divisoria */
.sidebar-line {
  position: fixed; top:0; left:230px; height:100vh; width:2px;
  background: linear-gradient(to bottom, rgba(255,255,255,0) 0%,
                                      rgba(255,255,255,0.25) 30%,
                                      rgba(255,255,255,0.25) 70%,
                                      rgba(255,255,255,0) 100%);
  z-index:1; backdrop-filter: blur(2px);
}

/* ====== BOTONES (TU CAPA VISUAL) ====== */
.icon-button {
  position: fixed;
  background: rgba(35,35,35,0.75);
  border: 2px solid rgba(255,255,255,0.25);
  transition: transform .22s ease, border-color .22s ease, background .22s ease;
  z-index: 5;  /* la capa click va con z-index: 8 */
  display: flex; justify-content: center; align-items: center;
  overflow: hidden;
}
.icon-button:hover { background: rgba(255,255,255,0.08); transform: scale(1.05); border-color: rgba(255,255,255,0.6); }
.icon-button img { width:100%; height:100%; object-fit:cover; border-radius:inherit; filter: brightness(0.93) contrast(1.05); transition: all .22s; }
.icon-button:hover img { filter: brightness(1.05) contrast(1.1); }

/* Tamaño y posición (izquierda: cuadrados) */
#btn-home, #btn-craft, #btn-mat {
  left: 25px; width:180px; height:180px; border-radius:22px;
}
#btn-home  { top:12%; }
#btn-craft { top:41%; }
#btn-mat   { top:70%; }

/* Derecha: círculos */
#btn-spec, #btn-config {
  border-radius:50%; width:80px; height:80px;
}
#btn-spec  { right:25px; top:80px; }
#btn-config{ right:25px; bottom:30px; }

/* ====== CAPA CLICK (WIDGET NATIVO) ======
   Ponemos un botón nativo invisible exactamente encima del botón visual.
   Así el click es nativo (sin JS/URL) y tu botón visual se ve tal cual. */
.click-slot {
  position: fixed; z-index: 8;  /* por encima de la capa visual */
  width: 180px; height: 180px; border-radius: 22px;
  pointer-events: auto;
}
#slot-home  { left:25px; top:12%;  }
#slot-craft { left:25px; top:41%;  }
#slot-mat   { left:25px; top:70%;  }
#slot-spec  { right:25px; top:80px;  width:80px; height:80px;  border-radius:50%; }
#slot-conf  { right:25px; bottom:30px; width:80px; height:80px; border-radius:50%; }

/* Hacemos invisibles los botones nativos, pero ocupan todo el área */
.click-slot [data-testid="baseButton-secondary"] {
  background: transparent !important;
  border: none !important;
  color: transparent !important;
  box-shadow: none !important;
  width: 100% !important;
  height: 100% !important;
  padding: 0 !important;
}
.click-slot button { width: 100%; height: 100%; cursor: pointer; }

/* ====== CONTENIDO con transición suave ====== */
#main-content {
  opacity: .0;
  transform: translateY(2px);
  animation: fadeIn .20s ease-out forwards;
}
@keyframes fadeIn {
  from { opacity: .0; transform: translateY(2px); }
  to   { opacity: 1;  transform: translateY(0); }
}

/* Texto */
h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CAPA VISUAL DE TUS BOTONES (imágenes)
# -----------------------------------------------------------------------------
def img_or_placeholder(data_uri: str):
    if data_uri:
        return f'<img src="{data_uri}" />'
    return '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:#aaa;font:600 14px/1 sans-serif;">img</div>'

st.markdown(f"""
<div id="btn-home"   class="icon-button">{img_or_placeholder(icon_home)}</div>
<div id="btn-craft"  class="icon-button">{img_or_placeholder(icon_craft)}</div>
<div id="btn-mat"    class="icon-button">{img_or_placeholder(icon_mat)}</div>
<div id="btn-spec"   class="icon-button">{img_or_placeholder(icon_spec)}</div>
<div id="btn-config" class="icon-button">{img_or_placeholder(icon_conf)}</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CAPA CLICKABLE (BOTONES NATIVOS INVISIBLES) — CAMBIA SOLO STATE (SPA-like)
# -----------------------------------------------------------------------------
def nav_button(slot_id: str, label: str, target_page: str):
    st.markdown(f'<div id="{slot_id}" class="click-slot">', unsafe_allow_html=True)
    if st.button(label, key=f"k_{slot_id}"):
        st.session_state.pagina = target_page
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

nav_button("slot-home",  "Home",            "Home")
nav_button("slot-craft", "Craft",           "Craft")
nav_button("slot-mat",   "Materiales",      "Materiales")
nav_button("slot-spec",  "Especificaciones","Especificaciones")
nav_button("slot-conf",  "Configuración",   "Configuracion")

# -----------------------------------------------------------------------------
# CONTENIDO (solo esta zona cambia y se anima; lo demás permanece)
# -----------------------------------------------------------------------------
pagina = st.session_state.pagina

if pagina == "Home":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    if logo_data:
        st.markdown(f"""
        <div style="
            position: fixed; left: 260px; right: 0; top: 0; bottom: 0;
            display:flex; align-items:center; justify-content:center;
            text-align:center; z-index:0;">
            <img src="{logo_data}" alt="AstroCycle logo"
                 style="width:1000px; max-width:85vw; height:auto;
                        filter: drop-shadow(0 0 35px rgba(255,255,255,0.35));" />
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Sube **logotipoastrocycle2.png** a la carpeta del script.")
    st.markdown('</div>', unsafe_allow_html=True)

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
    import streamlit.components.v1 as components
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Configuracion":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
    st.markdown('</div>', unsafe_allow_html=True)
