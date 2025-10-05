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

    /* ---------- Barra lateral fija ---------- */
    .sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 240px;
        height: 100%;
        background: rgba(15, 15, 15, 0.7);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
        display: flex;
        flex-direction: column;
        padding: 20px 10px;
        z-index: 10;
    }

    .sidebar h2 {
        color: #fff;
        text-align: center;
        margin-bottom: 30px;
    }

    .sidebar button {
        background: rgba(255,255,255,0.05);
        color: #fff;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 14px;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        width: 100%;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .sidebar button:hover {
        background: rgba(255,255,255,0.15);
        transform: translateY(-1px);
    }

    .sidebar button.active {
        background: rgba(255,255,255,0.25);
        border-color: rgba(255,255,255,0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }

    /* ---------- Contenido principal ---------- */
    .main-content {
        margin-left: 260px;
        padding: 20px 40px;
    }

    .main-title {
        color: #ffffff;
        font-size: 36px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .muted {
        color: rgba(230,230,230,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Fondo ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Estado del botón ----------
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# ---------- Barra lateral personalizada ----------
st.markdown(
    f"""
    <div class="sidebar">
        <h2>🚀 AstroCycle</h2>
        <form action="?page=🏠 Home"><button class="{'active' if st.session_state.page=='🏠 Home' else ''}">🏠 Home</button></form>
        <form action="?page=📊 Datos Generales"><button class="{'active' if st.session_state.page=='📊 Datos Generales' else ''}">📊 Datos Generales</button></form>
        <form action="?page=🤖 Status"><button class="{'active' if st.session_state.page=='🤖 Status' else ''}">🤖 Status</button></form>
        <form action="?page=🛠️ Craft"><button class="{'active' if st.session_state.page=='🛠️ Craft' else ''}">🛠️ Craft</button></form>
        <form action="?page=⚙️ Especificaciones"><button class="{'active' if st.session_state.page=='⚙️ Especificaciones' else ''}">⚙️ Especificaciones</button></form>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Control manual de navegación ----------
params = st.query_params
if "page" in params:
    st.session_state.page = params["page"]

page = st.session_state.page

# ---------- Contenido dinámico ----------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

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
        st.error("❌ No se encontró el archivo 'Rove_prototipo1.glb'. Súbelo a la carpeta del proyecto.")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Nota inferior ----------
st.markdown("""
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(255,255,255,0.6); font-size:12px;">
        ⚙️ Sube <b>video.mp4</b> y <b>Rove_prototipo1.glb</b> a esta carpeta antes de publicar en Streamlit Cloud.
    </div>
""", unsafe_allow_html=True)
