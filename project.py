import streamlit as st

# ---------- Configuración ----------
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---------- Estilos ----------
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}

    /* Fondo y fuente */
    body {
        background-color: #0a0a0a;
        color: white;
    }

    /* Barra lateral izquierda */
    .sidebar-fixed {
        position: fixed;
        top: 0;
        left: 0;
        width: 230px;
        height: 100vh;
        background: rgba(20,20,20,0.95);
        border-right: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        padding: 25px 15px;
        box-sizing: border-box;
        color: white;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        margin-bottom: 24px;
    }

    .menu-btn {
        width: 100%;
        padding: 12px 14px;
        margin-bottom: 10px;
        background: rgba(255,255,255,0.04);
        border: none;
        border-radius: 8px;
        color: #fff;
        font-weight: 500;
        text-align: left;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .menu-btn:hover {
        background: rgba(255,255,255,0.1);
        transform: translateX(4px);
    }

    .menu-btn.active {
        background: rgba(255,255,255,0.18);
        font-weight: 600;
        border-left: 3px solid #8ecfff;
    }

    /* Contenedor principal a la derecha */
    .main-content {
        margin-left: 250px;
        padding: 30px 50px;
        color: white;
    }

    h2 {
        margin-top: 0;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Menú lateral ----------
st.markdown("""
<div class="sidebar-fixed">
    <div class="sidebar-title">🚀 AstroCycle</div>
""", unsafe_allow_html=True)

# Lista de páginas
pages = ["🏠 Home", "📊 Datos Generales", "🤖 Status", "🛠️ Craft", "⚙️ Especificaciones"]
if "page" not in st.session_state:
    st.session_state.page = pages[0]

# Crear botones del menú
for p in pages:
    active_class = "active" if st.session_state.page == p else ""
    if st.button(p, key=p):
        st.session_state.page = p
    st.markdown(f"""
        <script>
        var btn = window.parent.document.querySelector('button[key="{p}"]');
        if (btn) btn.classList.add('{active_class}');
        </script>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Contenido a la derecha ----------
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

if st.session_state.page == "🏠 Home":
    st.markdown("## 🏠 Home")
    st.write("Bienvenido al panel principal del proyecto **AstroCycle**.")
    st.write("Aquí podrás monitorear todos los módulos del rover.")

elif st.session_state.page == "📊 Datos Generales":
    st.markdown("## 📊 Datos Generales")
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
    st.markdown("## 🤖 Estado del Sistema")
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif st.session_state.page == "🛠️ Craft":
    st.markdown("## 🛠️ Sección de Fabricación")
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")

elif st.session_state.page == "⚙️ Especificaciones":
    st.markdown("## ⚙️ Especificaciones Técnicas")
    st.write("Aquí irá el modelo 3D y las características técnicas del rover.")

st.markdown("</div>", unsafe_allow_html=True)
