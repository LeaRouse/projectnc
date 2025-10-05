import streamlit as st
from pathlib import Path
import base64

# ---------- Configuración ----------
st.set_page_config(page_title="AstroCycle", layout="wide")

VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

# ---------- Fondo animado ----------
def get_video_html():
    if VIDEO_FILE.exists():
        data = VIDEO_FILE.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        """
    else:
        return "<!-- no video -->"

# ---------- Estilos ----------
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    body {margin: 0; padding: 0;}

    video#bgvid {
        position: fixed;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        transform: translate(-50%, -50%);
        object-fit: cover;
        z-index: -3;
        filter: brightness(0.65) contrast(1.05);
    }

    .bg-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.45);
        z-index: -2;
    }

    /* Barra lateral fija */
    .sidebar-fixed {
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 250px;
        background: rgba(10,10,10,0.35);
        backdrop-filter: blur(6px);
        border-right: 1px solid rgba(255,255,255,0.1);
        padding: 24px 16px;
        box-sizing: border-box;
        z-index: 10;
    }

    .sidebar-fixed h2 {
        color: white;
        font-size: 22px;
        margin-bottom: 24px;
        text-align: center;
    }

    .sidebar-btn {
        display: block;
        width: 100%;
        background: rgba(255,255,255,0.07);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 12px;
        text-align: left;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        cursor: pointer;
        transition: 0.15s;
    }

    .sidebar-btn:hover {
        background: rgba(255,255,255,0.15);
        transform: translateY(-1px);
    }

    .sidebar-btn.active {
        background: rgba(255,255,255,0.25);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    /* Contenido principal */
    .main-content {
        margin-left: 270px;
        padding: 30px 50px;
        color: white;
    }

    .main-title {
        font-size: 36px;
        margin-bottom: 10px;
    }

    .muted {
        color: rgba(230,230,230,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Fondo animado ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Estado de página ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- Barra lateral ----------
st.markdown('<div class="sidebar-fixed">', unsafe_allow_html=True)
st.markdown("<h2>🚀 AstroCycle</h2>", unsafe_allow_html=True)

def sidebar_button(label, value, emoji=""):
    active = "active" if st.session_state.page == value else ""
    if st.button(f"{emoji} {label}", key=value, use_container_width=True):
        st.session_state.page = value
    st.markdown(f"<style>div[data-testid='stButton'][key='{value}'] button{{background:{'rgba(255,255,255,0.25)' if active else 'rgba(255,255,255,0.07)'}};}}</style>", unsafe_allow_html=True)

sidebar_button("Home", "home", "🏠")
sidebar_button("Datos Generales", "datos", "📊")
sidebar_button("Status", "status", "🤖")
sidebar_button("Craft", "craft", "🛠️")
sidebar_button("Especificaciones", "especificaciones", "⚙️")
sidebar_button("Configuración", "config", "🧩")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Contenido dinámico ----------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

page = st.session_state.page

if page == "home":
    st.markdown("<h1 class='main-title'>AstroCycle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='muted'>Panel principal del rover interplanetario.</p>", unsafe_allow_html=True)

elif page == "datos":
    st.markdown("<h2 class='main-title'>📊 Datos Generales</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nombre", "Rover X-Proto")
        st.metric("Modelo", "Rove 2025")
    with c2:
        st.metric("Código", "RC-002")
        st.metric("Ubicación", "Hangar C")
    with c3:
        st.metric("Estado", "Operativo")
        st.metric("Última revisión", "2025-10-05")

elif page == "status":
    st.markdown("<h2 class='main-title'>🤖 Estado del Sistema</h2>", unsafe_allow_html=True)
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif page == "craft":
    st.markdown("<h2 class='main-title'>🛠️ Sección de Fabricación</h2>", unsafe_allow_html=True)
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")

elif page == "especificaciones":
    st.markdown("<h2 class='main-title'>⚙️ Especificaciones Técnicas</h2>", unsafe_allow_html=True)
    st.write("Incluye la vista 3D del modelo del rover:")
    if MODEL_FILE.exists():
        st.markdown(f"""
            <model-viewer src="Rove_prototipo1.glb" alt="Modelo 3D del Rover"
                camera-controls auto-rotate exposure="1"
                style="width:100%; height:600px; background: transparent;">
            </model-viewer>
            <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ No se encontró el archivo 'Rove_prototipo1.glb'.")

elif page == "config":
    st.markdown("<h2 class='main-title'>🧩 Configuración del Sistema</h2>", unsafe_allow_html=True)
    st.write("Ajustes generales, idioma, calibración de sensores y mantenimiento preventivo.")

st.markdown("</div>", unsafe_allow_html=True)
