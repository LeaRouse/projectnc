import streamlit as st
import streamlit.components.v1 as components

# --- Configuración de la página ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- Estado de página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- Función para cambiar página ---
def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- CSS ---
st.markdown("""
<style>
.stApp { background-color: #0a0a0a !important; color: #d0d0d0 !important; }

.encabezado-global {
    width:100%; background-color:#1a1a1a; color:#d0d0d0;
    padding:12px 20px; font-size:20px; font-weight:bold;
    border-bottom:2px solid #2a2a2a; border-radius:8px 8px 0 0;
    text-align:center; margin-bottom:20px;
}

.menu-lateral {
    display:flex; flex-direction:column; gap:10px; padding-top:10px; height:100%;
}

.menu-lateral button {
    width: 100%; height: 50px; border-radius:10px; border:none;
    font-weight:bold; text-align:left; display:flex; align-items:center;
    padding-left:12px; font-size:16px; cursor:pointer; transition:0.2s;
    background-color:#2a2a2a; color:#d0d0d0;
}

.menu-lateral button:hover { background-color:#3a3a3a; color:#ffffff; transform:scale(1.02); }

.menu-lateral .activo { background-color:#555555; color:#ffffff; }

.menu-lateral .bottom { margin-top:auto; }

.contenido { padding-left:20px; }
</style>
""", unsafe_allow_html=True)

# --- Navbar global ---
st.markdown('<div class="encabezado-global">🌌 AstroCycle - Panel de Control del Robot</div>', unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns([1,5])

# --- Menú lateral ---
paginas_arriba = [
    ("🏠", "Home"),
    ("📊", "Datos Generales"),
    ("🤖", "Status"),
    ("🛠️", "Craft"),
    ("📦", "Materiales")
]

paginas_abajo = [
    ("⚙️", "Especificaciones"),
    ("🧩", "Configuración")
]

with col1:
    st.markdown('<div class="menu-lateral">', unsafe_allow_html=True)

    # Botones de arriba
    for icono, nombre in paginas_arriba:
        clase = "activo" if st.session_state.pagina == nombre else ""
        if st.button(f"{icono} {nombre}", key=nombre):
            cambiar_pagina(nombre)
        st.markdown(f"""
            <style>
            div.stButton > button[key="{nombre}"] {{ background-color:{'#555555' if clase=='activo' else '#2a2a2a'} !important; }}
            </style>
        """, unsafe_allow_html=True)

    # Separar los botones de abajo
    st.markdown('<div class="bottom"></div>', unsafe_allow_html=True)

    # Botones de abajo
    for icono, nombre in paginas_abajo:
        clase = "activo" if st.session_state.pagina == nombre else ""
        if st.button(f"{icono} {nombre}", key=nombre):
            cambiar_pagina(nombre)
        st.markdown(f"""
            <style>
            div.stButton > button[key="{nombre}"] {{ background-color:{'#555555' if clase=='activo' else '#2a2a2a'} !important; }}
            </style>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- Contenido ---
with col2:
    if st.session_state.pagina == "Home":
        st.header("🏠 Home")
    elif st.session_state.pagina == "Datos Generales":
        st.header("📊 Datos Generales")
    elif st.session_state.pagina == "Status":
        st.header("🤖 Status del Robot")
    elif st.session_state.pagina == "Craft":
        st.header("🛠️ Craft")
    elif st.session_state.pagina == "Materiales":
        st.header("📦 Materiales")
    elif st.session_state.pagina == "Especificaciones":
        st.header("⚙️ Especificaciones")
        st.write("Modelo 3D del prototipo:")
        viewer_url = "https://learouse.github.io/prototipo/"
        components.iframe(viewer_url, height=600, width="100%", scrolling=True)
    elif st.session_state.pagina == "Configuración":
        st.header("🧩 Configuración")
