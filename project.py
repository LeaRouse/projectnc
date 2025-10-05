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

# Mantener la URL actualizada al estado
try:
    st.query_params["page"] = st.session_state.pagina
except AttributeError:
    st.experimental_set_query_params(page=st.session_state.pagina)

# --- BOTONES FLOTANTES CON NAVEGACIÓN INTERNA (mismo tab, sin JS) ---
current = st.session_state.pagina  # opcional, para marcar activo

st.markdown(f"""
<style>
/* resalte del botón activo (opcional) */
.icon-button.active {{
  outline: 3px solid rgba(255,255,255,0.7);
  box-shadow: 0 0 20px rgba(255,255,255,0.25);
}}

/* estilos del botón html para que no se vea como botón nativo */
.icon-as-form {{
  position: fixed;
  z-index: 6;
  margin: 0;
  padding: 0;
  background: none;
  border: none;
  width: 180px;
  height: 180px;
  border-radius: 22px;
  cursor: pointer;
  overflow: hidden;
}}
/* ubicaciones (coinciden con tus #btn-*) */
#home-form {{ left:25px; top:12%;  }}
#craft-form {{ left:25px; top:41%;  }}
#mat-form   {{ left:25px; top:70%;  }}
#spec-form  {{ right:25px; top:80px; width:80px; height:80px; border-radius:50%; }}
#conf-form  {{ right:25px; bottom:30px; width:80px; height:80px; border-radius:50%; }}

/* capa visual del botón (tu estilo original) */
.icon-visual {{
  position: fixed;
  background: rgba(35,35,35,0.75);
  border: 2px solid rgba(255,255,255,0.25);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  z-index: 5;
}}
#btn-home, #btn-craft, #btn-mat {{
  left: 25px; width: 180px; height: 180px; border-radius: 22px;
}}
#btn-home {{ top:12%;  }}
#btn-craft {{ top:41%; }}
#btn-mat {{ top:70%;  }}
#btn-spec, #btn-config {{
  border-radius:50%; width:80px; height:80px;
}}
#btn-spec {{ right:25px; top:80px;    }}
#btn-config {{ right:25px; bottom:30px; }}

.icon-visual:hover {{ background: rgba(255,255,255,0.08); transform: scale(1.05); border-color: rgba(255,255,255,0.6); }}
.icon-visual img {{ width:100%; height:100%; object-fit:cover; border-radius:inherit; filter: brightness(0.93) contrast(1.05); transition: all .25s; }}
.icon-visual:hover img {{ filter: brightness(1.05) contrast(1.1); }}

/* quitar estilos por defecto al <button> dentro del form */
.icon-as-form:focus {{ outline: none; }}
</style>

<!-- Capa visual (se ve) -->
<div id="btn-home"   class="icon-visual {'active' if current=='Home' else ''}"><img src="{icon_home}"  alt="Home"></div>
<div id="btn-craft"  class="icon-visual {'active' if current=='Craft' else ''}"><img src="{icon_craft}" alt="Craft"></div>
<div id="btn-mat"    class="icon-visual {'active' if current=='Materiales' else ''}"><img src="{icon_mat}"   alt="Materiales"></div>
<div id="btn-spec"   class="icon-visual {'active' if current=='Especificaciones' else ''}"><img src="{icon_spec}" alt="Especificaciones"></div>
<div id="btn-config" class="icon-visual {'active' if current=='Configuracion' else ''}"><img src="{icon_conf}" alt="Configuración"></div>

<!-- Capas clickables (formularios GET que cambian ?page=... en el mismo tab) -->
<form id="home-form"  class="icon-as-form"  method="get">
  <input type="hidden" name="page" value="Home">
  <button type="submit" aria-label="Home"></button>
</form>

<form id="craft-form" class="icon-as-form"  method="get">
  <input type="hidden" name="page" value="Craft">
  <button type="submit" aria-label="Craft"></button>
</form>

<form id="mat-form"   class="icon-as-form"  method="get">
  <input type="hidden" name="page" value="Materiales">
  <button type="submit" aria-label="Materiales"></button>
</form>

<form id="spec-form"  class="icon-as-form"  method="get">
  <input type="hidden" name="page" value="Especificaciones">
  <button type="submit" aria-label="Especificaciones"></button>
</form>

<form id="conf-form"  class="icon-as-form"  method="get">
  <input type="hidden" name="page" value="Configuracion">
  <button type="submit" aria-label="Configuración"></button>
</form>
""", unsafe_allow_html=True)


# --- CONTENIDO ---
pagina = st.session_state.pagina
IMG_FILE = Path("logotipoastrocycle2.png")

if pagina == "Home":
   
    # 1) Armamos el tag del logo fuera del f-string grande (sin anidar comillas)
    if logo_data:
        logo_tag = (
            f'<img src="{logo_data}" alt="AstroCycle logo" '
            f'style="width:1000px; max-width:85vw; height:auto; '
            + f'filter:drop-shadow(0 0 35px rgba(255,255,255,0.35)); transform:scale(1.75); '
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







