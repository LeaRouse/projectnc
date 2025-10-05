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
/* Fondo general de la app */
.stApp {
    background-color: #0a0a0a !important;
    color: #d0d0d0 !important;
}

/* Encabezado global */
.encabezado-global {
    width: 100%;
    background-color: #1a1a1a;
    color: #d0d0d0;
    padding: 15px 20px;
    font-size: 20px;
    font-weight: bold;
    border-bottom: 2px solid #2a2a2a;
    border-radius: 8px 8px 0 0;
    text-align: center;
}

/* Contenedor principal que abarca menu + contenido */
.contenedor-principal {
    display: flex;
    flex-direction: row;
    width: 100%;
    margin-top: 10px;
}

/* Menu lateral custom */
.menu-lateral {
    background-color: #1c1c1c;
    border-radius: 10px;
    width: 220px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Botones del menú */
.menu-lateral button {
    padding: 12px;
    border-radius: 10px;
    border: none;
    background-color: #2a2a2a;
    color: #d0d0d0;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
    text-align: left;
}

.menu-lateral button:hover {
    background-color: #3a3a3a;
    color: #ffffff;
    transform: scale(1.02);
}

/* Contenedor de contenido */
.contenido {
    flex-grow: 1;
    background-color: #0f0f0f;
    border-radius: 10px;
    padding: 20px;
    margin-left: 15px;
}
</style>
""", unsafe_allow_html=True)

# --- Encabezado global ---
st.markdown('<div class="encabezado-global">🌌 AstroCycle - Panel de Control del Robot</div>', unsafe_allow_html=True)

# --- Contenedor principal: menú lateral + contenido ---
menu_container = st.container()
with menu_container:
    st.markdown('<div class="contenedor-principal">', unsafe_allow_html=True)

    # --- Menu lateral ---
    menu_html = """
    <div class="menu-lateral">
        <button onclick="window.location.href='#home'">🏠 Home</button>
        <button onclick="window.location.href='#datos'">📊 Datos Generales</button>
        <button onclick="window.location.href='#status'">🤖 Status</button>
        <button onclick="window.location.href='#craft'">🛠️ Craft</button>
        <button onclick="window.location.href='#materiales'">📦 Materiales</button>
        <button onclick="window.location.href='#especificaciones'">⚙️ Especificaciones</button>
        <button onclick="window.location.href='#configuracion'">🧩 Configuración</button>
    </div>
    """
    st.markdown(menu_html, unsafe_allow_html=True)

    # --- Contenido ---
    st.markdown('<div class="contenido">', unsafe_allow_html=True)

    # Navegación con Streamlit
    if 'pagina' not in st.session_state:
        st.session_state.pagina = 'Home'

    def cambiar_pagina(p):
        st.session_state.pagina = p

    col_menu, col_content = st.columns([1,5])

    with col_content:
        # Página Home
        if st.session_state.pagina == "Home":
            st.header("🏠 Home")
            st.write("Bienvenido a AstroCycle. Explora todo desde aquí.")
            st.image(
                "https://www.nasa.gov/wp-content/uploads/2023/03/hs-2009-25-a-xlarge_web.jpg",
                use_container_width=True
            )

        elif st.session_state.pagina == "Datos Generales":
            st.header("📊 Datos Generales")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Nombre", "Rover Prot1")
                st.metric("Modelo", "X-2025")
                st.metric("Código", "RC-001")
            with col2:
                st.metric("Peso", "45 kg")
                st.metric("Altura", "1.2 m")
                st.metric("Capacidad", "15 kg")

        elif st.session_state.pagina == "Status":
            st.header("🤖 Status del Robot")
            st.metric("Estado General", "Funcionando")
            st.metric("Batería", "78%")
            st.progress(78)
            st.metric("Sensores Activos", "5/5")
            st.metric("Conectividad", "Online")
            st.write("Última alerta: Ninguna")

        elif st.session_state.pagina == "Craft":
            st.header("🛠️ Craft")
            st.write("Contenido relacionado a la construcción y fabricación.")

        elif st.session_state.pagina == "Materiales":
            st.header("📦 Materiales")
            st.write("Inventario de materiales y buscador.")

        elif st.session_state.pagina == "Especificaciones":
            st.header("⚙️ Especificaciones")
            st.write("Detalles técnicos y modelo 3D interactivo del prototipo.")
            viewer_url = "https://learouse.github.io/prototipo/"
            components.iframe(viewer_url, height=600, width="100%", scrolling=True)

        elif st.session_state.pagina == "Configuracion":
            st.header("🧩 Configuración")
            st.write("Opciones de configuración de la app.")

    st.markdown('</div></div>', unsafe_allow_html=True)  # cerrar contenedor
