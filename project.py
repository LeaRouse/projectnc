import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🚀",
    page_icon="🪐",
    layout="wide"
)

# --- VIDEO DE FONDO (SE REPITE SIEMPRE) ---
st.markdown("""
    <video autoplay loop muted playsinline id="bgvideo"
        style="
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
            z-index: -1;
        ">
        <source src="video.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
        /* Quitar barra superior y footer de Streamlit */
        header, footer {visibility: hidden;}

        /* Fondo oscuro semitransparente para contenido */
        .main {
            background: rgba(10, 10, 15, 0.65);
            border-radius: 15px;
            padding: 20px;
        }

        /* Estilo de la barra lateral */
        section[data-testid="stSidebar"] {
            background-color: rgba(15, 15, 25, 0.85);
            border-radius: 15px;
            color: #eee;
            padding-top: 30px;
        }

        /* Botones del menú */
        div[data-testid="stSidebar"] button {
            background-color: #222 !important;
            color: #ccc !important;
            border-radius: 10px !important;
            border: none !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            margin-bottom: 10px !important;
            width: 100% !important;
            transition: 0.2s ease-in-out;
        }

        /* Hover */
        div[data-testid="stSidebar"] button:hover {
            background-color: #03dffc !important;
            color: #000 !important;
            transform: scale(1.02);
        }

        /* Títulos y texto */
        h1, h2, h3, h4, p {
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.title("🪐 AstroCycle")
menu = st.sidebar.radio("Navegación", [
    "🏠 Home",
    "⚙️ Configuración",
    "📊 Especificaciones",
    "🧰 Craft",
    "🧩 Materiales"
])

# --- CONTENIDO PRINCIPAL ---
if menu == "🏠 Home":
    st.title("🚀 AstroCycle: Rover Prototype")
    st.write("Explora el modelo 3D interactivo de tu prototipo directamente aquí:")

    # VISOR 3D (usando Google Model Viewer)
    components.html(f"""
        <model-viewer 
            src="prototipo1.glb" 
            alt="Rover Prototype" 
            camera-controls 
            auto-rotate 
            shadow-intensity="1"
            style="width:100%; height:600px; background-color: transparent;">
        </model-viewer>

        <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    """, height=600)

elif menu == "⚙️ Configuración":
    st.header("⚙️ Configuración del Sistema")
    st.write("Aquí podrás ajustar parámetros del rover, calibrar sensores o definir rutinas automáticas.")

elif menu == "📊 Especificaciones":
    st.header("📊 Especificaciones Técnicas")
    st.write("Esta sección mostrará la información técnica y componentes clave del sistema AstroCycle.")

elif menu == "🧰 Craft":
    st.header("🧰 Proceso de Fabricación")
    st.write("En esta sección puedes revisar el historial de construcción, ensamblaje y mantenimiento del rover.")

elif menu == "🧩 Materiales":
    st.header("🧩 Materiales del Rover")
    st.write("Aquí se listan los materiales y recursos usados para fabricar y mantener el prototipo.")
