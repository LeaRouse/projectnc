# --- util: cargar PNG como data URI ---
from mimetypes import guess_type

@st.cache_data
def img_data_uri(path_str: str) -> str:
    p = Path(path_str)
    if not p.exists():
        return ""  # para poder avisar después
    mime, _ = guess_type(p.name)
    if not mime:
        mime = "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

icon_home  = img_data_uri("home.png")
icon_craft = img_data_uri("craft.png")
icon_mat   = img_data_uri("materiales.png")
icon_spec  = img_data_uri("especificaciones.png")
icon_conf  = img_data_uri("config.png")

# --- BOTONES FLOTANTES CON IMÁGENES (embebidas) ---
st.markdown(f"""
<div>
  <div class="icon-button" id="btn-home">
    <img src="{icon_home or ''}" alt="Home">
  </div>
  <div class="icon-button" id="btn-craft">
    <img src="{icon_craft or ''}" alt="Craft">
  </div>
  <div class="icon-button" id="btn-mat">
    <img src="{icon_mat or ''}" alt="Materiales">
  </div>
  <div class="icon-button" id="btn-spec">
    <img src="{icon_spec or ''}" alt="Especificaciones">
  </div>
  <div class="icon-button" id="btn-config">
    <img src="{icon_conf or ''}" alt="Configuración">
  </div>
</div>
""", unsafe_allow_html=True)

# Avisos si falta algún archivo
missing = []
if not icon_home:  missing.append("home.png")
if not icon_craft: missing.append("craft.png")
if not icon_mat:   missing.append("materiales.png")
if not icon_spec:  missing.append("especificaciones.png")
if not icon_conf:  missing.append("config.png")
if missing:
    st.warning("No se encontraron: " + ", ".join(missing))
