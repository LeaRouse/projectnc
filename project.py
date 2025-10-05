import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="wide", page_title="Panel Rover")

# 🔹 Fondo animado con tu GIF
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
  background: url("https://cdn.discordapp.com/attachments/882749328861564969/1424203752348323901/VideodeWhatsApp2025-10-04alas20.10.24_4530686d-ezgif.com-video-to-gif-converter.gif?ex=68e3189a&is=68e1c71a&hm=a61f2e60afe76a05157dcabe8b2e235a1ed337db0a9262074c2ece64ca2fdffe&") no-repeat center center fixed;
  background-size: cover;
}

[data-testid="stHeader"] {
  background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
  background-color: rgba(10, 10, 10, 0.8);
  color: white;
}

div.stButton > button {
  width: 100%;
  background-color: rgba(50, 50, 50, 0.85);
  color: white;
  border-radius: 8px;
  padding: 10px;
  transition: 0.3s;
  font-weight: 500;
}

div.stButton > button:hover {
  background-color: rgba(100, 100, 100, 0.9);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🔹 Barra lateral
st.sidebar.title("🚀 Rover Control")
pagina = st.sidebar.radio(
    "Menú",
    ["Home", "Datos generales", "Status", "Craft", "Materiales", "Especificaciones", "Configuración"]
)

# 🔹 Contenido principal (placeholder)
st.title(f"Página: {pagina}")

if pagina == "Home":
    st.write("Bienvenido al panel principal del Rover 🚀")
elif pagina == "Datos generales":
    st.write("Aquí irán los datos generales del Rover.")
elif pagina == "Status":
    st.write("Estado actual del sistema.")
elif pagina == "Craft":
    st.write("Detalles de fabricación y prototipo.")
elif pagina == "Materiales":
    st.write("Inventario de materiales.")
elif pagina == "Especificaciones":
    st.write("Detalles técnicos del sistema.")
elif pagina == "Configuración":
    st.write("Configuración del sistema y opciones avanzadas.")
