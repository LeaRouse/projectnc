import streamlit as st

st.set_page_config(layout="wide", page_title="Panel Rover")

# 🌌 Fondo animado (tu GIF)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
  background: url("https://cdn.discordapp.com/attachments/882749328861564969/1424203752348323901/VideodeWhatsApp2025-10-04alas20.10.24_4530686d-ezgif.com-video-to-gif-converter.gif") no-repeat center center fixed;
  background-size: cover;
}

[data-testid="stHeader"] {
  background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border-right: 1px solid rgba(255,255,255,0.1);
}

/* 🔹 Ocultar círculos del radio button */
[data-testid="stSidebar"] [data-baseweb="radio"] > div:first-child {
  display: none !important;
}

/* 🔹 Botones transparentes */
div[role="radiogroup"] > label {
  background-color: rgba(255,255,255,0.08);
  border-radius: 10px;
  color: white;
  padding: 12px 0;
  text-align: center;
  font-weight: 500;
  margin-bottom: 10px;
  width: 100%;
  border: 1px solid rgba(255,255,255,0.15);
  transition: all 0.3s ease;
  display: block;
  box-sizing: border-box;
}

div[role="radiogroup"] > label:hover {
  background-color: rgba(255,255,255,0.2);
  transform: scale(1.03);
}

/* 🔹 Botón seleccionado (sutil resplandor) */
div[role="radiogroup"] > label[aria-checked="true"] {
  background-color: rgba(255,255,255,0.25) !important;
  border: 1px solid rgba(255,255,255,0.3);
  box-shadow: 0 0 10px rgba(255,255,255,0.2);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🧭 Menú lateral
st.sidebar.title("🛰️ Rover Panel")
pagina = st.sidebar.radio(
    "",
    ["Home", "Datos generales", "Status", "Craft", "Materiales", "Especificaciones", "Configuración"]
)

# 📄 Contenido principal
st.markdown(f"<h1 style='color:white; text-align:center;'>🚀 {pagina}</h1>", unsafe_allow_html=True)

if pagina == "Home":
    st.write("Bienvenido al panel principal del Rover 🌌")
elif pagina == "Datos generales":
    st.write("Aquí irán los datos generales del Rover.")
elif pagina == "Status":
    st.write("Estado actual del sistema del robot.")
elif pagina == "Craft":
    st.write("Detalles de fabricación y prototipo 3D.")
elif pagina == "Materiales":
    st.write("Inventario de materiales del rover.")
elif pagina == "Especificaciones":
    st.write("Detalles técnicos y del sistema.")
elif pagina == "Configuración":
    st.write("Opciones de configuración y control.")
