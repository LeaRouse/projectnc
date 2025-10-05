


import streamlit as st
from pathlib import Path

# ---- CONFIGURACIÓN ----
st.set_page_config(page_title="AstroCycle", page_icon="🚀", layout="wide")

# ---- ESTILOS ----
st.markdown("""
    <style>
    /* Ocultar header y menú */
    #MainMenu, header, footer {visibility: hidden;}

    /* Fondo de video */
    video {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
    }

    /* Estilo del título */
    .title {
        text-align: center;
        font-size: 55px;
        color: white;
        text-shadow: 0 0 25px #00ffff;
        font-family: 'Segoe UI', sans-serif;
        margin-top: 20px;
    }

    /* Botones iguales */
    section[data-testid="stSidebar"] .stButton>button {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
        height: 55px;
        margin-top: 10px;
        transition: all 0.3s ease;
    }
    section[data-testid="stSidebar"] .stButton>button:hover {
        background: rgba(255,255,255,0.25);
        transform: scale(1.05);
    }

    /* Fondo transparente de sidebar */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

# ---- VIDEO DE FONDO ----
st.markdown("""
    <video autoplay loop muted playsinline>
        <source src="video.mp4" type="video/mp4">
    </video>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
st.sidebar.title("🚀 AstroCycle")
st.sidebar.markdown("---")

# Botones en la barra lateral
st.sidebar.button("Inicio")
st.sidebar.button("Simulación")
st.sidebar.button("Modelo 3D")
st.sidebar.button("Acerca de")

# ---- CONTENIDO CENTRAL ----
st.markdown("<h1 class='title'>AstroCycle</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>Proyecto de exploración espacial interactivo.</p>", unsafe_allow_html=True)
