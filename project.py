import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AstroCycle 🌌",
    page_icon="🪐",
    layout="wide"
)

# --- CSS PERSONALIZADO ---
st.markdown("""
<style>
/* Barra lateral */
section[data-testid="stSidebar"] {
    background-color: #11112b;
    border-radius: 20px;
    padding: 20px;
    position: relative;
    height: 100vh;
}

/* Título lateral */
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #99ccff;
    text-align: center;
    margin-bottom: 25px;
}

/* Botones del menú */
.stButton > button {
    display: block;
    width: 100%;
    margin-bottom: 12px;
    padding: 10px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    color: #d0e7ff;
    background-color: #1a1a3f;
    transition: 0.2s;
    text-align: left;
    cursor: pointer;
}

/* Hover */
.stButton > button:hover {
    background-color: #2a2a55;
    color: #ffffff;
    transform: scale(1.02);
}

/* Botones abajo con espacio extra */
.sidebar-footer {
    position: absolute;
    bottom: 120px;  /* ajusta este valor para mover más abajo o arriba */
    left: 20px;
    right: 20px;
}

/* Títulos y textos principales */
h1, h2, h3, h4, p, span {
    color: #d0e7ff;
}
</style>
""", unsafe_allow_html=True)

# --- TÍTULO DEL MENÚ ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Home'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

# --- Secciones principales arriba ---
st.sidebar.button("🏠 Home", on_click=cambiar_pagina, args=("Home",))
st.sidebar.button("🛠️ Craft", on_click=cambiar_pagina, args=("Craft",))
st.sidebar.button("📦 Materiales", on_click=cambiar_pagina, args=("Materiales",))

# --- Secciones de abajo ---
st.sidebar.markdown('<div class="sidebar-footer">', unsafe_allow_html=True)
st.sidebar.button("⚙️ Especificaciones", on_click=cambiar_pagina, args=("Especificaciones",))
st.sidebar.button("🧩 Configuración", on_click=cambiar_pagina, args=("Configuracion",))
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# --- CONTENIDO ---
if st.session_state.pagina == "Home":
    st.title("🏠 Home")
    st.write("Bienvenido a AstroCycle. Explora todo desde aquí.")
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg",
        use_container_width=True
    )

elif st.session_state.pagina == "Craft":
    st.header("🛠️ Craft")
    st.write("Contenido relacionado a la construcción y fabricación.")

elif st.session_state.pagina == "Materiales":
    st.header("📦 Materiales")
    st.write("Aquí se muestran los materiales utilizados y sus detalles.")

elif st.session_state.pagina == "Especificaciones":
    st.header("⚙️ Especificaciones")
    st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)

elif st.session_state.pagina == "Configuracion":
    st.header("🧩 Configuración")
    st.write("Opciones de configuración de la app.")
