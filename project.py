import streamlit as st
from pathlib import Path
import base64

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

    /* 🔹 Barra lateral fija personalizada */
    .sidebar-fixed {
        position: fixed;
        top: 0;
        left: 0;
        height: 100vh;
        width: 240px;
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
    }

    .sidebar-fixed button {
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
        margin-bottom: 12px;
        cursor: pointer;
        transition: 0.15s;
    }

    .sidebar-fixed button:hover {
        background: rgba(255,255,255,0.15);
        transform: translateY(-1px);
    }

    .sidebar-fixed button.active {
        background: rgba(255,255,255,0.25);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    /* 🔹 Contenido principal */
    .main-content {
        margin-left: 260px;
        padding: 20px 40px;
        color: white;
    }

    .main-title {
        font-size: 36px;
        margin-bottom: 8px;
    }

    .muted {
        color: rgba(230,230,230,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Fondo ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Sidebar manual ----------
st.markdown("""
<div class="sidebar-fixed">
    <h2>🚀 AstroCycle</h2>
    <form action="#" method="get">
        <button name="page" value="home" class="sidebar-btn">🏠 Home</button>
        <button name="page" value="datos">📊 Datos Generales</button>
        <button name="page" value="status">🤖 Status</button>
        <button name="page" value="craft">🛠️ Craft</button>
        <button name="page" value="especificaciones">⚙️ Especificaciones</button>
        <button name="page" value="configuracion">🧩 Configuración</button>
    </form>
</div>
""", unsafe_allow_html=True)

# ---------- Obtener la página actual ----------
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# ---------- Contenido dinámico ----------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if page == "home":
    st.markdown("<h1 class='main-title'>AstroCycle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='muted'>Panel principal del rover interplanetario.</p>", unsafe_allow_html=True)

elif page == "datos":
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
        st.metric("Última revisión", "2025-10-05")

elif page == "status":
    st.markdown("<h2 class='main-title'>Estado del Sistema</h2>", unsafe_allow_html=True)
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif page == "craft":
    st.markdown("<h2 class='main-title'>Sección de Fabricación</h2>", unsafe_allow_html=True)
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")

elif page == "especificaciones":
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

elif page == "configuracion":
    st.markdown("<h2 class='main-title'>Configuración del Sistema</h2>", unsafe_allow_html=True)
    st.write("Ajustes generales, idioma, calibración de sensores y mantenimiento preventivo.")

st.markdown("</div>", unsafe_allow_html=True)
