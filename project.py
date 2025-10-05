import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- Función para imágenes ---
def img_data_uri(path_str: str):
    p = Path(path_str)
    if not p.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode("utf-8")

icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# --- Estado ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# --- CSS ---
st.markdown("""
<style>
.stApp {background:transparent !important; color:#d0d0d0 !important;}
.icon-left {position:fixed; left:25px; width:180px; height:180px; border-radius:22px; background: rgba(35,35,35,0.5); display:flex; justify-content:center; align-items:center; cursor:pointer; z-index:5;}
.icon-left:hover {background: rgba(255,255,255,0.08); transform:scale(1.05);}
#home-btn {top:12%;}
#craft-btn {top:41%;}
#mat-btn {top:70%;}
.icon-right {position:fixed; width:80px; height:80px; border-radius:50%; cursor:pointer; display:flex; justify-content:center; align-items:center; z-index:5; background: rgba(35,35,35,0.85);}
.icon-right:hover {transform:scale(1.1); background: rgba(70,70,70,0.95);}
#spec-btn {right:25px; top:80px;}
#conf-btn {right:25px; bottom:30px;}
#main-content {position:fixed; left:250px; top:0; bottom:0; right:0; overflow-y:auto; padding:30px;}
</style>
""", unsafe_allow_html=True)

# --- BOTONES VISUALES ---
def btn_html(data_uri):
    return f'<img src="{data_uri}" style="width:100%; height:100%; object-fit:cover; border-radius:inherit;">'

st.markdown(f"""
<div id="home-btn" class="icon-left">{btn_html(icon_home)}</div>
<div id="craft-btn" class="icon-left">{btn_html(icon_craft)}</div>
<div id="mat-btn" class="icon-left">{btn_html(icon_mat)}</div>
<div id="spec-btn" class="icon-right">{btn_html(icon_spec)}</div>
<div id="conf-btn" class="icon-right">{btn_html(icon_conf)}</div>
""", unsafe_allow_html=True)

# --- BOTONES NATIVOS INVISIBLES (solo clic real) ---
cols = st.columns([0.03, 0.97])  # primera columna super estrecha para botones invisibles

with cols[0]:
    if st.button("Home", key="btn_home_invis"):
        st.session_state.pagina = "Home"
    if st.button("Craft", key="btn_craft_invis"):
        st.session_state.pagina = "Craft"
    if st.button("Materiales", key="btn_mat_invis"):
        st.session_state.pagina = "Materiales"
    if st.button("Especificaciones", key="btn_spec_invis"):
        st.session_state.pagina = "Especificaciones"
    if st.button("Configuración", key="btn_conf_invis"):
        st.session_state.pagina = "Configuracion"

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
elif pagina=="Configuracion":
    st.markdown('<div id="main-content"><h2>🧩 Configuración</h2><p>Opciones de configuración de la app.</p></div>', unsafe_allow_html=True)
