# app.py
import streamlit as st
from pathlib import Path
import base64

# ---------- Config ----------
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---------- Archivos esperados ----------
VIDEO_FILE = Path("video.mp4")          # pon tu video aqui
MODEL_FILE = Path("prototipo1.glb")     # pon tu modelo .glb aqui

# ---------- Construir HTML del video (base64 si existe local) ----------
def get_video_html():
    if VIDEO_FILE.exists():
        data = VIDEO_FILE.read_bytes()
        b64 = base64.b64encode(data).decode("utf-8")
        # usamos data URI para asegurar que Streamlit lo muestre tanto local como en deploy
        return f'<video autoplay loop muted playsinline id="bgvid"><source src="data:video/mp4;base64,{b64}" type="video/mp4"></video>'
    else:
        # fallback: no video
        return "<!-- video no encontrado: coloca video.mp4 en la carpeta del proyecto -->"

# ---------- CSS: fondo, overlay, sidebar y "botones" estilo radio ---------- 
st.markdown(
    """
    <style>
    /* ocultar header/mainmenu/footer nativos */
    #MainMenu, header, footer { visibility: hidden; }

    /* video fondo: centrado y cover para evitar "cuadraditos" */
    video#bgvid {
      position: fixed;
      top: 50%;
      left: 50%;
      min-width: 100%;
      min-height: 100%;
      width: auto;
      height: auto;
      transform: translate(-50%, -50%);
      object-fit: cover;            /* evita mosaicos y mantiene aspecto */
      z-index: -2;
      image-rendering: auto;
      filter: brightness(0.65) contrast(1.05) saturate(1.05);
    }

    /* capa overlay para asegurar legibilidad */
    .bg-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.45);
      z-index: -1;
    }

    /* Sidebar: fondo translúcido y blur */
    section[data-testid="stSidebar"] {
      background: rgba(6,6,6,0.35);
      backdrop-filter: blur(6px);
      border-radius: 12px;
      padding-top: 18px;
    }

    /* estilo uniforme para las opciones del radio (simulan botones)
       ocultamos el circulito y forzamos altura/ancho iguales */
    /* esconder el control del radio (círculo) */
    section[data-testid="stSidebar"] [data-baseweb="radio"] > div:first-child { display: none !important; }

    /* etiquetas del radiogroup (cada opción) */
    div[role="radiogroup"] > label {
      display: block;
      width: 100%;
      height: 56px;                 /* altura fija */
      line-height: 56px;            /* centra vertical el texto */
      padding-left: 16px;           /* separa icono/texto del borde */
      margin-bottom: 12px;
      border-radius: 10px;
      box-sizing: border-box;
      background: rgba(255,255,255,0.03); /* muy sutil transparente */
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.06);
      font-weight: 600;
      transition: all 0.14s ease;
    }

    div[role="radiogroup"] > label:hover {
      background: rgba(255,255,255,0.06);
      transform: translateY(-1px);
      cursor: pointer;
    }

    /* opción activa */
    div[role="radiogroup"] > label[aria-checked="true"] {
      background: rgba(255,255,255,0.10) !important;
      box-shadow: 0 6px 18px rgba(0,0,0,0.45);
      border: 1px solid rgba(255,255,255,0.12);
    }

    /* Hacer que el texto en el main sea legible */
    .main-title {
      color: #ffffff;
      text-align: left;
      font-size: 34px;
      margin-top: 6px;
      margin-bottom: 6px;
    }
    .muted {
      color: rgba(230,230,230,0.8);
    }

    /* asegurar botones del sidebar exactamente iguales (para el caso de botones nativos) */
    section[data-testid="stSidebar"] .stButton>button {
      height:56px !important;
      width:100% !important;
      border-radius:10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- insertar video y overlay ----------
st.markdown(get_video_html(), unsafe_allow_html=True)
st.markdown('<div class="bg-overlay"></div>', unsafe_allow_html=True)

# ---------- SIDEBAR (navegación) ----------
st.sidebar.title("🚀 AstroCycle")
st.sidebar.markdown("")

# opciones principales (emoji + etiqueta)
pages = [
    "🏠 Home",
    "📊 Datos Generales",
    "🤖 Status",
    "🛠️ Craft",
    "⚙️ Especificaciones"
]

page = st.sidebar.radio("", pages, index=0)  # radio styled como botones iguales

# optional small button at bottom for Configuración
st.sidebar.markdown("---")
if st.sidebar.button("⚙ Configuración"):
    page = "⚙ Configuración"

# ---------- CONTENIDO POR PÁGINA ----------
# Home
if page == "🏠 Home":
    st.markdown("<div style='padding:8px 18px;'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>AstroCycle</h1>", unsafe_allow_html=True)
    st.markdown("<p class='muted'>Panel de control — visualización y monitoreo del rover.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Datos Generales
elif page == "📊 Datos Generales":
    st.markdown("<h2 class='main-title'>Datos Generales</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Nombre", "Rover Prot1")
        st.metric("Modelo", "X-2025")
    with c2:
        st.metric("Código", "RC-001")
        st.metric("Ubicación", "Hangar A")
    with c3:
        st.metric("Estado", "Operativo")
        st.metric("Última actualización", "2025-10-04")

# Status (robot)
elif page == "🤖 Status":
    st.markdown("<h2 class='main-title'>Status del Robot</h2>", unsafe_allow_html=True)
    # ejemplo de widgets para status
    battery = st.slider("Batería (%)", min_value=0, max_value=100, value=78)
    st.progress(battery)
    st.write("Sensores activos: 5/5")
    st.metric("Conectividad", "Online")
    # ON/OFF rápido
    on_off = st.radio("Encendido / Apagado", ("ON", "OFF"))
    st.write("Modo:", on_off)

# Craft
elif page == "🛠️ Craft":
    st.markdown("<h2 class='main-title'>Craft</h2>", unsafe_allow_html=True)
    st.write("Historial de fabricación, productos y proceso. (a completar)")

# Especificaciones + Modelo 3D
elif page == "⚙️ Especificaciones":
    st.markdown("<h2 class='main-title'>Especificaciones & Modelo 3D</h2>", unsafe_allow_html=True)
    st.write("Detalles técnicos y vista 3D interactiva del prototipo.")
    # Si el archivo .glb existe local, model-viewer lo cargará; si no, mostramos aviso.
    if MODEL_FILE.exists():
        st.markdown(
            """
            <model-viewer src="prototipo1.glb" alt="Rover 3D Model"
                camera-controls auto-rotate exposure="1"
                style="width:100%; height:600px; background: transparent;">
            </model-viewer>
            <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("No se encontró 'prototipo1.glb' en la carpeta. Súbelo al repo junto a este script.")

# Configuración (si fue pulsado)
elif page == "⚙ Configuración":
    st.markdown("<h2 class='main-title'>Configuración</h2>", unsafe_allow_html=True)
    st.write("Ajustes del sistema (a completar).")

# ---------- NOTAS y AYUDA RÁPIDA ----------
st.markdown(
    """
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(255,255,255,0.7); font-size:12px;">
        Tips: sube <b>video.mp4</b> y <b>prototipo1.glb</b> al mismo directorio y haz commit & push si usas Streamlit Cloud.
    </div>
    """,
    unsafe_allow_html=True,
)
