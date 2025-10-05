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

    .menu-container {
        background: rgba(10,10,10,0.35);
        backdrop-filter: blur(6px);
        border-radius: 12px;
        padding: 18px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .menu-button {
        background: rgba(255,255,255,0.05);
        color: #fff;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 12px;
        text-align: left;
        font-weight: 600;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .menu-button:hover {
        background: rgba(255,255,255,0.12);
        transform: translateX(3px);
    }

    .menu-button.active {
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.2);
    }

    .main-title {
        color: #ffffff;
        font-size: 34px;
        margin-bottom: 8px;
    }

    .muted {color: rgba(230,230,230,0.8);}
    </style>
""", unsafe_allow_html=True)

# ---------- Fondo animado ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- Layout principal ----------
col_menu, col_content = st.columns([1, 4])

with col_menu:
    st.markdown("<div class='menu-container'>", unsafe_allow_html=True)
    st.markdown("### 🚀 AstroCycle")

    pages = {
        "🏠 Home": "Home",
        "📊 Datos Generales": "Datos Generales",
        "🤖 Status": "Status",
        "🛠️ Craft": "Craft",
        "⚙️ Especificaciones": "Especificaciones",
        "🧩 Configuración": "Configuración"
    }

    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    for icon_text in pages.keys():
        if st.button(icon_text, key=icon_text, use_container_width=True):
            st.session_state.page = icon_text

    st.markdown("</div>", unsafe_allow_html=True)

with col_content:
    page = st.session_state.page

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

    elif page == "🧩 Configuración":
        st.markdown("<h2 class='main-title'>Configuración</h2>", unsafe_allow_html=True)
        st.write("Ajustes y parámetros del sistema.")
        st.toggle("Modo oscuro", value=True)
        st.selectbox("Idioma", ["Español", "Inglés"])
        st.slider("Volumen general", 0, 100, 70)
        st.button("Guardar cambios", type="primary")

# ---------- Nota inferior ----------
st.markdown("""
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(255,255,255,0.6); font-size:12px;">
        ⚙️ Sube <b>video.mp4</b> y <b>Rove_prototipo1.glb</b> a esta carpeta antes de publicar en Streamlit Cloud.
    </div>
""", unsafe_allow_html=True)
