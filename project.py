import streamlit as st
from pathlib import Path
import base64

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# ---------------------------------------------------------------------------
# UTILS
# ---------------------------------------------------------------------------
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

def bg_video_html():
    video = Path("video.mp4")
    if video.exists():
        data = video.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
          <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    return "<!-- no video.mp4 -->"

# ---------------------------------------------------------------------------
# ASSETS
# ---------------------------------------------------------------------------
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# ---------------------------------------------------------------------------
# STATE
# ---------------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# ---------------------------------------------------------------------------
# BACKGROUND + CSS
# ---------------------------------------------------------------------------
st.markdown(bg_video_html(), unsafe_allow_html=True)

st.markdown("""
<style>
.stApp { background: transparent !important; color: #d0d0d0 !important; }
video#bgvid { position: fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform:translate(-50%, -50%); object-fit:cover; z-index:-3; filter: brightness(0.65) contrast(1.05); }
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

.icon-button {
  position: fixed; display:flex; justify-content:center; align-items:center;
  overflow:hidden; cursor:pointer; transition: transform .2s ease;
  z-index:5;
}
.icon-button:hover { transform: scale(1.05); }

.icon-button img { width:100%; height:100%; object-fit:cover; border-radius:inherit; }

#btn-home, #btn-craft, #btn-mat { left:25px; width:180px; height:180px; border-radius:22px; }
#btn-home { top:12%; } #btn-craft { top:41%; } #btn-mat { top:70%; }

#btn-spec, #btn-config { right:25px; border-radius:50%; width:80px; height:80px; }
#btn-spec { top:80px; } #btn-config { bottom:30px; }

h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# FUNCION PARA CREAR BOTONES HTML/JS
# ---------------------------------------------------------------------------
def create_button_html(id_name, data_uri, target_page):
    return f"""
    <div id="{id_name}" class="icon-button" onclick="window.parent.postMessage({{'type':'{target_page}'}}, '*')">
        <img src="{data_uri}" />
    </div>
    """

st.markdown(
    create_button_html("btn-home", icon_home, "Home") +
    create_button_html("btn-craft", icon_craft, "Craft") +
    create_button_html("btn-mat", icon_mat, "Materiales") +
    create_button_html("btn-spec", icon_spec, "Especificaciones") +
    create_button_html("btn-config", icon_conf, "Configuracion"),
    unsafe_allow_html=True
)

# ---------------------------------------------------------------------------
# JS para recibir clics
# ---------------------------------------------------------------------------
import streamlit.components.v1 as components
components.html("""
<script>
window.addEventListener('message', (event) => {
    const type = event.data.type;
    if(type){
        document.dispatchEvent(new CustomEvent('updatePagina',{detail:type}));
    }
});
</script>
""", height=0, width=0)

# ---------------------------------------------------------------------------
# Escuchar eventos
# ---------------------------------------------------------------------------
if 'last_event' not in st.session_state:
    st.session_state.last_event = None

# Captura de JS
if st.session_state.last_event is None:
    st.session_state.last_event = "Home"

# Usando streamlit para capturar evento de JS
# Esto funciona gracias al CustomEvent "updatePagina"
from streamlit_js_eval import streamlit_js_eval
pagina_js = streamlit_js_eval(
    "document.addEventListener('updatePagina', e => {window.parent.postMessage(e.detail,'*');});",
    key="js_eval"
)
if pagina_js:
    st.session_state.pagina = pagina_js

# ---------------------------------------------------------------------------
# CONTENIDO DINÁMICO
# ---------------------------------------------------------------------------
pagina = st.session_state.pagina

if pagina == "Home":
    st.markdown('<div style="position:fixed; left:260px; right:0; top:0; bottom:0; display:flex; justify-content:center; align-items:center; z-index:0;">', unsafe_allow_html=True)
    if logo_data:
        st.markdown(f'<img src="{logo_data}" style="width:1000px; max-width:85vw; height:auto; filter: drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina == "Craft":
    st.header("🛠️ Craft")
elif pagina == "Materiales":
    st.header("📦 Materiales")
elif pagina == "Especificaciones":
    st.header("⚙️ Especificaciones")
    components.iframe("https://learouse.github.io/prototipo/", height=600, width="100%", scrolling=True)
elif pagina == "Configuracion":
    st.header("🧩 Configuración")
