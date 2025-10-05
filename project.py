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
    return "<!-- No se encontró video.mp4 -->"

st.markdown(get_video_html(), unsafe_allow_html=True)

# --- FUNCIONES PARA IMAGEN BASE64 ---
@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# --- CARGAR ICONOS ---
iconos = {
    "Home": img_data_uri("home.png"),
    "Craft": img_data_uri("craft.png"),
    "Materiales": img_data_uri("materiales.png"),
    "Especificaciones": img_data_uri("especificaciones.png"),
    "Configuracion": img_data_uri("config.png"),
    "Logo": img_data_uri("logotipoastrocycle2.png")
}

# --- ESTADO DE NAVEGACIÓN ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# --- CSS DE BOTONES Y VIDEO ---
st.markdown(f"""
<style>
/* Fondo y video */
.stApp {{
    background: transparent !important;
    color: #d0d0d0;
}}
video#bgvid {{
    position: fixed;
    top: 50%; left: 50%;
    min-width: 100%; min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: -3;
    filter: brightness(0.65) contrast(1.05);
}}
.bg-overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.45);
    z-index: -2;
}}

/* Línea divisoria */
.sidebar-line {{
    position: fixed;
    top: 0;
    left: 230px;
    height: 100vh;
    width: 2px;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%,
                                          rgba(255,255,255,0.25) 30%,
                                          rgba(255,255,255,0.25) 70%,
                                          rgba(255,255,255,0) 100%);
    z-index: 1;
    backdrop-filter: blur(2px);
}}

/* Estilo común de botones */
.icon-button {{
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
}}

.icon-button:hover {{
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}}

.icon-button img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}}

.icon-button:hover img {{
    filter: brightness(1.05) contrast(1.1);
}}

/* Botones a la izquierda */
#btn-home, #btn-craft, #btn-mat {{
    left: 25px;
    width: 180px;
    height: 180px;
    border-radius: 22px;
}}

#btn-home {{ top: 12%; }}
#btn-craft {{ top: 41%; }}
#btn-mat {{ top: 70%; }}

/* Botones a la derecha */
#btn-spec, #btn-config {{
    border-radius: 50%;
    width: 80px;
    height: 80px;
}}

#btn-spec {{ right: 25px; top: 80px; }}
#btn-config {{ right: 25px; bottom: 30px; }}

/* Contenedor de contenido */
#main-content {{
    margin-left: 260px;
    padding: 20px;
}}
</style>
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# --- BOTONES HTML FIJOS ---
st.markdown(f"""
<div class="icon-button" id="btn-home" onclick="fetch('/?nav=Home').then(() => window.location.reload())">
    <img src="{iconos['Home']}">
</div>
<div class="icon-button" id="btn-craft" onclick="fetch('/?nav=Craft').then(() => window.location.reload())">
    <img src="{iconos['Craft']}">
</div>
<div class="icon-button" id="btn-mat" onclick="fetch('/?nav=Materiales').then(() => window.location.reload())">
    <img src="{iconos['Materiales']}">
</div>
<div class="icon-button" id="btn-spec" onclick="fetch('/?nav=Especificaciones').then(() => window.location.reload())">
    <img src="{iconos['Especificaciones']}">
</div>
<div class="icon-button" id="btn-config" onclick="fetch('/?nav=Configuracion').then(() => window.location.reload())">
    <img src="{iconos['Configuracion']}">
</div>
""", unsafe_allow_html=True)

# --- DETECTAR CLIC CON PARÁMETRO EN URL ---
query_params = st.experimental_get_query_params()
if "nav" in query_params:
    st.session_state.pagina = query_params["nav"][0]

# --- CONTENIDO DE CADA SUBPÁGINA ---
st.markdown('<div id="main-content">', unsafe_allow_html=True)

pagina = st.session_state.pagina

if pagina == "Home":
    if iconos["Logo"]:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{iconos['Logo']}" style="width:1000px; max-width:85vw; height:auto;
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
