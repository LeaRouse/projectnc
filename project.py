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

# --- CSS para dashboard ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
                url("https://cdn.pixabay.com/photo/2020/04/10/11/32/galaxy-5020955_1280.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #d0d0d0;
}

/* Menú lateral */
.menu-lateral {
    display:flex; flex-direction:column; gap:12px; padding:15px; height:100%;
}

/* Botones uniformes tipo dashboard */
.menu-lateral button {
    width: 100%; height: 55px; border-radius:12px; border:none;
    font-weight:bold; display:flex; align-items:center;
    padding-left:16px; font-size:16px; cursor:pointer;
    background-color:#2a2a2a; color:#d0d0d0; transition:0.2s;
}

.menu-lateral button:hover {
    background-color:#3a3a3a; color:#ffffff; transform:scale(1.02);
}

.menu-lateral .activo {
    background-color:#555555; color:#ffffff;
}

/* Separa los botones de abajo */
.menu-lateral .bottom { margin-top:auto; }

/* Iconos alineados */
.menu-lateral span.icono {
    margin-right: 10px; font-size:18px;
}

/* Contenido */
.contenido { padding-left:20px; }
</style>
""", unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns([1,5])

# --- Definir páginas e iconos ---
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

# --- Menú lateral ---
with col1:
    st.markdown('<div class="menu-lateral">', unsafe_allow_html=True)

    # Botones de arriba
    for icono, nombre in paginas_arriba:
        clase = "activo" if st.session_state.pagina == nombre else ""
        if st.button(f"{nombre}", key=nombre):
            cambiar_pagina(nombre)
        st.markdown(f"""
            <style>
            div.stButton > button[key="{nombre}"] {{
                background-color:{'#555555' if clase=='activo' else '#2a2a2a'} !important;
            }}
            div.stButton > button[key="{nombre}"]::before {{
                content: '{icono}'; margin-right:10px;
            }}
            </style>
        """, unsafe_allow_html=True)

    # Separar los botones de abajo
    st.markdown('<div class="bottom"></div>', unsafe_allow_html=True)

    # Botones de abajo
    for icono, nombre in paginas_abajo:
        clase = "activo" if st.session_state.pagina == nombre else ""
        if st.button(f"{nombre}", key=nombre):
            cambiar_pagina(nombre)
        st.markdown(f"""
            <style>
            div.stButton > button[key="{nombre}"] {{
                background-color:{'#555555' if clase=='activo' else '#2a2a2a'} !important;
            }}
            div.stButton > button[key="{nombre}"]::before {{
                content: '{icono}'; margin-right:10px;
            }}
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
