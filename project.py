import streamlit as st

# ---------- Configuración ----------
st.set_page_config(page_title="AstroCycle", layout="wide")

# ---------- Estilos personalizados ----------
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}

    .sidebar-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 240px;
        height: 100vh;
        background: rgba(15, 15, 15, 0.9);
        backdrop-filter: blur(10px);
        color: white;
        padding: 24px 16px;
        box-sizing: border-box;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #fff;
        margin-bottom: 24px;
        text-align: center;
    }

    .menu-button {
        display: block;
        width: 100%;
        padding: 12px 16px;
        text-align: left;
        border-radius: 8px;
        border: none;
        background: rgba(255,255,255,0.05);
        color: #fff;
        font-weight: 500;
        margin-bottom: 10px;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .menu-button:hover {
        background: rgba(255,255,255,0.15);
        transform: translateX(3px);
    }

    .menu-button.active {
        background: rgba(255,255,255,0.25);
        font-weight: 600;
    }

    .content-container {
        margin-left: 270px;
        padding: 30px;
        color: white;
    }

    body {
        background: radial-gradient(circle at 20% 20%, #0a0a0a, #000);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Menú lateral ----------
st.markdown("""
<div class="sidebar-container">
    <div class="sidebar-title">🚀 AstroCycle</div>
""", unsafe_allow_html=True)

# Lista de páginas
pages = ["🏠 Home", "📊 Datos Generales", "🤖 Status", "🛠️ Craft", "⚙️ Especificaciones"]
# Estado de página
if "page" not in st.session_state:
    st.session_state.page = pages[0]

# Renderizamos los botones
for p in pages:
    active_class = "active" if st.session_state.page == p else ""
    if st.button(p, key=p):
        st.session_state.page = p
    st.markdown(f"<div style='height:2px'></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- Contenido dinámico ----------
st.markdown("<div class='content-container'>", unsafe_allow_html=True)

if st.session_state.page == "🏠 Home":
    st.markdown("## 🏠 Home")
    st.write("Bienvenido al panel principal del proyecto AstroCycle.")

elif st.session_state.page == "📊 Datos Generales":
    st.markdown("## 📊 Datos Generales")
    st.write("Aquí se muestran los datos principales del rover.")

elif st.session_state.page == "🤖 Status":
    st.markdown("## 🤖 Estado del Sistema")
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")

elif st.session_state.page == "🛠️ Craft":
    st.markdown("## 🛠️ Sección de Fabricación")
    st.write("Visualiza el proceso de ensamblaje y mantenimiento del rover.")

elif st.session_state.page == "⚙️ Especificaciones":
    st.markdown("## ⚙️ Especificaciones Técnicas")
    st.write("Incluye la vista 3D del modelo del rover.")

st.markdown("</div>", unsafe_allow_html=True)
