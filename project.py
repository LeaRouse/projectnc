import streamlit as st
import streamlit.components.v1 as components

# Configuración general
st.set_page_config(page_title="AstroCycle", layout="wide")

# --- VIDEO DE FONDO ---
background_video = """
    <video autoplay loop muted playsinline 
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
"""
st.markdown(background_video, unsafe_allow_html=True)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
        /* Oculta la barra superior de Streamlit */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Fondo de las secciones y transparencia */
        .stApp {
            background: transparent !important;
        }

        /* Sidebar (barra lateral) */
        section[data-testid="stSidebar"] {
            background-color: rgba(0, 0, 0, 0.65) !important;
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255,255,255,0.2);
        }

        /* Botones */
        button {
            width: 100%;
            margin-bottom: 0.6rem;
            background: rgba(255,255,255,0.1);
            color: white;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease;
        }
        button:hover {
            background: rgba(255,255,255,0.25);
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTENIDO DE LA BARRA LATERAL ---
st.sidebar.title("🪐 AstroCycle")
st.sidebar.markdown("### Navegación")

# Lista de páginas
pages = {
    "Inicio": "inicio",
    "Simulación": "simulacion",
    "Control": "control",
    "Datos": "datos",
    "Acerca de": "acerca"
}

page = st.sidebar.radio("Ir a:", list(pages.keys()))

# --- PÁGINAS ---
if page == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.markdown("Explora el modelo 3D del prototipo.")
    components.html(
        f"""
        <model-viewer 
            src="Rove_prototipo1.glb" 
            alt="Rove Prototype" 
            camera-controls 
            auto-rotate 
            style="width: 100%; height: 600px;">
        </model-viewer>
        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
        """,
        height=650,
    )

elif page == "Simulación":
    st.header("🚀 Módulo de Simulación")
    st.write("Aquí irá el entorno de simulación del rover.")

elif page == "Control":
    st.header("🎮 Panel de Control")
    st.write("Interfaz para controlar el prototipo.")

elif page == "Datos":
    st.header("📊 Datos en tiempo real")
    st.write("Visualización de métricas y sensores.")

elif page == "Acerca de":
    st.header("ℹ️ Acerca de AstroCycle")
    st.write("Proyecto de exploración robótica — prototipo Rove.")

