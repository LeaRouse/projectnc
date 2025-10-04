import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #0a0a1a;
    }

    /* Estilo de la barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #111133;
        border-radius: 20px;
        padding-top: 30px;
    }

    /* Título del menú */
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        color: #03dffc;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Botones personalizados */
    div[data-testid="stSidebar"] button {
        background-color: #1a1a3d !important;
        color: #03dffc !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        transition: 0.2s ease-in-out;
    }

    /* Efecto hover */
    div[data-testid="stSidebar"] button:hover {
        background-color: #03dffc !important;
        color: #0a0a1a !important;
        transform: scale(1.03);
    }

    /* Textos principales */
    h1, h2, h3, h4, p {
        color: #03dffc;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL ---
st.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- Lógica del menú (botones) ---
pagina = None
if st.sidebar.button("🏠 Inicio"):
    pagina = "Inicio"
elif st.sidebar.button("🪐 Pantalla 1"):
    pagina = "Pantalla 1"
elif st.sidebar.button("✨ Pantalla 2"):
    pagina = "Pantalla 2"
else:
    pagina = "Inicio"

# --- CONTENIDO SEGÚN LA PÁGINA ---
if pagina == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.write("Explora el universo desde tu pantalla con un diseño moderno y elegante.")
    st.image("https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg", use_container_width=True)

elif pagina == "Pantalla 1":
    st.header("🪐 Pantalla 1")
    st.write("Aquí puedes agregar contenido sobre planetas, órbitas o datos astronómicos.")

elif pagina == "Pantalla 2":
    st.header("✨ Pantalla 2")
    st.write("Espacio para simulaciones, animaciones o datos interactivos del cosmos.")
