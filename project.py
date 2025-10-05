import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="AstroCycle", layout="wide")

# --- VIDEO DE FONDO ---
st.markdown("""
    <video autoplay loop muted playsinline id="bgvideo"
        style="
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            object-fit: cover;
        ">
        <source src="video.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# --- ESTILOS ---
st.markdown("""
    <style>
        /* Quitar elementos de Streamlit */
        #MainMenu, header, footer {visibility: hidden;}
        .stApp { background: transparent !important; }

        /* Sidebar siempre visible */
        [data-testid="stSidebar"] {
            background-color: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* Títulos y texto blancos */
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: white !important;
        }

        /* Botones del menú */
        .stRadio > div { gap: 0.5rem; }
        .stRadio label {
            background-color: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 8px 12px;
            transition: 0.3s;
        }
        .stRadio label:hover {
            background-color: rgba(255,255,255,0.3);
            transform: scale(1.03);
        }
        div[role="radiogroup"] > label > div[data-testid="stMarkdownContainer"] > p {
            color: white !important;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR MENU ---
st.sidebar.title("🪐 AstroCycle")
st.sidebar.markdown("### Menú principal")

page = st.sidebar.radio(
    "Navegación",
    ["Inicio", "Simulación", "Control", "Datos", "Acerca de"],
    label_visibility="collapsed"
)

# --- CONTENIDO DE CADA PÁGINA ---
if page == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.markdown("Explora el modelo 3D del prototipo.")
    components.html(
        """
        <model-viewer src="Rove_prototipo1.glb" 
            alt="Rove Prototype"
            auto-rotate 
            camera-controls 
            style="width:100%; height:600px;">
        </model-viewer>
        <script type="module" 
            src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
        </script>
        """,
        height=650,
    )

elif page == "Simulación":
    st.header("🚀 Módulo de Simulación")
    st.write("Aquí irá el entorno de simulación del rover.")

elif page == "Control":
    st.header("🎮 Panel de Control")
    st.write("Interfaz para controlar el prototipo en tiempo real.")

elif page == "Datos":
    st.header("📊 Datos en tiempo real")
    st.write("Visualización de métricas y sensores del rover.")

elif page == "Acerca de":
    st.header("ℹ️ Sobre AstroCycle")
    st.write("Proyecto de exploración robótica desarrollado por el equipo AstroCycle.")

