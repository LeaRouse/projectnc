import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Rover UI", layout="wide")

# --- VIDEO DE FONDO (con suavizado) ---
st.markdown("""
    <style>
    /* Fondo de video animado */
    .video-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -2;
        overflow: hidden;
    }
    .video-background video {
        position: absolute;
        top: 50%;
        left: 50%;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        transform: translate(-50%, -50%);
        object-fit: cover;
        filter: brightness(0.7) contrast(1.05) saturate(1.2);
        image-rendering: auto; /* suavizado */
    }
    /* Capa oscura */
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.55);
        z-index: -1;
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background: rgba(20, 20, 20, 0.6);
        border-radius: 18px;
        padding-top: 30px;
        backdrop-filter: blur(6px);
    }

    /* Botones */
    div[data-testid="stSidebar"] button {
        background-color: rgba(35, 35, 35, 0.7) !important;
        color: #f0f0f0 !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        width: 100% !important;
        height: 45px !important;
        margin-bottom: 10px !important;
        transition: all 0.2s ease-in-out;
    }
    div[data-testid="stSidebar"] button:hover {
        background-color: rgba(80,80,80,0.8) !important;
        transform: scale(1.05);
    }

    /* Textos principales */
    h1, h2, h3, p {
        color: #e6e6e6 !important;
        text-shadow: 0 0 10px rgba(0,0,0,0.4);
    }
    </style>

    <div class="video-background">
        <video autoplay muted loop playsinline>
            <source src="video.mp4" type="video/mp4">
        </video>
    </div>
    <div class="overlay"></div>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("🚀 Rover UI")
pagina = st.sidebar.radio("Navegación", ["Home", "Craft", "Materiales", "Especificaciones", "Configuración"])

# --- CONTENIDO PRINCIPAL ---
if pagina == "Home":
    st.title("🏠 Home")
    st.write("Bienvenido al sistema del Rover. Aquí puedes acceder a toda la información del proyecto.")
elif pagina == "Craft":
    st.title("🛠 Craft")
    st.write("Detalles del ensamblaje, construcción y mantenimiento del Rover.")
elif pagina == "Materiales":
    st.title("⚙ Materiales")
    st.write("Lista de materiales y recursos disponibles para fabricación.")
elif pagina == "Especificaciones":
    st.title("📋 Especificaciones")
    st.write("Características técnicas del sistema, estructura y rendimiento.")
    # Modelo 3D incrustado
    st.markdown("""
        <model-viewer src="prototipo1.glb" alt="Rover 3D Model"
        camera-controls auto-rotate rotation-per-second="30deg"
        style="width:100%;height:600px;background:transparent;"></model-viewer>
        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    """, unsafe_allow_html=True)
elif pagina == "Configuración":
    st.title("⚙ Configuración")
    st.write("Ajustes generales del sistema y calibración del Rover.")
