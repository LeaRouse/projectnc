import streamlit as st
from pathlib import Path
import base64
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

# --- CSS GENERAL ---
st.markdown("""
<style>
/* Fondo y video */
.stApp { background: transparent !important; color: #d0d0d0 !important; }
video#bgvid { position: fixed; top:50%; left:50%; min-width:100%; min-height:100%;
    transform:translate(-50%, -50%); object-fit:cover; z-index:-3;
    filter: brightness(0.65) contrast(1.05); }
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* Sidebar fija izquierda */
.sidebar-left {
    position: fixed;
    top: 12%;
    left: 25px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    z-index: 10;
}

/* Sidebar fija derecha */
.sidebar-right {
    position: fixed;
    right: 25px;
    z-index: 10;
}

/* Botones (imagen + texto) */
.sidebar-btn {
    width: 180px;
    height: 180px;
    border-radius: 22px;
    background: rgba(35,35,35,0.75);
    border: 2px solid rgba(255,255,255,0.25);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.25s ease;
    color: #d0d0d0;
    text-decoration: none;
    user-select: none;
}
.sidebar-btn:hover {
    background: rgba(255,255,255,0.08);
    border-color: rgba(255,255,255,0.6);
    color: white;
    transform: scale(1.05);
}
.sidebar-btn img {
    width: 90px;
    height: 90px;
    object-fit: cover;
    border-radius: 12px;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.sidebar-btn:hover img {
    filter: brightness(1.05) contrast(1.1);
}
.sidebar-btn span {
    margin-top: 12px;
    font-weight: 600;
    font-size: 1.2rem;
}

/* Botones derechos (más pequeños y circulares) */
.sidebar-right .sidebar-btn {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    padding: 0;
}
.sidebar-right .sidebar-btn span {
    display: none;
}

/* Contenido principal con margen para que no quede bajo los botones */
#main-content {
    margin-left: 260px;
    margin-right: 120px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Izquierda (3 botones) ---
st.markdown(f"""
<div class="sidebar-left">
    <a href="#Home" class="sidebar-btn" title="Home">
        <img src="{icon_home}" alt="Home" />
        <span>Home</span>
    </a>
    <a href="#Craft" class="sidebar-btn" title="Craft">
        <img src="{icon_craft}" alt="Craft" />
        <span>Craft</span>
    </a>
    <a href="#Materiales" class="sidebar-btn" title="Materiales">
        <img src="{icon_mat}" alt="Materiales" />
        <span>Materiales</span>
    </a>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Derecha (2 botones) ---
st.markdown(f"""
<div class="sidebar-right" style="top: 80px; display: flex; flex-direction: column; gap: 20px;">
    <a href="#Especificaciones" class="sidebar-btn" title="Especificaciones">
        <img src="{icon_spec}" alt="Especificaciones" />
    </a>
    <a href="#Configuracion" class="sidebar-btn" title="Configuración">
        <img src="{icon_conf}" alt="Configuración" />
    </a>
</div>
""", unsafe_allow_html=True)

# --- Mostrar el contenido en base a la sección seleccionada ---
st.markdown('<div id="main-content">', unsafe_allow_html=True)

# Usamos `st.radio` para cambiar entre secciones sin recargar la página.
seccion = st.radio("Selecciona una sección", ["Home", "Craft", "Materiales", "Especificaciones", "Configuracion"])

if seccion == "Home":
    if logo_data:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{logo_data}" style="width:1000px; max-width:85vw; height:auto;
            filter: drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
        </div>
        """, unsafe_allow_html=True)
    st.write("Bienvenido a AstroCycle 🌌, la app para tu prototipo estelar.")

elif seccion == "Craft":
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")

elif seccion == "Materiales":
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")

elif seccion == "Especificaciones":
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)

elif seccion == "Configuracion":
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")

st.markdown('</div>', unsafe_allow_html=True)
