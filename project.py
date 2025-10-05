import streamlit as st
from pathlib import Path
import base64

# ---------- Config ----------
st.set_page_config(page_title="AstroCycle", layout="wide", initial_sidebar_state="collapsed")

# Paths de archivos esperados
VIDEO_FILE = Path("video.mp4")
MODEL_FILE = Path("Rove_prototipo1.glb")

# ---------- Parseo de query params (navegación por links) ----------
params = st.experimental_get_query_params()
if "page" in params:
    page = params["page"][0]
else:
    page = st.session_state.get("page", "home")

if "sub" in params:
    sub = params["sub"][0]
else:
    sub = st.session_state.get("sub", None)

st.session_state.page = page
st.session_state.sub = sub

# ---------- Styles (barra izquierda fija + contenido a la derecha) ----------
st.markdown(
    """
    <style>
    /* General */
    #MainMenu, header, footer {visibility: hidden;}
    body { background: #071019; color: #f1f5f9; }

    /* Sidebar fijo */
    .sidebar-fixed {
        position: fixed;
        top: 0;
        left: 0;
        width: 240px;
        height: 100vh;
        background: linear-gradient(180deg, rgba(8,10,15,0.95), rgba(12,14,18,0.95));
        border-right: 1px solid rgba(255,255,255,0.04);
        padding: 18px;
        box-sizing: border-box;
        z-index: 9999;
        overflow-y: auto;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 16px;
    }

    .menu-btn {
        display: block;
        text-decoration: none;
        color: #e6eef8;
        padding: 12px 14px;
        margin-bottom: 8px;
        border-radius: 8px;
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.02);
        font-weight: 600;
        transition: all 0.12s ease;
    }
    .menu-btn:hover { transform: translateX(6px); background: rgba(255,255,255,0.04); }
    .menu-btn.active { background: rgba(142,207,255,0.12); border-color: rgba(142,207,255,0.22); color: #dff5ff; }

    .sub-btn {
        display: block;
        text-decoration: none;
        color: #cfe7f7;
        padding: 8px 14px;
        margin: 6px 0 10px 10px;
        border-radius: 8px;
        background: rgba(255,255,255,0.01);
        border: 1px solid rgba(255,255,255,0.01);
        font-weight: 500;
        font-size: 14px;
    }
    .sub-btn.active { background: rgba(142,207,255,0.06); border-color: rgba(142,207,255,0.12); }

    /* Contenido principal (a la derecha) */
    .main-area {
        margin-left: 270px;
        padding: 28px;
        min-height: 100vh;
        box-sizing: border-box;
    }

    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.03);
        padding: 16px;
        border-radius: 12px;
    }

    .muted { color: rgba(200,220,240,0.65); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Construcción del menú (HTML anchors para poder estilarlos) ----------
menu_items = [
    ("home", "🏠 Home"),
    ("datos", "📊 Datos Generales"),
    ("status", "🤖 Status"),
    ("craft", "🛠️ Craft"),
    ("specs", "⚙️ Especificaciones"),
    ("config", "⚙ Configuración"),
]

# Generar HTML del menú
menu_html = '<div class="sidebar-fixed">'
menu_html += '<div class="sidebar-title">🚀 AstroCycle</div>'

for key, label in menu_items:
    active = "active" if st.session_state.page == key else ""
    menu_html += f'<a class="menu-btn {active}" href="?page={key}">{label}</a>'

# Subpáginas solo visibles cuando page == datos
if st.session_state.page == "datos":
    subs = [("info", "📄 Información del Rover"), ("tele", "📡 Telemetría"), ("maint", "🧰 Mantenimiento")]
    menu_html += '<div style="margin-top:10px;"><small class="muted">Subsecciones</small></div>'
    for skey, slabel in subs:
        sactive = "active" if st.session_state.sub == skey else ""
        menu_html += f'<a class="sub-btn {sactive}" href="?page=datos&sub={skey}">{slabel}</a>'

menu_html += "</div>"

st.markdown(menu_html, unsafe_allow_html=True)

# ---------- Área principal (a la derecha) ----------
st.markdown('<div class="main-area">', unsafe_allow_html=True)

# ---------- Helper para mostrar título limpio ----------
title_map = {
    "home": "🏠 Home",
    "datos": "📊 Datos Generales",
    "status": "🤖 Status",
    "craft": "🛠️ Craft",
    "specs": "⚙️ Especificaciones",
    "config": "⚙ Configuración",
}
current_page = st.session_state.page
st.markdown(f"## {title_map.get(current_page, current_page)}")

# ---------- Contenido por página ----------
if current_page == "home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("Bienvenido al panel principal de **AstroCycle**. Selecciona una sección en la barra izquierda.")
    st.markdown("</div>", unsafe_allow_html=True)

elif current_page == "datos":
    # Si no hay subselección, pedir que elija
    sub = st.session_state.sub
    if sub is None:
        st.info("Selecciona una subsección desde la barra izquierda (Información / Telemetría / Mantenimiento).")
    elif sub == "info":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📄 Información del Rover")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Nombre", "Rover X-Proto")
            st.metric("Modelo", "Rove 2025")
        with c2:
            st.metric("Código", "RC-002")
            st.metric("Ubicación", "Hangar C")
        st.markdown("</div>", unsafe_allow_html=True)
    elif sub == "tele":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📡 Telemetría")
        st.write("Ejemplo de gráficas recientes:")
        st.line_chart({"Temperatura °C": [18, 19, 21, 20, 22, 23, 22]})
        st.line_chart({"Batería %": [100, 97, 94, 92, 89, 86, 84]})
        st.markdown("</div>", unsafe_allow_html=True)
    elif sub == "maint":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧰 Mantenimiento")
        st.write("- Último chequeo: 2025-10-04")
        st.write("- Componentes reemplazados: módulo térmico y panel solar secundario.")
        st.markdown("</div>", unsafe_allow_html=True)

elif current_page == "status":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 Estado del Sistema")
    battery = st.slider("Nivel de batería (%)", 0, 100, 85)
    st.progress(battery)
    st.metric("Sensores activos", "6/6")
    st.metric("Conectividad", "Online")
    st.markdown("</div>", unsafe_allow_html=True)

elif current_page == "craft":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛠️ Sección de Fabricación")
    st.write("Visualiza el proceso de creación, ensamblaje y mantenimiento del rover.")
    st.markdown("</div>", unsafe_allow_html=True)

elif current_page == "specs":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚙️ Especificaciones Técnicas")
    st.write("Vista 3D y características técnicas del rover.")
    if MODEL_FILE.exists():
        st.success(f"Modelo 3D encontrado: {MODEL_FILE.name}")
        # opcional: mostrar el model-viewer embed (si estás en un entorno que lo soporte)
        st.markdown(f"""
            <model-viewer src="{MODEL_FILE.name}" alt="Modelo 3D del Rover"
                camera-controls auto-rotate exposure="1"
                style="width:100%; height:480px; background: transparent;">
            </model-viewer>
            <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
        """, unsafe_allow_html=True)
    else:
        st.warning("❌ No se encontró el archivo 3D (Rove_prototipo1.glb). Sube el archivo desde Configuración.")
    st.markdown("</div>", unsafe_allow_html=True)

elif current_page == "config":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚙ Configuración")

    # Mostrar estado actual de archivos
    colA, colB = st.columns(2)
    with colA:
        st.write("**Archivos actuales**")
        st.write("Video (video.mp4):", "✔️" if VIDEO_FILE.exists() else "❌ No presente")
        st.write("Modelo 3D (Rove_prototipo1.glb):", "✔️" if MODEL_FILE.exists() else "❌ No presente")

    with colB:
        st.write("**Preferencias**")
        if "show_bg" not in st.session_state:
            st.session_state.show_bg = True
        if "show_model" not in st.session_state:
            st.session_state.show_model = True

        st.session_state.show_bg = st.checkbox("Mostrar fondo animado (video.mp4)", value=st.session_state.show_bg)
        st.session_state.show_model = st.checkbox("Habilitar vista 3D (si existe .glb)", value=st.session_state.show_model)

    st.markdown("---")

    st.write("**Subir/Actualizar archivos**")
    uploaded_video = st.file_uploader("Subir video.mp4 (fondo)", type=["mp4"])
    uploaded_model = st.file_uploader("Subir Rove_prototipo1.glb (modelo 3D)", type=["glb", "gltf", "zip"])

    if st.button("Guardar archivos"):
        saved_any = False
        if uploaded_video is not None:
            data = uploaded_video.read()
            VIDEO_FILE.write_bytes(data)
            st.success(f"Guardado: {VIDEO_FILE.name}")
            saved_any = True
        if uploaded_model is not None:
            data = uploaded_model.read()
            MODEL_FILE.write_bytes(data)
            st.success(f"Guardado: {MODEL_FILE.name}")
            saved_any = True
        if not saved_any:
            st.info("No se cargó ningún archivo. Selecciona un archivo primero.")

    st.markdown("---")
    st.write("**Acciones**")
    if st.button("Restablecer configuración a valores por defecto"):
        # Ajustes por defecto
        st.session_state.show_bg = True
        st.session_state.show_model = True
        st.success("Configuración restablecida.")

    st.write("Puedes volver a la página principal haciendo clic en '🏠 Home' en la barra izquierda.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Pie / nota ----------
st.markdown(
    """
    <div style="position: fixed; right: 12px; bottom: 12px; color: rgba(200,220,240,0.6); font-size:12px;">
        ⚙️ Usa la sección '⚙ Configuración' para subir video.mp4 o Rove_prototipo1.glb.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)  # cierre main-area
