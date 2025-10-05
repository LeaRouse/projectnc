st.markdown("""
<style>
/* ===== FONDO ===== */
.stApp { background: transparent !important; color: #d0d0d0 !important; }
video#bgvid {
    position: fixed; top:50%; left:50%;
    min-width:100%; min-height:100%;
    transform:translate(-50%, -50%);
    object-fit:cover;
    z-index:-3;
    filter: brightness(0.65) contrast(1.05);
}
.bg-overlay { position: fixed; inset:0; background: rgba(0,0,0,0.45); z-index:-2; }

/* ===== LÍNEA DIVISORIA IZQUIERDA ===== */
.sidebar-line {
    position: fixed;
    top: 0;
    left: 230px;               /* distancia desde el borde izquierdo */
    height: 100vh;
    width: 2px;
    background: linear-gradient(
        to bottom,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.25) 30%,
        rgba(255,255,255,0.25) 70%,
        rgba(255,255,255,0) 100%
    );
    z-index: 1;
    backdrop-filter: blur(2px);
}

/* ===== BOTONES ===== */
.icon-button {
    position: fixed;
    background: rgba(35,35,35,0.75);
    border: 2px solid rgba(255,255,255,0.25);
    cursor: pointer;
    transition: all 0.25s ease;
    z-index: 5;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

/* --- EFECTO HOVER --- */
.icon-button:hover {
    background: rgba(255,255,255,0.08);
    transform: scale(1.05);
    border-color: rgba(255,255,255,0.6);
}

/* --- IMÁGENES --- */
.icon-button img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
    filter: brightness(0.93) contrast(1.05);
    transition: all 0.25s ease;
}
.icon-button:hover img {
    filter: brightness(1.05) contrast(1.1);
}

/* --- BOTONES IZQUIERDA (CUADRADOS GRANDES Y ESPACIADOS) --- */
#btn-home, #btn-craft, #btn-mat {
    left: 25px;
    width: 180px;
    height: 180px;
    border-radius: 22px;
}
#btn-home { top: 12%; }
#btn-craft { top: 41%; }
#btn-mat { top: 70%; }

/* --- BOTONES DERECHA (CÍRCULOS) --- */
#btn-spec, #btn-config {
    border-radius: 50%;
    width: 80px;
    height: 80px;
}
#btn-spec { right: 25px; top: 80px; }
#btn-config { right: 25px; bottom: 30px; }

/* --- TEXTOS --- */
h1,h2,h3,p,span { color:#d0d0d0 !important; }
</style>

<!-- Inserta la línea visual -->
<div class="sidebar-line"></div>
""", unsafe_allow_html=True)
