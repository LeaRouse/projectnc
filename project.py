import streamlit as st
from pathlib import Path
import base64

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="AstroCycle", layout="wide")

VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

# --- VIDEO DE FONDO (se carga una sola vez) ---
if "video_bg" not in st.session_state:
    if VIDEO_FILE.exists():
        video_base64 = base64.b64encode(VIDEO_FILE.read_bytes()).decode("utf-8")
        st.session_state.video_bg = f"""
            <video autoplay loop muted playsinline 
                style="
                    position: fixed; 
                    right: 0; bottom: 0; 
                    min-width: 100%; min-height: 100%;
                    z-index: -1;
                    object-fit: cover;
                    filter: brightness(0.35);
                    background-color: #000;
                ">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        """
    else:
        st.session_state.video_bg = """
            <div style="position: fixed; right:0; bottom:0; 
                width:100%; height:100%; background:black; z-index:-1;"></div>
        """

st.markdown(st.session_state.video_bg, unsafe_allow_html=True)

# --- ESTILOS GENERALES ---
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem;}

    /* Fondo general oscuro */
    .stApp {
        background-color: rgba(0,0,0,0.9);
    }

    /* Sidebar fija */
    section[data-testid="stSidebar"] {
        background-color: rgba(20, 20, 30, 0.9);
        border-right: 1px solid rgba(100,100,120,0.3);
        padding-top: 40px;
        width: 240px;
    }

    /* Botones del menú */
    div[data-testid="stSidebar"] .stRadio > label {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    div[data-testid="stSidebar"] div[role="radio"] {
        background-color: rgba(50,50,70,0.7);
        color: white;
        border-radius: 10px;
        text-align: center;
        padding: 10px 0;
        font-weight: 600;
        width: 100%;
        transition: 0.2s;
    }

    div[data-testid="stSidebar"] div[role="radio"]:hover {
        background-color: rgba(70,70,100,0.9);
        transform: scale(1.03);
    }

    div[data-testid="stSidebar"] div[aria-checked="true"] {
        background-color: rgba(100,100,130,1);
        color: #00d0ff;
    }

    h1, h2, h3, h4, p, li {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("🚀 ASTROCYCLE")
pagina = st.sidebar.radio(
    "Navegación",
    ["Inicio", "Datos Generales", "Status", "Fabricación", "Especificaciones", "Configuración"],
    index=0
)

# --- CONTENIDO PRINCIPAL ---
st.markdown("<h1 style='text-align:center; color:white;'>ASTROCYCLE</h1>", unsafe_allow_html=True)

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
        st.error("❌ No se encontró el archivo 'Rove_prototipo1.glb'.")

elif pagina == "Configuración":
    st.subheader("⚙️ Configuración del Sistema")
    st.markdown("Opciones de calibración, conexión y control manual del rover.")
