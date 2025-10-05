import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="AstroCycle", layout="wide")

VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

# --- Configuración visual global ---
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem;}
    </style>
""", unsafe_allow_html=True)

# --- Fondo de video ---
if VIDEO_FILE.exists():
    video_base64 = base64.b64encode(VIDEO_FILE.read_bytes()).decode("utf-8")
    st.markdown(f"""
        <video autoplay loop muted playsinline 
        style="
            position: fixed; 
            right: 0; bottom: 0; 
            min-width: 100%; min-height: 100%; 
            z-index: -1; 
            object-fit: cover;
            filter: brightness(0.35);
        ">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ No se encontró el archivo 'video.mp4'. Colócalo junto a app.py.")

# --- Estado de visibilidad de la barra lateral ---
if "menu_visible" not in st.session_state:
    st.session_state.menu_visible = True

# --- Botón para mostrar/ocultar barra lateral ---
menu_button = st.button("☰ Menú", key="menu_toggle")

if menu_button:
    st.session_state.menu_visible = not st.session_state.menu_visible

# --- Contenido de la barra lateral ---
if st.session_state.menu_visible:
    with st.sidebar:
        st.title("ASTROCYCLE 🚀")
        pagina = st.radio("Navegación", [
            "Inicio",
            "Datos Generales",
            "Status",
            "Fabricación",
            "Especificaciones",
            "Configuración"
        ])
else:
    pagina = st.session_state.get("pagina_actual", "Inicio")

st.session_state.pagina_actual = pagina

# --- Encabezado principal ---
st.markdown("<h1 style='text-align:center; color:white;'>ASTROCYCLE</h1>", unsafe_allow_html=True)

# --- Contenido por página ---
if pagina == "Inicio":
    st.subheader("🌌 Bienvenido a AstroCycle")
    st.markdown("Sistema integral de control y visualización del rover de exploración.")

elif pagina == "Datos Generales":
    st.subheader("📋 Datos Generales")
    st.markdown("- Nombre: **Rover AstroCycle**  \n- Modelo: **v1.0**  \n- Año: 2025")

elif pagina == "Status":
    st.subheader("🧭 Estado del Sistema")
    st.markdown("- Energía: **100%**  \n- Sensores: OK  \n- Comunicación: Activa  \n- Temperatura: Nominal")

elif pagina == "Fabricación":
    st.subheader("⚙️ Proceso de Fabricación")
    st.markdown("1. Ensamblaje de chasis  \n2. Integración de sensores  \n3. Pruebas de campo  \n4. Certificación final")

elif pagina == "Especificaciones":
    st.subheader("🔧 Especificaciones Técnicas")
    if MODEL_FILE.exists():
        with open(MODEL_FILE, "rb") as f:
            glb_b64 = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(f"""
            <model-viewer src="data:model/gltf-binary;base64,{glb_b64}" 
                alt="Modelo 3D del rover" 
                auto-rotate camera-controls 
                style="width:100%; height:600px; background-color: rgba(0,0,0,0.3); border-radius: 15px;">
            </model-viewer>
            <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ No se encontró el archivo 'Rove_prototipo1.glb'. Súbelo a la carpeta del proyecto.")

elif pagina == "Configuración":
    st.subheader("⚙️ Configuración del Sistema")
    st.markdown("Opciones de calibración, conexión y control manual del rover.")
