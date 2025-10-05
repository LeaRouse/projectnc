import streamlit as st
from pathlib import Path
import base64
from mimetypes import guess_type
import streamlit.components.v1 as components

st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

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
    return "<!-- no video -->"

st.markdown(get_video_html(), unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

icons = {
    "Home": img_data_uri("home.png"),
    "Craft": img_data_uri("craft.png"),
    "Materiales": img_data_uri("materiales.png"),
    "Especificaciones": img_data_uri("especificaciones.png"),
    "Configuracion": img_data_uri("config.png"),
    "Logo": img_data_uri("logotipoastrocycle2.png"),
}

if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# CSS
st.markdown("""
<style>
.stApp { background: transparent !important; color: #d0d0d0; }
video#bgvid {
    position: fixed; top:50%; left:50%;
    min-width:100%; min-height:100%;
    transform:translate(-50%, -50%);
    object-fit:cover; z-index:-3;
    filter: brightness(0.65) contrast(1.05);
}
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }
.sidebar-line {
    position: fixed; top:0; left:230px; height:100vh; width:2px;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%,
                                 rgba(255,255,255,0.25) 30%,
                                 rgba(255,255,255,0.25) 70%,
                                 rgba(255,255,255,0) 100%);
    z-index:1; backdrop-filter: blur(2px);
}
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
.icon-button:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}
.icon-button img {
    width:100%;
    height:100%;
    object-fit: cover;
    border-radius: inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.icon-button:hover img {
    filter: brightness(1.05) contrast(1.1);
}
#btn-home, #btn-craft, #btn-mat {
    left: 25px;
    width: 180px;
    height: 180px;
    border-radius: 22px;
}
#btn-home { top: 12%; }
#btn-craft { top: 41%; }
#btn-mat { top: 70%; }
#btn-spec, #btn-config {
    border-radius: 50%;
    width: 80px;
    height: 80px;
}
#btn-spec { right: 25px; top: 80px; }
#btn-config { right: 25px; bottom: 30px; }
#main-content { margin-left: 260px; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# Botones visuales con onclick que envían mensaje
st.markdown(f"""
<div class="icon-button" id="btn-home" onclick="window.parent.postMessage({{type:'NAV', page:'Home'}}, '*')">
    <img src="{icons['Home']}">
</div>
<div class="icon-button" id="btn-craft" onclick="window.parent.postMessage({{type:'NAV', page:'Craft'}}, '*')">
    <img src="{icons['Craft']}">
</div>
<div class="icon-button" id="btn-mat" onclick="window.parent.postMessage({{type:'NAV', page:'Materiales'}}, '*')">
    <img src="{icons['Materiales']}">
</div>
<div class="icon-button" id="btn-spec" onclick="window.parent.postMessage({{type:'NAV', page:'Especificaciones'}}, '*')">
    <img src="{icons['Especificaciones']}">
</div>
<div class="icon-button" id="btn-config" onclick="window.parent.postMessage({{type:'NAV', page:'Configuracion'}}, '*')">
    <img src="{icons['Configuracion']}">
</div>
""", unsafe_allow_html=True)

# Script que escucha los mensajes y actualiza el estado con componentes.html
components.html("""
<script>
window.addEventListener('message', event => {
    const msg = event.data;
    if (msg.type === 'NAV' && msg.page) {
        // envío al Streamlit
        window.parent.postMessage({isStreamlitMessage: true, page_to_nav: msg.page}, '*');
    }
});
</script>
""", height=0, width=0)

# Script para capturar el mensaje que envía el script anterior (funciona en Streamlit)
# usamos componentes.html con atributo "allowScript" o usando custom message handler
components.html("""
<script>
const targetOrigin = '*';
window.addEventListener('message', (event) => {
    const d = event.data;
    if (d.isStreamlitMessage && d.page_to_nav) {
        // Cambiamos la URL sin recargar
        window.history.replaceState(null, '', `?nav=${d.page_to_nav}`);
        // Trigger recarga mínima de la app
        window.location.reload();
    }
});
</script>
""", height=0, width=0)

# Leer parámetro de URL
params = st.experimental_get_query_params()
if "nav" in params:
    st.session_state.pagina = params["nav"][0]

# Contenido dinámico
st.markdown('<div id="main-content">', unsafe_allow_html=True)

pag = st.session_state.pagina

if pag == "Home":
    if icons["Logo"]:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{icons['Logo']}" style="width:1000px; max-width:85vw; height:auto;
            filter: drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
        </div>
        """, unsafe_allow_html=True)

elif pag == "Craft":
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")

elif pag == "Materiales":
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")

elif pag == "Especificaciones":
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)

elif pag == "Configuracion":
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")

st.markdown('</div>', unsafe_allow_html=True)
