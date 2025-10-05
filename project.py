import streamlit as st
import streamlit.components.v1 as components

# --- Configuración de página ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- Estado de página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- Función para cambiar página ---
def cambiar_pagina(pagina):
    st.session_state.pagina = pagina

# --- CSS profesional ---
st.markdown("""
<style>
/* Fondo general */
.stApp { background-color: #0a0a0a !important; color: #d0d0d0 !important; }

/* Navbar global */
.encabezado-global {
    width:100%; background-color:#1a1a1a; color:#d0d0d0;
    padding:12px 20px; font-size:20px; font-weight:bold;
    border-bottom:2px solid #2a2a2a; border-radius:8px 8px 0 0;
    text-align:center; margin-bottom:20px;
}

/* Menú lateral */
.menu-lateral {
    display:flex; flex-direction:column; gap:10px; padding-top:10px;
}

/* Botones uniformes */
.menu-lateral button {
    width: 100%; height: 50px;  /* todos iguales */
    border-radius:10px; border:none;
    font-weight:bold; text-align:left;
    display:flex; align-items:center; padding-left:12px;
    font-size:16px; cursor:pointer; transition:0.2s;
    background-color:#2a2a2a; color:#d0d0d0;
}
.menu-lateral button:hover { background-color:#3a3a3a; color:#ffffff; transform:scale(1.02); }

/* Botón activo */
.menu-lateral .activo { background-color:#555555; color:#ffffff; }

/* Contenido */
.contenido { padding-left:20px; }
</style>
""", unsafe_allow_html=True)

# --- Navbar global ---
st.markdown('<div class="encabezado-global">🌌 AstroCycle - Panel de Control del Robot</div>', unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns([1,5])

# --- Definir páginas e iconos ---
paginas = [
    ("🏠", "Home"),
    ("📊", "Datos Generales"),
    ("🤖", "Status"),
    ("🛠️", "Craft"),
    ("📦", "Materiales"),
    ("⚙️", "Especificaciones"),
    ("🧩", "Configuración")
]

# --- Menú lateral con HTML buttons ---
with col1:
    menu_html = '<div class="menu-lateral">'
    for icono, nombre in paginas:
        clase = "activo" if st.session_state.pagina == nombre else ""
        # Cada botón HTML con onclick para cambiar st.session_state
        menu_html += f"""
        <button class="{clase}" onclick="window.location.href='#{nombre}'">{icono} {nombre}</button>
        """
    menu_html += '</div>'
    st.markdown(menu_html, unsafe_allow_html=True)

    # Capturar clic usando botones invisibles de Streamlit
    for _, nombre in paginas:
        if st.button(f"btn_{nombre}", key=f"btn_{nombre}"):
            cambiar_pagina(nombre)

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
