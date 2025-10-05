import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# --- Configuración ---
st.set_page_config(page_title="AstroCycle 🌌", layout="wide")

# --- Video de fondo ---
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

# --- CSS ---
st.markdown("""
<style>
.stApp {background: transparent !important; color: #d0d0d0 !important;}
video#bgvid {position: fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform: translate(-50%, -50%); object-fit: cover; z-index:-3; filter: brightness(0.65) contrast(1.05);}
.bg-overlay {position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2;}

/* Botones flotantes derecha */
.floating-button {
    position: fixed;
    z-index: 5;
    width: 140px;
    padding: 12px;
    border-radius: 14px;
    border: none;
    font-weight: bold;
    color: #f1f1f1;
    background-color: rgba(30,30,30,0.85);
    cursor: pointer;
    transition: all 0.25s ease;
}
.floating-button:hover { background-color: rgba(70,70,70,0.95); transform: scale(1.05); }
#btn-top-right { right: 20px; top: 80px; }
#btn-bottom-right { right: 20px; bottom: 30px; }
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Layout ---
col_left, col_right = st.columns([1, 4])

# --- Botones izquierda ---
with col_left:
    st.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
    st.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
    st.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))

# --- Botones derecha flotantes ---
st.markdown(f"""
<button class="floating-button" id="btn-top-right" onclick="window.parent.postMessage({{type: 'Especificaciones'}}, '*')">⚙️ Especificaciones</button>
<button class="floating-button" id="btn-bottom-right" onclick="window.parent.postMessage({{type: 'Configuracion'}}, '*')">🧩 Configuración</button>
""", unsafe_allow_html=True)

# --- Captura mensajes botones flotantes ---
components.html("""
<script>
window.addEventListener('message', (event) => {
    const type = event.data.type;
    if (type) {
        document.dispatchEvent(new CustomEvent('updatePagina', {detail: type}));
    }
});
</script>
""", height=0, width=0)

# --- Contenido dinámico columna derecha ---
with col_right:
    pagina = st.session_state.pagina

    if pagina == "Home":
        st.title("🏠 Home")
        st.write("Bienvenido a **AstroCycle**. Explora todo desde aquí.")
        IMG_FILE = Path("logotipoastrocycle.png")
        if IMG_FILE.exists():
            st.image(str(IMG_FILE), use_column_width=True, caption="Logotipo AstroCycle")
        else:
            st.warning("No se encontró logotipoastrocycle.png")

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
