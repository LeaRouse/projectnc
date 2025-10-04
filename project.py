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
        background-color: #090a1a;
        color: #e0f7ff;
    }

    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #0e1233;
        border-radius: 20px;
        padding-top: 25px;
        padding-left: 10px;
        padding-right: 10px;
        box-shadow: 0 0 15px rgba(0,0,0,0.4);
    }

    /* Título del menú */
    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        color: #00eaff;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Botones del menú */
    div[data-testid="stSidebar"] button {
        background-color: #1a1e4a !important;
        color: #e0f7ff !important;
        border: 1px solid #00eaff !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        transition: all 0.3s ease-in-out;
    }

    /* Hover */
    div[data-testid="stSidebar"] button:hover {
        background-color: #00eaff !important;
        color: #0a0a1a !important;
        transform: scale(1.05);
    }

    /* Títulos principales */
    h1, h2, h3, h4 {
        color: #00eaff;
    }

    /* Texto general */
    p, span {
        color: #e0f7ff;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ LATERAL FIJO (usando radio) ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

pagina = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "🪐 Pantalla 1", "✨ Pantalla 2"],
    label_visibility="collapsed"
)

# --- CONTENIDO SEGÚN LA PÁGINA ---
if pagina == "🏠 Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.write("Explora el universo desde tu pantalla con un diseño moderno y elegante.")
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg",
        use_container_width=True
    )

elif pagina == "🪐 Pantalla 1":
    st.header("🪐 Planetas y Órbitas")
    st.write("Aquí puedes agregar contenido sobre planetas, órbitas o datos astronómicos.")

elif pagina == "✨ Pantalla 2":
    st.header("✨ Simulaciones y Datos Interactivos")
    st.write("Espacio para animaciones o datos del cosmos.")
