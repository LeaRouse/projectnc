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
        width: 260px;
        height: 100%;
        background: rgba(15, 15, 15, 0.7);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
        display: flex;
        flex-direction: column;
        padding: 20px 14px;
        z-index: 10;
        overflow-y: auto;
    }

    .sidebar h2 {
        color: #fff;
        text-align: center;
        margin-bottom: 20px;
    }

    .sidebar button {
        background: rgba(255,255,255,0.05);
        color: #fff;
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 10px;
        width: 100%;
        transition: all 0.2s ease;
        cursor: pointer;
        text-align: left;
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

    .sub-btn {
        margin-left: 10px;
        font-size: 14px !important;
        background: rgba(255,255,255,0.03);
    }

    .main-content {
        margin-left: 280px;
        padding: 20px 40px;
    }

    .main-title {
        color: #ffffff;
        font-size: 36px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .sub-title {
        color: #b0c4de;
        font-size: 24px;
        margin-top: 4px;
        margin-bottom: 16px;
    }

    .muted {
        color: rgba(230,230,230,0.8);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Fondo ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Estado ----------
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "subpage" not in st.session_state:
    st.session_state.subpage = None

# ---------- Barra lateral ----------
st.markdown('<div class="sidebar">', unsafe_allow_html=True)
st.markdown("<h2>🚀 AstroCycle</h2>", unsafe_allow_html=True)

def nav_button(label, target_page):
    active = "active" if st.session_state.page == target_page else ""
    if st.button(label, key=label, use_container_width=True):
        st.session_state.page = target_page
        st.session_state.subpage = None
    st.markdown(f"<style>div[data-testid='stButton'] button#{label} {{border-radius:10px;}}</style>", unsafe_allow_html=True)

# Páginas principales
main_pages = ["🏠 Home", "📊 Datos Generales", "🤖 Status", "🛠️ Craft", "⚙️ Especificaciones"]
for p in main_pages:
    nav_button(p, p)

# Subpáginas (solo visibles en "📊 Datos Generales")
if st.session_state.page == "📊 Datos Generales":
    if st.button("📄 Información del Rover", key="sub_info", use_container_width=True):
        st.session_state.subpage = "info"
    if st.button("📡 Telemetría", key="sub_tele", use_container_width=True):
        st.session_state.subpage = "tele"
    if st.button("🧰 Mantenimiento", key="sub_maint", use_container_width=True):
        st.session_state.subpage = "maint"

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Contenido principal ----------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

page = st.session_state.page
sub = st.session_state.subpage

if page == "🏠 Home":
    st.markdown("<h1 class='main-title'>AstroCycle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='muted'>Panel principal del rover interplanetario.</p>", unsafe_allow_html=True)

elif page == "📊 Datos Generales":
    st.markdown("<h1 class='main-title'>📊 Datos Generales</h1>", unsafe_allow_html=True)
    if sub is None:
        st.markdown("<p class='muted'>Selecciona una subpágina a la izquierda.</p>", unsafe_allow_html=True)
    elif sub == "info":
        st.markdown("<h2 class='sub-title'>📄 Información del Rover</h2>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Nombre", "Rover X-Proto")
            st.metric("Modelo", "Rove 2025")
        with c2:
            st.metric("Código", "RC-002")
            st.metric("Ubicación", "Hangar C")
    elif sub == "tele":
        st.markdown("<h2 class='sub-title'>📡 Telemetría</h2>", unsafe_allow_html=True)
        st.line_chart({"Temperatura °C": [18, 19, 21, 20, 22, 23, 22]})
        st.line_chart({"Batería %": [100, 97, 94, 92, 89, 86, 84]})
    elif sub == "maint":
        st.markdown("<h2 class='sub-title'>🧰 Mantenimiento</h2>", unsafe_allow_html=True)
        st.write("- Último chequeo: 2025-10-04")
        st.write("- Componentes reemplazados: módulo térmico y panel solar secundario.")

elif page == "🤖 Status":
    st.markdown("<h1 class='main-title'>🤖 Estado del Sistema</h1>", unsafe_allow_html=True)
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif page == "🛠️ Craft":
    st.markdown("<h1 class='main-title'>🛠️ Sección de Fabricación</h1>", unsafe_allow_html=True)
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")

elif page == "⚙️ Especificaciones":
    st.markdown("<h1 class='main-title'>⚙️ Especificaciones Técnicas</h1>", unsafe_allow_html=True)
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

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Nota inferior ----------
st.markdown("""
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(255,255,255,0.6); font-size:12px;">
        ⚙️ Sube <b>video.mp4</b> y <b>Rove_prototipo1.glb</b> antes de publicar.
    </div>
""", unsafe_allow_html=True)
