import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🌠",
    page_icon="🪐",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo con degradado espacial */
    .stApp {
        background: radial-gradient(circle at top left, #090b1a, #04030c 70%);
        color: #dbe4ff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar moderna */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #12132b 0%, #0b0c1d 100%);
        border-right: 2px solid #26284a;
        border-radius: 0 20px 20px 0;
        padding-top: 40px;
        box-shadow: 0 0 15px rgba(0,0,0,0.4);
    }

    /* Título del menú */
    .sidebar-title {
        font-size: 25px;
        font-weight: bold;
        color: #8be9fd;
        text-align: center;
        margin-bottom: 25px;
        text-shadow: 0 0 8px #00fff2;
    }

    /* Botones personalizados */
    div[data-testid="stSidebar"] button {
        background: linear-gradient(90deg, #232651 0%, #1b1e3a 100%) !important;
        color: #b8cfff !important;
        border: 1px solid #30345c !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: bold !important;
        margin: 5px 0 12px 0 !important;
        width: 100% !important;
        transition: all 0.25s ease-in-out;
    }

    /* Hover con brillo */
    div[data-testid="stSidebar"] button:hover {
        background: linear-gradient(90deg, #3a46b0, #1b6dc1) !important;
        color: white !important;
        box-shadow: 0 0 12px #1b6dc1 !important;
        transform: scale(1.04);
    }

    /* Títulos principales */
    h1, h2, h3, h4, h5, h6 {
        color: #9fc9ff !important;
        text-shadow: 0 0 10px rgba(31, 92, 255, 0.5);
    }

    p {
        color: #d7e2ff !important;
        font-size: 16px;
    }

    /* Imagen centrada con sombra */
    .stImage > img {
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(0, 153, 255, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- Lógica de navegación ---
pagina = None
if st.sidebar.button("🏠 Inicio"):
    pagina = "Inicio"
elif st.sidebar.button("🪐 Sistema Solar"):
    pagina = "Sistema Solar"
elif st.sidebar.button("✨ Galaxias"):
    pagina = "Galaxias"
else:
    pagina = "Inicio"

# --- CONTENIDO ---
if pagina == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.write("Explora el universo con una interfaz limpia, moderna y llena de energía cósmica 💫.")
    st.image(
        "https://cdn.spacetelescope.org/archives/images/wallpaper2/heic1509a.jpg",
        use_container_width=True
    )

elif pagina == "Sistema Solar":
    st.header("🪐 El Sistema Solar")
    st.write("Descubre los planetas, sus lunas y las maravillas que orbitan nuestra estrella más cercana.")
    st.image(
        "https://cdn.mos.cms.futurecdn.net/LWeQrhMqQ3eQrLKjL4UKhR-1200-80.jpg",
        use_container_width=True
