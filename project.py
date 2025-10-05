import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
from mimetypes import guess_type

# ---------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------------------
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# ---------------------------------------------------------------------
# FUNCIONES UTILS
# ---------------------------------------------------------------------
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

def get_video_html(video_path="video.mp4"):
    p = Path(video_path)
    if p.exists():
        data = p.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    return "<!-- No video -->"

# ---------------------------------------------------------------------
# CARGAR IMÁGENES
# ---------------------------------------------------------------------
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# ---------------------------------------------------------------------
# STATE
# ---------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina
    st.experimental_rerun()

# ---------------------------------------------------------------------
# VIDEO DE FONDO + CSS
# ---------------------------------------------------------------------
st.markdown(get_video_html(), unsafe_allow_html=True)

st.markdown("""
<style>
/* Fondo y overlay */
.stApp { background: transparent !important; color:#d0d0d0 !important; }
video#bgvid { position:fixed; top:50%; left:50%; min-width:100%; min-height:100%;
    transform:translate(-50%, -50%); object-fit:cover; z-index:-3;
    filter: brightness(0.65) contrast(1.05);}
.bg-overlay {position:fixed; inset:0; background:rgba(0,0,0,0.45); z-index:-2;}

/* Línea divisoria */
.sidebar-line { position:fixed; top:0; left:230px; width:2px; height:100vh;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,0.25) 30%, rgba(255,255,255,0.25) 70%, rgba(255,255,255,0) 100%);
    z-index:1; backdrop-filter: blur(2px); }

/* Botones flotantes izquierda */
.icon-button { position:fixed; background: rgba(35,35,35,0.75);
    border:2px solid rgba(255,255,255,0.25); cursor:pointer;
    transition: all 0.25s ease; z-index:5; display:flex; justify-content:center; align-items:center; overflow:hidden; }
.icon-button:hover { background: rgba(255,255,255,0.08); transform: scale(1.05); border-color: rgba(255,255,255,0.6);}
.icon-button img { width:100%; height:100%; object-fit:cover; border-radius:inherit; filter: brightness(0.93) contrast(1.05); transition: all 0.25s ease;}
.icon-button:hover img { filter: brightness(1.05) contrast(1.1); }

/* Posición botones izquierda */
#btn-home, #btn-craft, #btn-mat { left:25px; width:180px; height:180px; border-radius:22px;}
#btn-home {top:12%;} #btn-craft{top:41%;} #btn-mat{top:70%;}

/* Posición botones derecha */
#btn-spec,#btn-config {border-radius:50%; width:80px; height:80px;}
#btn-spec{right:25px; top:80px;} #btn-config{right:25px; bottom:30px;}

/* Contenido animado */
#main-content { opacity:0; transform: scale(0.995); animation: pageFadeIn .35s ease-out forwards;}
@keyframes pageFadeIn { from{opacity:0; transform:scale(0.985);} to{opacity:1; transform:scale(1);} }
h1,h2,h3,p,span { color:#d0d0d0 !important;}
</style>
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# BOTONES VISUALES (solo los negros/transparente)
# ---------------------------------------------------------------------
def img_or_placeholder(data_uri):
    if data_uri: return f'<img src="{data_uri}" />'
    return '<div style="color:#aaa">img</div>'

st.markdown(f"""
<div id="btn-home" class="icon-button">{img_or_placeholder(icon_home)}</div>
<div id="btn-craft" class="icon-button">{img_or_placeholder(icon_craft)}</div>
<div id="btn-mat" class="icon-button">{img_or_placeholder(icon_mat)}</div>
<div id="btn-spec" class="icon-button">{img_or_placeholder(icon_spec)}</div>
<div id="btn-config" class="icon-button">{img_or_placeholder(icon_conf)}</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# JS para que los botones negros/transparente funcionen y cambien la página
# ---------------------------------------------------------------------
components.html(f"""
<script>
(function(){
  function smoothGoto(page){{
    const root = window.parent.document.documentElement;
    if(root) root.classList.add('leaving');
    setTimeout(function(){{
      window.parent.location.search = '?page=' + encodeURIComponent(page);
    }}, 180);
  }}

  const map = {{
    'btn-home': 'Home',
    'btn-craft': 'Craft',
    'btn-mat': 'Materiales',
    'btn-spec': 'Especificaciones',
    'btn-config': 'Configuracion'
  }};

  Object.keys(map).forEach(function(id){{
    const el = window.parent.document.getElementById(id);
    if(el && !el._astroBound){{
      el._astroBound = true;
      el.addEventListener('click', function(ev){{
        ev.preventDefault(); ev.stopPropagation();
        smoothGoto(map[id]);
      }});
    }}
  }});
  setInterval(function(){{
    Object.keys(map).forEach(function(id){{
      const el = window.parent.document.getElementById(id);
      if(el && !el._astroBound){{
        el._astroBound = true;
        el.addEventListener('click', function(ev){{
          ev.preventDefault(); ev.stopPropagation();
          smoothGoto(map[id]);
        }});
      }}
    }});
  }}, 500);
})();
</script>
""", height=0, width=0)

# ---------------------------------------------------------------------
# CONTENIDO (se muestra al lado derecho de los botones)
# ---------------------------------------------------------------------
pagina = st.session_state.pagina
col1, col2 = st.columns([1,4])

with col1:
    pass  # los botones flotantes ya están

with col2:
    if pagina=="Home":
        st.markdown('<div id="main-content">', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center;'>AstroCycle</h1>", unsafe_allow_html=True)
        if logo_data:
            st.image(logo_data, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    elif pagina=="Craft":
        st.markdown('<div id="main-content">', unsafe_allow_html=True)
        st.header("🛠️ Craft")
        st.write("Sección de construcción y desarrollo del prototipo.")
        st.markdown('</div>', unsafe_allow_html=True)
    elif pagina=="Materiales":
        st.markdown('<div id="main-content">', unsafe_allow_html=True)
        st.header("📦 Materiales")
        st.write("Aquí se muestran los materiales utilizados y sus detalles.")
        st.markdown('</div>', unsafe_allow_html=True)
    elif pagina=="Especificaciones":
        st.markdown('<div id="main-content">', unsafe_allow_html=True)
        st.header("⚙️ Especificaciones")
        st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
        components.iframe("https://learouse.github.io/prototipo/", height=600, width="100%", scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)
    elif pagina=="Configuracion":
        st.markdown('<div id="main-content">', unsafe_allow_html=True)
        st.header("🧩 Configuración")
        st.write("Opciones de configuración de la app.")
        st.markdown('</div>', unsafe_allow_html=True)
