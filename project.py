import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Panel Rover")

# GIF de fondo animado
gif_url = "https://media.discordapp.net/attachments/882749328861564969/1424230119525843069/JPL-20220906-Perseverance_Explores_Jezero_Crater_Delta_UHDsmall_online-video-cutter.com.gif?ex=68e33129&is=68e1dfa9&hm=1919fe256093826069802cc23de1c3b55dc7f2cffc3fd7c689292aaba519466f&=&width=856&height=482"

# Estilos CSS
css = f"""
<style>
[data-testid="stAppViewContainer"] {{
  background: url("{gif_url}") no-repeat center center fixed;
  background-size: cover;
}}
[data-testid="stSidebar"] {{
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
}}
div.stButton > button {{
  background-color: rgba(50, 50, 50, 0.85);
  color: white;
  border-radius: 8px;
  padding: 10px;
  transition: 0.3s;
  font-weight: 500;
}}
div.stButton > button:hover {{
  background-color: rgba(100, 100, 100, 0.9);
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Menú lateral
st.sidebar.title("🚀 Panel del Rover")
pagina = st.sidebar.radio(
    "Menú",
    ["Home", "Datos generales", "Status", "Craft", "Materiales", "Especificaciones", "Configuración"]
)

# Contenido principal
st.title(pagina)

if pagina == "Home":
    st.write("Bienvenido al panel principal del Rover")
elif pagina == "Datos generales":
    st.write("Aquí van los datos generales del Rover")
elif pagina == "Status":
    st.write("Estado del robot")
elif pagina == "Craft":
    st.write("Sección Craft")
elif pagina == "Materiales":
    st.write("Sección Materiales")
elif pagina == "Especificaciones":
    st.write("Aquí va el modelo 3D")
    reader = f'<iframe src="{gif_url}" width="100%" height="400"></iframe>'
    st.markdown(reader, unsafe_allow_html=True)
elif pagina == "Configuración":
    st.write("Opciones de configuración del sistema")
