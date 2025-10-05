import streamlit as st
from pathlib import Path

# ---- CONFIGURACIÓN BÁSICA ----
st.set_page_config(page_title="AstroCycle", page_icon="🚀", layout="wide")

# ---- ESTILO CSS ----
page_bg_video = Path("video.mp4")

st.markdown("""
    <style>
    /* Ocultar el encabezado y el menú de Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Fondo de video a pantalla completa */
    .stApp {
        background-color: transparent;
    }
    video {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        object-fit: cover;
    }

    /* Título */
    .title {
        text-align: center;
        font-size: 60px;
        color: white;
        text-shadow: 0 0 20px #00ffff;
        font-family: 'Segoe UI', sans-serif;
        margin-top: 20px;
    }

    /* Botones */
    .stButton>button {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        font-size: 18px;
        padding: 15px 40px;
        border-radius: 10px;
        width: 220px;
        height: 60px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---- REPRODUCIR VIDEO ----
video_file = open(page_bg_video, "rb").read()
video_url = f"data:video/mp4;base64,{video_file.encode('base64').decode()}" if hasattr(video_file, 'encode') else None

st.markdown(f"""
    <video autoplay loop muted playsinline>
        <source src="video.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# ---- CONTENIDO PRINCIPAL ----
st.markdown("<h1 class='title'>AstroCycle</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Inicio")

with col2:
    st.button("Simulación")

with col3:
    st.button("Acerca de")

