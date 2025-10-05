import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- FUNCIONES ---
@st.cache_data
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

# --- IMÁGENES ---
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# --- ESTADO ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# --- VIDEO DE FONDO ---
VIDEO_FILE = Path("video.mp4")
def get_video_html():
    if VIDEO_FILE.exists():
        b64 = base64.b64encode(VIDEO_FILE.read_bytes()).decode("utf-8")
        return f"""
        <video autoplay loop muted playsinline id="bgvid">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
        <div class="bg-overlay"></div>
        """
    return "<!-- No se encontró video.mp4 -->"

st.markdown(get_video_html(), unsafe_allow_html=True)

# --- CSS ---
st.markdown("""
<style>
.stApp { background: transparent !important; color:#d0d0d0 !important; }
video#bgvid { position:fixed; top:50%; left:50%; min-width:100%; min-height:100%; transform:translate(-50%,-50%); object-fit:cover; z-index:-3; filter:brightness(0.65) contrast(1.05); }
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* BOTONES IZQUIERDA CUADRADOS TRANSPARENTES */
.icon-left {
    position:fixed; left:25px; width:180px; height:180px; border-radius:22px;
    background: rgba(35,35,35,0.5); display:flex; justify-content:center; align-items:center; cursor:pointer; z-index:5; transition: all .25s;
}
.icon-left:hover { background: rgba(255,255,255,0.08); transform: scale(1.05); }
#home-btn { top:12%; }
#craft-btn { top:41%; }
#mat-btn { top:70%; }

/* BOTONES DERECHA CIRCULARES VISIBLES */
.icon-right {
    position:fixed; width:80px; height:80px; border-radius:50%; cursor:pointer;
    display:flex; justify-content:center; align-items:center; z-index:5;
    background: rgba(35,35,35,0.85); transition: all .25s;
}
.icon-right:hover { transform: scale(1.1); background: rgba(70,70,70,0.95); }
#spec-btn { right:25px; top:80px; }
#conf-btn { right:25px; bottom:30px; }

/* CONTENIDO A LA DERECHA DE LOS BOTONES */
#main-content { position: fixed; left:250px; top:0; bottom:0; right:0; overflow-y:auto; padding:30px; }
</style>
""", unsafe_allow_html=True)

# --- BOTONES VISUALES ---
def btn_img(data_uri):
    if data_uri:
        return f'<img src="{data_uri}" style="width:100%; height:100%; object-fit:cover; border-radius:inherit;">'
    return '<div style="width:100%;height:100%;background:#333;"></div>'

# Botones izquierda (transparentes)
st.markdown(f"""
<div id="home-btn" class="icon-left">{btn_img(icon_home)}</div>
<div id="craft-btn" class="icon-left">{btn_img(icon_craft)}</div>
<div id="mat-btn" class="icon-left">{btn_img(icon_mat)}</div>
""", unsafe_allow_html=True)

# Botones derecha visibles
st.markdown(f"""
<div id="spec-btn" class="icon-right">{btn_img(icon_spec)}</div>
<div id="conf-btn" class="icon-right">{btn_img(icon_conf)}</div>
""", unsafe_allow_html=True)

# --- JS: solo los botones existentes cambian página ---
components.html(f"""
<script>
(function(){{
    const map = {{
        'home-btn':'Home',
        'craft-btn':'Craft',
        'mat-btn':'Materiales',
        'spec-btn':'Especificaciones',
        'conf-btn':'Configuracion'
    }};
    const doc = window.parent.document || document;
    Object.keys(map).forEach(function(id){{
        const el = doc.getElementById(id);
        if(el && !el._bound){{
            el._bound=true;
            el.addEventListener('click', function(){{
                const url = new URL(window.parent.location);
                url.searchParams.set('page', map[id]);
                window.parent.location = url;
            }});
        }}
    }});
}})();
</script>
""", height=0)

# --- CONTENIDO DINÁMICO ---
pagina = st.session_state.pagina

if pagina=="Home":
    st.markdown(f"""
    <div id="main-content" style="display:flex; flex-direction:column; align-items:center; padding-top:50px;">
        <h1>AstroCycle</h1>
        <img src="{logo_data}" style="width:600px; max-width:85vw; height:auto; filter:drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
    </div>
    """, unsafe_allow_html=True)
elif pagina=="Craft":
    st.markdown('<div id="main-content"><h2>🛠️ Craft</h2><p>Sección de construcción y desarrollo del prototipo.</p></div>', unsafe_allow_html=True)
elif pagina=="Materiales":
    st.markdown('<div id="main-content"><h2>📦 Materiales</h2><p>Aquí se muestran los materiales utilizados y sus detalles.</p></div>', unsafe_allow_html=True)
elif pagina=="Especificaciones":
    st.markdown('<div id="main-content"><h2>⚙️ Especificaciones</h2><p>Detalles técnicos y modelo 3D interactivo del prototipo.</p></div>', unsafe_allow_html=True)
    components.iframe("https://learouse.github.io/prototipo/", height=600, width="100%", scrolling=True)
elif pagina=="Configuracion":
    st.markdown('<div id="main-content"><h2>🧩 Configuración</h2><p>Opciones de configuración de la app.</p></div>', unsafe_allow_html=True)
