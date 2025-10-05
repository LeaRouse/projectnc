import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
from mimetypes import guess_type

# -----------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# -----------------------------------------------------------------------
# VIDEO DE FONDO
# -----------------------------------------------------------------------
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

# -----------------------------------------------------------------------
# UTIL: PNG/JPG -> data URI
# -----------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        st.warning(f"No se encontró {path_str}")
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# -----------------------------------------------------------------------
# CARGA DE ICONOS
# -----------------------------------------------------------------------
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# -----------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# -----------------------------------------------------------------------
# CSS GLOBAL
# -----------------------------------------------------------------------
st.markdown("""
<style>
.stApp { background: transparent !important; color:#d0d0d0 !important; }
