import streamlit as st

st.set_page_config(page_title="AstroCycle", layout="wide")

# --- CSS personalizado ---
st.markdown("""
<style>
/* Barra lateral */
section[data-testid="stSidebar"] {
    background-color: #11112b; /* barra lateral oscura */
    border-radius: 20px;
    padding: 20px;
}

/* Título del menú */
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
    background-color: #1a1a3f; /* botón ligeramente más claro que barra */
    transition: 0.2s;
    text-align: left;
    cursor: pointer;
}

/* Hover */
.stButton > button:hover {
    background-color: #2a2a55; /* sutil más claro al pasar cursor */
    color: #ffffff;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# --- Título ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- Lógica del menú con botones usando session_state ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Inicio'

def cambiar_pagina(nombre):
    st.session_state.pagina = nombre

# Botones de menú
st.sidebar.button("🏠 Inicio", key="btn_inicio", on_click=cambiar_pagina, args=("Inicio",))
st.sidebar.button("🪐 Pantalla 1", key="btn_1", on_click=cambiar_pagina, args=("Pantalla 1",))
st.sidebar.button("✨ Pantalla 2", key="btn_2", on_click=cambiar_pagina, args=("Pantalla 2",))

# --- Contenido según la página ---
if st.session_state.pagina == "Inicio":
    st.title("🌌 Bienvenido a AstroCycle")
    #st.write("Explora el universo con estilo moderno y elegante.")

elif st.session_state.pagina == "Pantalla 1":
    st.header("🪐 Pantalla 1")
    #st.write("Contenido sobre planetas, órbitas o datos astronómicos.")

elif st.session_state.pagina == "Pantalla 2":
    st.header("✨ Pantalla 2")
    #st.write("Simulaciones o animaciones del cosmos.")

