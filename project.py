import streamlit as st
import streamlit.components.v1 as components

# ---- CONFIGURACIÓN GENERAL ----
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---- VIDEO DE FONDO ----
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

# ---- ESTILOS ----
st.markdown("""
    <style>
        /* Ocultar header y footer */
        #MainMenu, header, footer {visibility: hidden;}
        .stApp { background: transparent !important; }

        /* Barra lateral SIEMPRE visible */
        section[data-testid="stSidebar"] {
            background-color: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255,255,255,0.2);
        }

        /* Títulos y texto blancos */
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: white !important;
        }

        /* Botones iguales */
        div[data-testid="stSidebar"] button {
            width: 100% !important;
            height: 45px !important;
            background-color: rgba(255,255,255,0.1);
            border-radius: 8px;
            border: none;
            margin-bottom: 10px;
            transition: all 0.3s ease;
            color: white;
            font-weight: 600;
        }
        div[data-testid="stSidebar"] button:hover {
            background-color: rgba(255,255,255,0.3);
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR MENÚ ----
st.sidebar.title("🪐 ASTROCYCLE")
st.sidebar.markdown("---")

# Botones con el mismo tamaño y comportamiento
page = st.sidebar.selectbox(
    "Menú principal",
    ["Inicio", "Simulación", "Control", "Datos", "Acerca de"],
    index=0
)

# ---- CONTENIDO PRINCIPAL ----
if page == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.markdown("Explora el prototipo 3D del rover.")

    # Modelo 3D
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
    st.header("🚀 Simulación del Rover")
    st.write("Aquí podrás ejecutar la simulación virtual del rover.")

elif page == "Control":
    st.header("🎮 Control del Rover")
    st.write("Panel para interactuar con el prototipo en tiempo real.")

elif page == "Datos":
    st.header("📊 Datos del Sistema")
    st.write("Visualización de sensores, temperatura, energía y otros datos del rover.")

elif page == "Acerca de":
    st.header("ℹ️ Proyecto AstroCycle")
    st.write("""
    AstroCycle es un sistema experimental para exploración planetaria y reciclaje automatizado.
    Desarrollado con fines educativos y de investigación.
    """)

