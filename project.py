import streamlit as st

st.set_page_config(page_title="AstroCycle", layout="wide")

# --- CSS para barra lateral moderna ---
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0e1233, #0a0a1a);
    border-radius: 20px;
    padding: 20px;
}
.sidebar-title {
    font-size: 24px;
    font-weight: bold;
    color: #00eaff;
    text-align: center;
    margin-bottom: 25px;
    text-shadow: 0 0 8px #00eaff;
}
.custom-btn {
    display: block;
    width: 100%;
    margin-bottom: 12px;
    padding: 10px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    color: #e0f7ff;
    background-color: #1a1e4a;
    transition: 0.2s;
    text-align: left;
    cursor: pointer;
}
.custom-btn:hover {
    background-color: #00eaff;
    color: #0a0a1a;
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# --- Título ---
st.sidebar.markdown('<div class="sidebar-title">🌠 AstroCycle</div>', unsafe_allow_html=True)

# --- Lógica del menú con botones ---
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
    st.write("Explora el universo con estilo moderno y elegante.")

elif st.session_state.pagina == "Pantalla 1":
    st.header("🪐 Pantalla 1")
    st.write("Contenido sobre planetas, órbitas o datos astronómicos.")

elif st.session_state.pagina == "Pantalla 2":
    st.header("✨ Pantalla 2")
    st.write("Simulaciones o animaciones del cosmos.")
