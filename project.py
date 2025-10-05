import streamlit as st
import streamlit.components.v1 as components

# --- Configuración de página ---
st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide"
)

# --- CSS para botones y layout ---
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background-color: #0a0a0a !important;
    color: #d0d0d0 !important;
}

/* Navbar global */
.encabezado-global {
    width: 100%;
    background-color: #1a1a1a;
    color: #d0d0d0;
    padding: 12px 20px;
    font-size: 20px;
    font-weight: bold;
    border-bottom: 2px solid #2a2a2a;
    border-radius: 8px 8px 0 0;
    text-align: center;
    margin-bottom: 20px;
}

/* Menú lateral: todos los botones iguales */
.menu-lateral button {
    width: 100% !important;       /* mismo ancho */
    height: 50px !important;      /* misma altura */
    margin-bottom: 10px !important; 
    border-radius: 10px !important;
    border: none !important;
    background-color: #2a2a2a !important;
    color: #d0d0d0 !important;
    font-weight: bold !important;
    text-align: left !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    cursor: pointer !important;
    transition: 0.2s !important;
}
.menu-lateral button:hover {
    background-color: #3a3a3a !important;
    color: #ffffff !important;
    transform: scale(1.02) !important;
}

/* Contenido */
.contenido {
    padding-left: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Navbar global ---
st.markdown('<div class="encabezado-global">🌌 AstroCycle - Panel de Control del Robot</div>', unsafe_allow_html=True)

# --- Estado de página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- Layout: columnas (menú | contenido) ---
col1, col2 = st.columns([1,5])

# --- Menú lateral con botones funcionales ---
with col1:
    st.markdown('<div class="menu-lateral">', unsafe_allow_html=True)
    if st.button("🏠 Home"): cambiar_pagina("Home")
    if st.button("📊 Datos Generales"): cambiar_pagina("Datos Generales")
    if st.button("🤖 Status"): cambiar_pagina("Status")
    if st.button("🛠️ Craft"): cambiar_pagina("Craft")
    if st.button("📦 Materiales"): cambiar_pagina("Materiales")
    if st.button("⚙️ Especificaciones"): cambiar_pagina("Especificaciones")
    if st.button("🧩 Configuración"): cambiar_pagina("Configuracion")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Contenido ---
with col2:
    if st.session_state.pagina == "Home":
        st.header("🏠 Home")
        st.write("")

    elif st.session_state.pagina == "Datos Generales":
        st.header("📊 Datos Generales")
        st.write("")

    elif st.session_state.pagina == "Status":
        st.header("🤖 Status del Robot")
        st.write("")

    elif st.session_state.pagina == "Craft":
        st.header("🛠️ Craft")
        st.write("")

    elif st.session_state.pagina == "Materiales":
        st.header("📦 Materiales")
        st.write("")

    elif st.session_state.pagina == "Especificaciones":
        st.header("⚙️ Especificaciones")
        st.write("Modelo 3D del prototipo:")
        viewer_url = "https://learouse.github.io/prototipo/"
        components.iframe(viewer_url, height=600, width="100%", scrolling=True)

    elif st.session_state.pagina == "Configuracion":
        st.header("🧩 Configuración")
        st.write("")
