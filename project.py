import streamlit as st

# Inicializar estado
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# Función para manejar clic
def cambiar_pagina(pag):
    st.session_state.pagina = pag

# --- BOTONES FIJOS (usamos CSS para posición absoluta) ---
st.markdown("""
    <style>
        .fixed-button {
            position: fixed;
            z-index: 10;
            width: 120px;
            height: 50px;
            background-color: #444;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        #home { top: 10%; left: 20px; }
        #craft { top: 25%; left: 20px; }
        #mat { top: 40%; left: 20px; }
        #spec { top: 10%; right: 20px; }
        #conf { bottom: 10%; right: 20px; }
    </style>
""", unsafe_allow_html=True)

# Contenedores para ubicar botones con estilo fijo
st.markdown('<div id="home" class="fixed-button">', unsafe_allow_html=True)
if st.button("Home", key="btn1", on_click=cambiar_pagina, args=("Home",)):
    pass
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="craft" class="fixed-button">', unsafe_allow_html=True)
if st.button("Craft", key="btn2", on_click=cambiar_pagina, args=("Craft",)):
    pass
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="mat" class="fixed-button">', unsafe_allow_html=True)
if st.button("Materiales", key="btn3", on_click=cambiar_pagina, args=("Materiales",)):
    pass
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="spec" class="fixed-button">', unsafe_allow_html=True)
if st.button("Specs", key="btn4", on_click=cambiar_pagina, args=("Especificaciones",)):
    pass
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div id="conf" class="fixed-button">', unsafe_allow_html=True)
if st.button("Config", key="btn5", on_click=cambiar_pagina, args=("Configuracion",)):
    pass
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTENIDO DINÁMICO ---
st.markdown("---")
st.subheader(f"Página actual: {st.session_state.pagina}")

if st.session_state.pagina == "Home":
    st.write("Contenido de la página de inicio.")
elif st.session_state.pagina == "Craft":
    st.write("Contenido de la página de construcción.")
elif st.session_state.pagina == "Materiales":
    st.write("Listado de materiales.")
elif st.session_state.pagina == "Especificaciones":
    st.write("Modelo 3D u otros detalles técnicos.")
elif st.session_state.pagina == "Configuracion":
    st.write("Ajustes y configuración de la app.")
