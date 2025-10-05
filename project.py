import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="AstroCycle", layout="wide")

VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

def get_video_html():
    if VIDEO_FILE.exists():
        b64 = base64.b64encode(VIDEO_FILE.read_bytes()).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        """
    return ""

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
    filter: brightness(0.65);
}

.bg-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: -1;
}

.layout {
    display: flex;
    height: 100vh;
}

.sidebar {
    width: 240px;
    background: rgba(20,20,20,0.5);
    backdrop-filter: blur(8px);
    padding: 20px;
    border-right: 1px solid rgba(255,255,255,0.1);
    box-sizing: border-box;
}

.content {
    flex: 1;
    padding: 40px;
    color: white;
    overflow-y: auto;
}

button {
    background: rgba(255,255,255,0.05);
    border: none;
    border-radius: 8px;
    color: white;
    padding: 12px;
    margin-bottom: 10px;
    width: 100%;
    text-align: left;
    font-weight: 600;
    cursor: pointer;
}
button:hover {
    background: rgba(255,255,255,0.15);
}
</style>
""", unsafe_allow_html=True)

st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown("<div class='bg-overlay'></div>", unsafe_allow_html=True)

st.markdown("<div class='layout'>", unsafe_allow_html=True)

# Barra lateral
with st.container():
    st.markdown("<div class='sidebar'>", unsafe_allow_html=True)
    st.markdown("### 🚀 AstroCycle")

    pages = ["🏠 Home", "📊 Datos Generales", "🤖 Status", "🛠️ Craft", "⚙️ Especificaciones", "🧩 Configuración"]
    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    for p in pages:
        if st.button(p, key=p):
            st.session_state.page = p
    st.markdown("</div>", unsafe_allow_html=True)

# Contenido
st.markdown("<div class='content'>", unsafe_allow_html=True)
page = st.session_state.page

if page == "🏠 Home":
    st.title("AstroCycle")
    st.write("Panel principal del rover interplanetario.")

elif page == "📊 Datos Generales":
    st.header("Datos Generales")
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
    st.header("Estado del Sistema")
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif page == "🛠️ Craft":
    st.header("Sección de Fabricación")
    st.write("Visualiza el proceso de ensamblaje y mantenimiento del rover.")

elif page == "⚙️ Especificaciones":
    st.header("Especificaciones Técnicas")
    if MODEL_FILE.exists():
        st.markdown(f"""
        <model-viewer src="{MODEL_FILE}" alt="Modelo 3D"
            camera-controls auto-rotate style="width:100%;height:500px;background:transparent;">
        </model-viewer>
        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ No se encontró el archivo del modelo 3D.")

elif page == "🧩 Configuración":
    st.header("Configuración")
    st.toggle("Modo oscuro", value=True)
    st.selectbox("Idioma", ["Español", "Inglés"])
    st.slider("Volumen general", 0, 100, 70)
    st.button("Guardar cambios")

st.markdown("</div></div>", unsafe_allow_html=True)
