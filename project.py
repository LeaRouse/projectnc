import streamlit as st

# --- FONDO ANIMADO CON VIDEO ---
st.markdown("""
<video autoplay loop muted playsinline id="bgvid">
  <source src="video.mp4" type="video/mp4">
</video>

<style>
#bgvid {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
  z-index: -1;
  opacity: 0.8; /* ajusta la transparencia */
  filter: brightness(60%); /* oscurece un poco el fondo */
}
</style>
""", unsafe_allow_html=True)

# --- ESTILO GENERAL ---
st.markdown("""
<style>
body {
    background-color: transparent;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Barra lateral */
.sidebar .sidebar-content {
    background-color: rgba(20,20,20,0.6);
    padding: 10px;
    border-radius: 10px;
}

/* Botones iguales */
button[kind="primary"] {
    background-color: rgba(50,50,50,0.8);
    color: white;
    border: 1px solid #888;
    width: 220px;
    height: 45px;
    margin-bottom: 10px;
    transition: all 0.2s ease-in-out;
}

button[kind="primary"]:hover {
    background-color: rgba(80,80,80,0.9);
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# --- INTERFAZ ---
st.sidebar.title("Menú")
paginas = [
    "Home", 
    "Datos Generales", 
    "Status", 
    "ON / OFF", 
    "Craft", 
    "Historial de Fabricación", 
    "Productos y Modelo 3D", 
    "Fabricación", 
    "Materiales", 
    "Buscador", 
    "Inventario de Materiales", 
    "Especificaciones", 
    "Info del Sistema", 
    "Configuración"
]
pagina = st.sidebar.radio("Selecciona una página:", paginas)

# --- CONTENIDO PRINCIPAL ---
st.title(pagina)
st.write(f"Contenido de **{pagina}** próximamente... 🚀")
