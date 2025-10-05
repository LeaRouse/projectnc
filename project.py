import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
from mimetypes import guess_type

# -------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# -------------------------------------------------------------------
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# -------------------------------------------------------------------
# FUNCIONES DE UTILIDAD
# -------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""
    mime, _ = guess_type(p.name)
    mime = mime or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

def get_video_html(video_file="video.mp4"):
    video = Path(video_file)
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

# -------------------------------------------------------------------
# CARGA DE IMÁGENES
# -------------------------------------------------------------------
icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")
logo_data  = img_data_uri("logotipoastrocycle2.png")

# -------------------------------------------------------------------
# ESTADO DE PÁGINA
# -------------------------------------------------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# -------------------------------------------------------------------
# FONDO + CSS
# -------------------------------------------------------------------
st.markdown(get_video_html(), unsafe_allow_html=True)

st.markdown("""
<style>
/* Fondo */
.stApp { background: transparent !important; color:#d0d0d0 !important; }
video#bgvid {
    position: fixed; top:50%; left:50%;
    min-width:100%; min-height:100%;
    transform:translate(-50%, -50%);
    object-fit:cover;
    z-index:-3;
    filter: brightness(0.65) contrast(1.05);
}
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* Línea divisoria */
.sidebar-line {
    position: fixed;
    top:0; left:230px; width:2px; height:100vh;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,0.25) 30%, rgba(255,255,255,0.25) 70%, rgba(255,255,255,0) 100%);
    z-index:1; backdrop-filter: blur(2px);
}

/* Botones flotantes */
.icon-button {
    position: fixed;
    background: rgba(35,35,35,0.75);
    border: 2px solid rgba(255,255,255,0.25);
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
    display: flex; justify-content:center; align-items:center;
    overflow:hidden;
}
.icon-button:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}
.icon-button img {
    width:100%; height:100%; object-fit:cover;
    border-radius:inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.icon-button:hover img { filter: brightness(1.05) contrast(1.1); }

/* Botones izquierda (cuadrados grandes) */
#btn-home, #btn-craft, #btn-mat {
    left:25px; width:180px; height:180px; border-radius:22px;
}
#btn-home  { top:12%; }
#btn-craft { top:41%; }
#btn-mat   { top:70%; }

/* Botones derecha (círculos) */
#btn-spec, #btn-config {
    border-radius:50%; width:80px; height:80px;
}
#btn-spec   { right:25px; top:80px; }
#btn-config { right:25px; bottom:30px; }

/* Contenido a la derecha */
#main-content {
    position: fixed;
    left:250px; top:0; bottom:0; right:0;
    overflow-y:auto;
    padding:30px;
    opacity:0;
    animation: fadeIn .35s forwards;
}
@keyframes fadeIn { from{opacity:0;} to{opacity:1;} }

h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# BOTONES VISUALES (solo imágenes)
# -------------------------------------------------------------------
def img_or_placeholder(data_uri: str):
    if data_uri:
        return f'<img src="{data_uri}" />'
    return '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:#aaa;">img</div>'

st.markdown(f"""
<div id="btn-home"   class="icon-button">{img_or_placeholder(icon_home)}</div>
<div id="btn-craft"  class="icon-button">{img_or_placeholder(icon_craft)}</div>
<div id="btn-mat"    class="icon-button">{img_or_placeholder(icon_mat)}</div>
<div id="btn-spec"   class="icon-button">{img_or_placeholder(icon_spec)}</div>
<div id="btn-config" class="icon-button">{img_or_placeholder(icon_conf)}</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# BOTONES FUNCIONALES CON JS PARA CAMBIAR SUBPÁGINA
# -------------------------------------------------------------------
components.html("""
<script>
(function(){
  function smoothGoto(page){
    const root = window.parent.document.documentElement;
    if(root) root.classList.add('leaving');
    setTimeout(function(){
      window.parent.location.search='?page=' + encodeURIComponent(page);
    },180);
  }
  const map = {
    'btn-home':'Home',
    'btn-craft':'Craft',
    'btn-mat':'Materiales',
    'btn-spec':'Especificaciones',
    'btn-config':'Configuracion'
  };
  Object.keys(map).forEach(function(id){
    const el = window.parent.document.getElementById(id);
    if(el && !el._bound){
      el._bound = true;
      el.addEventListener('click',function(ev){
        ev.preventDefault(); ev.stopPropagation();
        smoothGoto(map[id]);
      });
    }
  });
  setInterval(function(){
    Object.keys(map).forEach(function(id){
      const el = window.parent.document.getElementById(id);
      if(el && !el._bound){
        el._bound = true;
        el.addEventListener('click',function(ev){
          ev.preventDefault(); ev.stopPropagation();
          smoothGoto(map[id]);
        });
      }
    });
  },500);
})();
</script>
""", height=0, width=0)

# -------------------------------------------------------------------
# CONTENIDO DE SUBPÁGINAS
# -------------------------------------------------------------------
pagina = st.session_state.pagina

if pagina=="Home":
    html_home = f"""
    <div id="main-content">
      <div style="
          display:flex; flex-direction:column; justify-content:flex-start; align-items:center;
          height:100%; padding-top:50px;
      ">
        <h1>AstroCycle</h1>
        <img src="{logo_data}" style="width:600px; max-width:85vw; height:auto; filter:drop-shadow(0 0 35px rgba(255,255,255,0.35));"/>
      </div>
    </div>
    """
    st.markdown(html_home, unsafe_allow_html=True)

elif pagina=="Craft":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("🛠️ Craft")
    st.write("Sección de construcción y desarrollo del prototipo.")
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina=="Materiales":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina=="Especificaciones":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif pagina=="Configuracion":
    st.markdown('<div id="main-content">', unsafe_allow_html=True)
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
    st.markdown('</div>', unsafe_allow_html=True)
