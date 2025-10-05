import streamlit as st
import streamlit.components.v1 as components

# --- Configuración ---
st.set_page_config(page_title="AstroCycle 🌌", page_icon="🪐", layout="wide")

# --- Estado de página ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# --- CSS profesional ---
st.markdown("""
<style>
.stApp { background-color: #0a0a0a !important; color: #d0d0d0 !important; }

/* Navbar global */
.encabezado-global {
    width:100%; background-color:#1a1a1a; color:#d0d0d0;
    padding:12px 20px; font-size:20px; font-weight:bold;
    border-bottom:2px solid #2a2a2a; border-radius:8px 8px 0 0;
    text-align:center; margin-bottom:20px;
}

/* Menú lateral */
.menu-lateral { display:flex; flex-direction:column; gap:10px; padding-top:10px; }

/* Botones uniformes */
.menu-lateral button {
    width: 100% !important; height: 50px !important;
    border-radius:10px !important; border:none !important;
    font-weight:bold !important; text-align:left !important;
    display:flex !important; align-items:center !important;
    padding-left:12px !important; font-size:16px !important; cursor:pointer !important;
    transition:0.2s !important; background-color:#2a2a2a !important; color:#d0d0d0 !important;
}
.menu-lateral button:hover { background-color:#3a3a3a !important; color:#ffffff !important; transform:scale(1.02); }

/* Botón activo */
.menu-lateral .activo { background-color:#555555 !important; color:#ffffff !important; }

/* Iconos */
.menu-lateral i { margin-right: 8px; }

/* Contenido */
.contenido { padding-left:20px; }
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown('<div class="encabezado-global">🌌 AstroCycle - Panel de Control del Robot</div>', unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns([1,5])

# --- Definir páginas y iconos ---
paginas = [
    ("🏠", "Home", "Home"),
    ("📊", "Datos Generales", "Datos Generales"),
    ("🤖", "Status", "Status"),
    ("🛠️", "Craft", "Craft"),
    ("📦", "Materiales", "Materiales"),
    ("⚙️", "Especificaciones", "Especificaciones"),
    ("🧩", "Configuración", "Configuracion")
]

# --- Menú lateral ---
with col1:
    st.markdown('<div class="menu-lateral">', unsafe_allow_html=True)
    for icono, nombre, valor in paginas:
        clase = "activo" if st.session_state.pagina == valor else ""
        if st.button(f"{icono} {nombre}", key=valor):
            st.session_state.pagina = valor
        st.markdown(f"""
            <style>
            div.stButton > button[key="{valor}"] {{ background-color:{'#555555' if clase=='activo' else '#2a2a2a'} !important; }}
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
    elif st.session_state.pagina == "Configuracion":
        st.header("🧩 Configuración")
