import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---------------- ESTILOS ----------------
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    body {
        background-color: #0a0a0a;
        color: white;
    }
    .menu-btn {
        width: 100%;
        padding: 14px;
        border-radius: 8px;
        border: none;
        color: white;
        background: rgba(255,255,255,0.08);
        text-align: left;
        font-weight: 500;
        margin-bottom: 10px;
        transition: all 0.15s ease;
    }
    .menu-btn:hover {
        background: rgba(255,255,255,0.2);
        transform: translateX(4px);
    }
    .menu-btn.active {
        background: rgba(255,255,255,0.35);
        font-weight: 600;
        border-left: 3px solid #00bfff;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- ESTRUCTURA DE DOS COLUMNAS ----------------
col1, col2 = st.columns([1, 4])  # proporción: 1 parte menú, 4 partes contenido

with col1:
    st.markdown("### 🚀 AstroCycle")
    pages = ["🏠 Home", "📊 Datos Generales", "🤖 Status", "🛠️ Craft", "⚙️ Especificaciones"]

    if "page" not in st.session_state:
        st.session_state.page = pages[0]

    for p in pages:
        if st.button(p, key=p, help=f"Ir a {p}"):
            st.session_state.page = p

with col2:
    st.markdown(f"## {st.session_state.page}")  # título dinámico

    # ---------- CONTENIDO DE CADA SUBPÁGINA ----------
    if st.session_state.page == "🏠 Home":
        st.write("Bienvenido al panel principal del rover **AstroCycle**.")
        st.info("Selecciona una sección en el menú de la izquierda.")

    elif st.session_state.page == "📊 Datos Generales":
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Nombre", "Rover X-Proto")
            st.metric("Modelo", "Rove 2025")
        with c2:
            st.metric("Código", "RC-002")
            st.metric("Ubicación", "Hangar C")
        with c3:
            st.metric("Estado", "Operativo")
            st.metric("Última revisión", "2025-10-04")

    elif st.session_state.page == "🤖 Status":
        battery = st.slider("Nivel de batería (%)", 0, 100, 85)
        st.progress(battery)
        st.metric("Sensores activos", "6/6")
        st.metric("Conectividad", "Online")

    elif st.session_state.page == "🛠️ Craft":
        st.write("Visualiza el proceso de ensamblaje y mantenimiento del rover.")

    elif st.session_state.page == "⚙️ Especificaciones":
        st.write("Aquí se mostrará el modelo 3D y las especificaciones técnicas.")

