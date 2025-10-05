import streamlit as st
from pathlib import Path
import base64

# ---------- Configuración ----------
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---------- Archivos esperados ----------
VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

# ---------- Fondo animado ----------
def get_video_html():
    if VIDEO_FILE.exists():
        data = VIDEO_FILE.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f'''
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        '''
    else:
        return "<!-- No se encontró video.mp4 -->"

# ---------- Estilos ----------
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}

    video#bgvid {
        position: fixed;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        transform: translate(-50%, -50%);
        object-fit: cover;
        z-index: -2;
        filter: brightness(0.65) contrast(1.05) saturate(1.05);
    }

    .bg-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.45);
        z-index: -1;
    }

    /* 🔹 Sin espacio superior extra */
    .block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    /* 🔹 Barra lateral fija y compacta */
    section[data-testid="stSidebar"] {
        background: rgba(10,10,10,0.35);
        backdrop-filter: blur(6px);
        border-right: 1px solid rgba(255,255,255,0.1);
        height: 100vh;
        position: fixed;
        left: 0;
        top: 0;
        width: 250px;
        padding: 10px 16px;
    }

    /* 🔹 Ajuste del contenido para que no quede detrás */
    div[data-testid="stVerticalBlock"] {
        padding-left: 270px !important;
    }

    div[role="radiogroup"] > label {
        display: block;
        width: 100%;
        height: 50px;
        line-height: 50px;
        padding-left: 16px;
        margin-bottom: 10px;
        border-radius: 8px;
        background: rgba(255,255,255,0.05);
        color: #fff;
        font-weight: 600;
        transition: all 0.14s ease;
        box-sizing: border-box;
    }

    div[role="radiogroup"] > label:hover {
        background: rgba(255,255,255,0.1);
        cursor: pointer;
    }

    div[role="radiogroup"] > label[aria-checked="true"] {
        background: rgba(255,255,255,0.2);
        box-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }

    .main-title {
        color: #ffffff;
        font-size: 34px;
        margin: 0;
    }

    .muted {
        color: rgba(230,230,230,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Video de fondo ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.title("🚀 AstroCycle")

pages = [
    "🏠 Home",
    "📊 Datos Generales",
    "🤖 Status",
    "🛠️ Craft",
    "⚙️ Especificaciones",
    "⚙️ Configuración"
]
page = st.sidebar.radio("", pages, index=0)

# ---------- Contenido ----------
if page == "🏠 Home":
    st.markdown("<h1 class='main-title'>AstroCycle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='muted'>Panel principal del rover interplanetario.</p>", unsafe_allow_html=True)

elif page == "📊 Datos Generales":
    st.markdown("<h2 class='main-title'>Datos Generales</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nombre", "Rover X-Proto")
        st.metric("Modelo", "Rove 2025")
    with c2:
        st.metric("Código", "RC-002")
        st.metric("Ubicación", "Hangar C")
    with c3:
        st.metric("Estado", "Operativo")
        st.metric("Última revisión", "2025-10-04")

elif page == "🤖 Status":
    st.markdown("<h2 class='main-title'>Estado del Sistema</h2>", unsafe_allow_html=True)
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")
    st.radio("Modo de energía", ["Normal", "Ahorro", "Reinicio"])

elif page == "🛠️ Craft":
    st.markdown("<h2 class='main-title'>Sección de Fabricación</h2>", unsafe_allow_html=True)
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")

elif page == "⚙️ Especificaciones":
    st.markdown("<h2 class='main-title'>Especificaciones Técnicas</h2>", unsafe_allow_html=True)
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

elif page == "⚙️ Configuración":
    st.markdown("<h2 class='main-title'>Configuración del Sistema</h2>", unsafe_allow_html=True)
    st.write("Ajustes generales, idioma, calibración de sensores y mantenimiento preventivo.")

# ---------- Nota inferior ----------
st.markdown("""
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(255,255,255,0.6); font-size:12px;">
        ⚙️ Sube <b>video.mp4</b> y <b>Rove_prototipo1.glb</b> a esta carpeta antes de publicar.
    </div>
""", unsafe_allow_html=True)
