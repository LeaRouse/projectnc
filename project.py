import streamlit as st
import streamlit.components.v1 as components  # Para iframe del modelo 3D

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
    st.session_state.pagina = 'Inicio'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

# Botones del menú
st.sidebar.button("🏠 Inicio", on_click=cambiar_pagina, args=("Inicio",))
st.sidebar.button("🪐 Sistema Solar", on_click=cambiar_pagina, args=("Sistema Solar",))
st.sidebar.button("✨ Modelo 3D", on_click=cambiar_pagina, args=("Modelo 3D",))

# --- CONTENIDO SEGÚN LA PÁGINA ---
if st.session_state.pagina == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    st.write("Explora el universo con estilo moderno y elegante.")
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg",
        use_container_width=True
    )

elif st.session_state.pagina == "Sistema Solar":
    st.header("🪐 Sistema Solar")
    st.write("Aquí puedes agregar contenido sobre planetas, órbitas o datos astronómicos.")

elif st.session_state.pagina == "Modelo 3D":
    st.header("✨ Rover Prototipo 3D")
    st.write("Puedes rotar, hacer zoom y explorar el modelo 3D interactivo.")

    # --- Inserta el modelo .glb usando iframe desde GitHub Pages ---
    viewer_url = "https://learouse.github.io/prototipo/"
    components.iframe(viewer_url, height=600, width="100%", scrolling=True)
