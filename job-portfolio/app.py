import time
import base64
from pathlib import Path

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Job Pulache · Analista de Datos y Procesos",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"


def img_b64(name: str) -> str:
    p = ASSETS / name
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode()


PHOTO_NATURAL = img_b64("profile_natural.jpg")
PHOTO_DUOTONE = img_b64("profile_duotone.jpg")

# ----------------------------------------------------------------------------
# THEME STATE
# ----------------------------------------------------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"


def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"


THEME = st.session_state.theme

if THEME == "dark":
    C = dict(
        bg="#0E1210",
        bg_alt="#141B18",
        card="#131916",
        card_hover="#171F1B",
        text="#E7EFE9",
        text_dim="#8FA79A",
        text_faint="#576760",
        accent="#4FD183",
        accent_2="#E8C468",
        border="rgba(231,239,233,0.10)",
        border_strong="rgba(79,209,131,0.35)",
        grid_line="rgba(79,209,131,0.06)",
        shadow="0 20px 60px rgba(0,0,0,0.45)",
        mode_label="MODO_NOCTURNO",
        toggle_icon="☾",
    )
else:
    C = dict(
        bg="#F3F1E7",
        bg_alt="#EAE7D9",
        card="#FCFBF6",
        card_hover="#FFFFFF",
        text="#14181A",
        text_dim="#4B5750",
        text_faint="#8A9187",
        accent="#2E6B45",
        accent_2="#9C6B1F",
        border="rgba(20,24,26,0.10)",
        border_strong="rgba(46,107,69,0.35)",
        grid_line="rgba(46,107,69,0.07)",
        shadow="0 20px 50px rgba(20,24,26,0.08)",
        mode_label="MODO_DIURNO",
        toggle_icon="☀",
    )

# ----------------------------------------------------------------------------
# GLOBAL CSS
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Public+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {{
    --bg: {C['bg']};
    --bg-alt: {C['bg_alt']};
    --card: {C['card']};
    --card-hover: {C['card_hover']};
    --text: {C['text']};
    --text-dim: {C['text_dim']};
    --text-faint: {C['text_faint']};
    --accent: {C['accent']};
    --accent-2: {C['accent_2']};
    --border: {C['border']};
    --border-strong: {C['border_strong']};
    --grid-line: {C['grid_line']};
    --shadow: {C['shadow']};
}}

#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header[data-testid="stHeader"] {{background: transparent;}}
div[data-testid="stToolbar"] {{visibility: hidden;}}
div[data-testid="stDecoration"] {{display:none;}}

html, body, [class*="css"] {{
    font-family: 'Public Sans', sans-serif;
}}

[data-testid="stAppViewContainer"] {{
    background-color: var(--bg);
    background-image:
        linear-gradient(var(--grid-line) 1px, transparent 1px),
        linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
    background-size: 42px 42px;
    color: var(--text);
    transition: background-color 0.4s ease, color 0.4s ease;
}}

[data-testid="stAppViewContainer"] > .main {{
    padding-top: 0rem;
}}

.block-container {{
    max-width: 1180px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}}

h1, h2, h3, h4 {{
    font-family: 'Space Mono', monospace;
    letter-spacing: -0.01em;
}}

::-webkit-scrollbar {{ width: 10px; }}
::-webkit-scrollbar-track {{ background: var(--bg); }}
::-webkit-scrollbar-thumb {{ background: var(--border-strong); border-radius: 0px; }}

/* ---- Mono utility text ---- */
.mono {{
    font-family: 'Space Mono', monospace;
}}
.tag {{
    display:inline-block;
    font-family:'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid var(--border-strong);
    padding: 3px 10px;
    border-radius: 2px;
    background: color-mix(in srgb, var(--accent) 8%, transparent);
}}

/* ---- Top bar ---- */
.topbar {{
    display:flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 22px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 8px;
}}
.topbar .brand {{
    font-family:'Space Mono', monospace;
    font-size: 0.95rem;
    letter-spacing: 0.02em;
    color: var(--text);
}}
.topbar .brand span {{ color: var(--accent); }}
.status-dot {{
    display:inline-block; width:7px; height:7px; border-radius:50%;
    background: var(--accent); margin-right:7px;
    box-shadow: 0 0 8px var(--accent);
    animation: blink 1.8s infinite;
}}
@keyframes blink {{ 0%,100%{{opacity:1}} 50%{{opacity:0.25}} }}

/* ---- Hero ---- */
.hero-eyebrow {{
    font-family:'Space Mono', monospace;
    color: var(--text-dim);
    font-size: 0.85rem;
    letter-spacing: 0.05em;
    margin-bottom: 10px;
}}
.hero-eyebrow::before {{ content: "> "; color: var(--accent); }}
.hero-title {{
    font-family:'Space Mono', monospace;
    font-weight: 700;
    font-size: clamp(2.1rem, 5vw, 3.6rem);
    line-height: 1.08;
    margin: 0 0 6px 0;
    color: var(--text);
}}
.hero-title .accent {{ color: var(--accent); }}
.hero-role {{
    font-size: 1.05rem;
    color: var(--text-dim);
    max-width: 560px;
    line-height: 1.6;
    margin-bottom: 18px;
}}
.hero-cursor {{
    display:inline-block; width:10px; height:1.15em; background: var(--accent);
    vertical-align: middle; margin-left: 4px;
    animation: blink 1s steps(2) infinite;
}}
.photo-frame {{
    position: relative;
    border: 1px solid var(--border-strong);
    padding: 10px;
    background: var(--card);
    box-shadow: var(--shadow);
}}
.photo-frame img {{
    width: 100%;
    display:block;
    filter: saturate(0.96) contrast(1.03);
}}
.photo-frame .corner {{
    position:absolute; width:14px; height:14px;
    border-color: var(--accent); border-style: solid;
}}
.photo-frame .tl {{ top:-1px; left:-1px; border-width: 2px 0 0 2px; }}
.photo-frame .br {{ bottom:-1px; right:-1px; border-width: 0 2px 2px 0; }}
.photo-caption {{
    font-family:'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-faint);
    margin-top: 8px;
    display:flex; justify-content: space-between;
}}

/* ---- Section headers ---- */
.sec-num {{
    font-family:'Space Mono', monospace;
    color: var(--accent);
    font-size: 0.85rem;
}}
.sec-title {{
    font-size: 1.55rem;
    font-weight: 700;
    margin: 2px 0 4px 0;
    color: var(--text);
}}
.sec-sub {{
    color: var(--text-dim);
    font-size: 0.95rem;
    margin-bottom: 22px;
    max-width: 620px;
}}

/* ---- KPI cards ---- */
.kpi {{
    background: var(--card);
    border: 1px solid var(--border);
    border-left: 2px solid var(--accent);
    padding: 16px 18px;
    height: 100%;
}}
.kpi .num {{
    font-family:'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1;
}}
.kpi .lbl {{
    color: var(--text-dim);
    font-size: 0.82rem;
    margin-top: 6px;
}}

/* ---- Cards (case studies) ---- */
.case-card {{
    background: var(--card);
    border: 1px solid var(--border);
    padding: 26px 26px 20px 26px;
    height: 100%;
    transition: border-color 0.25s ease, transform 0.25s ease;
}}
.case-card:hover {{
    border-color: var(--border-strong);
    transform: translateY(-3px);
}}
.case-card .idx {{
    font-family:'Space Mono', monospace;
    color: var(--accent);
    font-size: 0.8rem;
    margin-bottom: 10px;
}}
.case-card h4 {{
    font-size: 1.15rem;
    margin: 0 0 4px 0;
}}
.case-card .co {{
    font-family:'Space Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-faint);
    margin-bottom: 14px;
    letter-spacing: 0.04em;
}}
.case-card .block-label {{
    font-family:'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    color: var(--accent);
    margin-top: 12px;
    margin-bottom: 4px;
}}
.case-card p {{
    color: var(--text-dim);
    font-size: 0.9rem;
    line-height: 1.55;
    margin: 0;
}}
.chip {{
    display:inline-block;
    font-family:'Space Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-dim);
    border: 1px solid var(--border);
    padding: 2px 8px;
    margin: 3px 6px 0 0;
}}

/* ---- Timeline ---- */
.tl-row {{
    display:flex; gap: 18px; padding: 14px 0; border-bottom: 1px solid var(--border);
}}
.tl-row:last-child {{ border-bottom: none; }}
.tl-date {{
    font-family:'Space Mono', monospace;
    font-size: 0.78rem;
    color: var(--accent);
    min-width: 130px;
    padding-top: 2px;
}}
.tl-content h5 {{ margin: 0 0 2px 0; font-size: 1rem; }}
.tl-content .role {{ color: var(--text-dim); font-size: 0.85rem; margin-bottom: 4px; }}

/* ---- Demo panel ---- */
.demo-panel {{
    background: var(--card);
    border: 1px solid var(--border-strong);
    padding: 22px 24px;
}}
.demo-terminal-head {{
    display:flex; align-items:center; gap:8px; margin-bottom: 14px;
    font-family:'Space Mono', monospace; font-size: 0.75rem; color: var(--text-faint);
}}
.dot {{ width:9px; height:9px; border-radius:50%; display:inline-block; }}
.result-field {{
    display:flex; justify-content: space-between; padding: 7px 0;
    border-bottom: 1px dashed var(--border); font-size: 0.88rem;
}}
.result-field .k {{ color: var(--text-faint); font-family:'Space Mono', monospace; font-size:0.78rem; }}
.result-field .v {{ color: var(--text); font-weight: 600; text-align:right; }}

/* ---- Buttons ---- */
.stButton>button {{
    font-family: 'Space Mono', monospace !important;
    background: transparent !important;
    color: var(--text) !important;
    border: 1px solid var(--border-strong) !important;
    border-radius: 0px !important;
    padding: 8px 18px !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.04em;
    transition: all 0.2s ease;
}}
.stButton>button:hover {{
    background: var(--accent) !important;
    color: var(--bg) !important;
    border-color: var(--accent) !important;
}}
.stButton>button:focus:not(:active) {{
    color: var(--text) !important;
}}

/* Selectbox */
[data-testid="stSelectbox"] label {{
    font-family:'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    color: var(--text-dim) !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}}

/* footer */
.footbar {{
    margin-top: 60px;
    padding-top: 22px;
    border-top: 1px solid var(--border);
    display:flex; justify-content: space-between; align-items:center;
    font-family:'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-faint);
    flex-wrap: wrap;
    gap: 10px;
}}
.footbar a {{ color: var(--text-dim); text-decoration:none; }}
.footbar a:hover {{ color: var(--accent); }}

a.linklike {{
    color: var(--accent) !important;
    text-decoration: none;
    border-bottom: 1px solid var(--border-strong);
}}

/* Responsive stacking */
@media (max-width: 900px) {{
    [data-testid="stHorizontalBlock"] {{
        flex-wrap: wrap !important;
    }}
    [data-testid="stHorizontalBlock"] > div {{
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }}
    .hero-title {{ font-size: 2.1rem; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# TOP BAR
# ----------------------------------------------------------------------------
top_l, top_r = st.columns([5, 1])
with top_l:
    st.markdown(
        f"""
        <div class="topbar">
            <div class="brand"><span class="status-dot"></span>JOB<span>.</span>PULACHE &nbsp;/&nbsp; <span style="color:var(--text-dim); font-weight:400;">analista_datos_y_procesos</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_r:
    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
    st.button(f"{C['toggle_icon']} {C['mode_label']}", on_click=toggle_theme, use_container_width=True)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
hero_l, hero_r = st.columns([1.3, 1], gap="large")
with hero_l:
    st.markdown(
        f"""
        <div class="hero-eyebrow">piura, perú &nbsp;·&nbsp; disponible para nuevas oportunidades</div>
        <div class="hero-title">Job Pulache<br><span class="accent">Carreño</span><span class="hero-cursor"></span></div>
        <div class="hero-role">
            Bachiller en Sistemas &mdash; analista de datos y procesos con experiencia de campo real
            en <b style="color:var(--text)">operaciones agrícolas</b>, <b style="color:var(--text)">recursos humanos</b>
            y <b style="color:var(--text)">logística de almacén</b>. Transformo información dispersa
            en reportes, automatizaciones y decisiones.
        </div>
        <div>
            <span class="tag">EXCEL AVANZADO</span>
            <span class="tag">AUTOMATIZACIÓN DE DATOS</span>
            <span class="tag">REPORTING</span>
            <span class="tag">SECTOR AGROINDUSTRIAL</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3)
    with b1:
        st.link_button("↗ LinkedIn", "https://www.linkedin.com/in/jobpulachecarreno/", use_container_width=True)
    with b2:
        st.link_button("✆ WhatsApp", "https://wa.me/51930938449", use_container_width=True)
    with b3:
        st.link_button("✉ Correo", "mailto:pulachecarrenojob@gmail.com", use_container_width=True)

with hero_r:
    photo_src = f"data:image/jpeg;base64,{PHOTO_NATURAL}" if PHOTO_NATURAL else ""
    st.markdown(
        f"""
        <div class="photo-frame">
            <div class="corner tl"></div>
            <div class="corner br"></div>
            <img src="{photo_src}" alt="Job Pulache Carreño"/>
        </div>
        <div class="photo-caption">
            <span>IMG_PERFIL.JPG</span>
            <span>PIURA / PE</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# KPI STRIP
# ----------------------------------------------------------------------------
st.markdown(
    """<div class="sec-num">01 / PANEL</div><div class="sec-title">Resumen operativo</div>""",
    unsafe_allow_html=True,
)
k1, k2, k3, k4 = st.columns(4)
kpis = [
    ("3", "sectores de experiencia\n(agro · rrhh · logística)"),
    ("1", "proceso automatizado\ncon consumo de API SUNAT"),
    ("2026", "bachiller en sistemas\nInstituto IDAT"),
    ("100%", "orientado a datos\ny mejora de procesos"),
]
for col, (num, lbl) in zip([k1, k2, k3, k4], kpis):
    with col:
        st.markdown(
            f"""<div class="kpi"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>""",
            unsafe_allow_html=True,
        )

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TIMELINE
# ----------------------------------------------------------------------------
tl_l, tl_r = st.columns([1, 1.15], gap="large")
with tl_l:
    st.markdown(
        """<div class="sec-num">02 / TRAYECTORIA</div>
        <div class="sec-title">Recorrido profesional</div>
        <div class="sec-sub">Tres roles, un mismo hilo conductor: capturar información en el punto donde nace
        el problema y convertirla en algo que alguien más pueda usar para decidir.</div>""",
        unsafe_allow_html=True,
    )

    timeline = [
        ("2026", "Sunshine Export", "Digitador — Operaciones Agrícolas",
         "Registro y control de información de campo. Automaticé la búsqueda de datos de productores consumiendo la API de SUNAT, eliminando la búsqueda manual del área de facturación."),
        ("2025", "ProAgro", "Asistente de Recursos Humanos",
         "Elaboración de reportes de personal para la toma de decisiones. Validación activa de la información para asegurar su exactitud antes de llegar a gerencia."),
        ("2025", "Almacén", "Digitador — Logística",
         "Registro y control documentario del flujo de almacén, coordinación con logística para mantener la trazabilidad de entradas y salidas."),
    ]
    for date, org, role, desc in timeline:
        st.markdown(
            f"""
            <div class="tl-row">
                <div class="tl-date">{date}</div>
                <div class="tl-content">
                    <h5>{org}</h5>
                    <div class="role">{role}</div>
                    <div style="color:var(--text-dim); font-size:0.87rem; line-height:1.55;">{desc}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tl_r:
    categories = ["Almacén · Logística", "ProAgro · RRHH", "Sunshine · Agro"]
    starts = [2025.0, 2025.0, 2026.0]
    ends = [2025.6, 2025.95, 2026.55]

    fig = go.Figure()
    for i, (cat, s, e) in enumerate(zip(categories, starts, ends)):
        fig.add_trace(go.Scatter(
            x=[s, e], y=[cat, cat],
            mode="lines",
            line=dict(color=C["accent"], width=16),
            hovertemplate=f"<b>{cat}</b><br>%{{x:.2f}}<extra></extra>",
            showlegend=False,
        ))
    fig.update_layout(
        height=260,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Space Mono, monospace", color=C["text_dim"], size=11),
        xaxis=dict(title="", showgrid=True, gridcolor=C["grid_line"], zeroline=False,
                    tickfont=dict(color=C["text_faint"])),
        yaxis=dict(showgrid=False, tickfont=dict(color=C["text"], size=12)),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    skills = ["Excel avanzado", "Validación de datos", "Reportes gerenciales",
              "APIs / automatización", "Logística documentaria", "Comunicación con áreas"]
    values = [90, 88, 85, 78, 80, 82]
    fig2 = go.Figure()
    fig2.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=skills + [skills[0]],
        fill="toself",
        line=dict(color=C["accent"], width=2),
        fillcolor=f"rgba({int(C['accent'][1:3],16)},{int(C['accent'][3:5],16)},{int(C['accent'][5:7],16)},0.18)",
        hovertemplate="%{theta}: %{r}<extra></extra>",
    ))
    fig2.update_layout(
        height=280,
        margin=dict(l=40, r=40, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 100], showticklabels=False, gridcolor=C["grid_line"]),
            angularaxis=dict(tickfont=dict(color=C["text_dim"], size=10, family="Public Sans")),
        ),
        showlegend=False,
    )
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CASE STUDIES
# ----------------------------------------------------------------------------
st.markdown(
    """<div class="sec-num">03 / CASOS</div>
    <div class="sec-title">Cómo trabajo</div>
    <div class="sec-sub">Dos ejemplos reales de convertir un problema operativo en un proceso más rápido y confiable.</div>""",
    unsafe_allow_html=True,
)

cs1, cs2 = st.columns(2, gap="large")
with cs1:
    st.markdown(
        """
        <div class="case-card">
            <div class="idx">CASO 01</div>
            <h4>Automatización de búsqueda de productores</h4>
            <div class="co">SUNSHINE EXPORT · OPERACIONES AGRÍCOLAS</div>
            <div class="block-label">PROBLEMA</div>
            <p>El área de facturación perdía tiempo buscando manualmente los datos de cada productor antes de emitir comprobantes.</p>
            <div class="block-label">PROCESO</div>
            <p>Diseñé una consulta automatizada que consume la API de SUNAT para traer la información del productor directamente por su RUC.</p>
            <div class="block-label">RESULTADO</div>
            <p>Facturación dejó de hacer búsquedas manuales: la información llega lista y validada en segundos.</p>
            <div style="margin-top:14px;">
                <span class="chip">API SUNAT</span><span class="chip">AUTOMATIZACIÓN</span><span class="chip">FACTURACIÓN</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with cs2:
    st.markdown(
        """
        <div class="case-card">
            <div class="idx">CASO 02</div>
            <h4>Reportes para toma de decisiones de personal</h4>
            <div class="co">PROAGRO · RECURSOS HUMANOS</div>
            <div class="block-label">PROBLEMA</div>
            <p>Gerencia necesitaba información de personal confiable y a tiempo para decidir, y los datos venían de fuentes dispersas.</p>
            <div class="block-label">PROCESO</div>
            <p>Construí y mantuve reportes periódicos, validando cada dato cruzado con las áreas antes de consolidarlo.</p>
            <div class="block-label">RESULTADO</div>
            <p>Reportes usados directamente para decisiones de gestión de personal, con un margen de error mínimo.</p>
            <div style="margin-top:14px;">
                <span class="chip">RRHH</span><span class="chip">REPORTING</span><span class="chip">VALIDACIÓN DE DATOS</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# LIVE DEMO
# ----------------------------------------------------------------------------
st.markdown(
    """<div class="sec-num">04 / DEMO EN VIVO</div>
    <div class="sec-title">Simulador — automatización de consulta de productor</div>
    <div class="sec-sub">Una versión simplificada del proceso que construí en Sunshine. Datos de ejemplo,
    no información real de SUNAT — sirve para mostrar cómo funciona el flujo.</div>""",
    unsafe_allow_html=True,
)

demo_l, demo_r = st.columns([1, 1.3], gap="large")

MOCK_PRODUCERS = {
    "20601234567 — Agroexportadora Los Médanos S.A.C.": dict(
        razon_social="AGROEXPORTADORA LOS MÉDANOS S.A.C.",
        estado="ACTIVO", condicion="HABIDO",
        direccion="CAR. PIURA-SULLANA KM 12, PIURA",
        actividad="CULTIVO DE FRUTAS (UVA / MANGO)",
    ),
    "20558877441 — Fundo San Miguel E.I.R.L.": dict(
        razon_social="FUNDO SAN MIGUEL E.I.R.L.",
        estado="ACTIVO", condicion="HABIDO",
        direccion="AV. PANAMERICANA NORTE KM 4, SULLANA",
        actividad="CULTIVO DE BANANO ORGÁNICO",
    ),
    "20489912303 — Procesadora Agrícola del Norte S.A.": dict(
        razon_social="PROCESADORA AGRÍCOLA DEL NORTE S.A.",
        estado="ACTIVO", condicion="HABIDO",
        direccion="ZONA INDUSTRIAL, PIURA",
        actividad="PROCESAMIENTO Y CONSERVACIÓN DE FRUTAS",
    ),
}

with demo_l:
    choice = st.selectbox("Selecciona un productor de ejemplo", list(MOCK_PRODUCERS.keys()))
    run = st.button("▶ Ejecutar consulta automatizada", use_container_width=True)

with demo_r:
    st.markdown(
        f"""
        <div class="demo-panel">
            <div class="demo-terminal-head">
                <span class="dot" style="background:#E05252"></span>
                <span class="dot" style="background:#E8C468"></span>
                <span class="dot" style="background:{C['accent']}"></span>
                &nbsp;consulta_sunat.py
            </div>
        """,
        unsafe_allow_html=True,
    )

    placeholder = st.empty()

    if run:
        with placeholder.container():
            with st.spinner("consultando API SUNAT..."):
                time.sleep(1.1)
            data = MOCK_PRODUCERS[choice]
            fields = [
                ("RUC", choice.split(" — ")[0]),
                ("RAZÓN SOCIAL", data["razon_social"]),
                ("ESTADO", data["estado"]),
                ("CONDICIÓN", data["condicion"]),
                ("DIRECCIÓN FISCAL", data["direccion"]),
                ("ACTIVIDAD ECONÓMICA", data["actividad"]),
            ]
            rows = "".join(
                f'<div class="result-field"><span class="k">{k}</span><span class="v">{v}</span></div>'
                for k, v in fields
            )
            st.markdown(rows, unsafe_allow_html=True)

            fig3 = go.Figure()
            fig3.add_trace(go.Bar(
                x=["Búsqueda manual", "Automatizado (API)"],
                y=[8, 0.2],
                marker_color=[C["text_faint"], C["accent"]],
                text=["~8 min", "~12 seg"],
                textposition="outside",
                textfont=dict(family="Space Mono, monospace", color=C["text"]),
            ))
            fig3.update_layout(
                height=200,
                margin=dict(l=10, r=10, t=30, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                yaxis=dict(title="minutos", showgrid=True, gridcolor=C["grid_line"],
                            tickfont=dict(color=C["text_faint"])),
                xaxis=dict(tickfont=dict(color=C["text_dim"], family="Space Mono")),
                font=dict(family="Public Sans", color=C["text_dim"]),
            )
            st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})
    else:
        with placeholder.container():
            st.markdown(
                f"""<div style="color:var(--text-faint); font-family:'Space Mono',monospace; font-size:0.82rem; padding: 30px 0;">
                &gt; esperando ejecución...<span class="hero-cursor"></span>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# CONTACT / FOOTER
# ----------------------------------------------------------------------------
st.markdown(
    """<div class="sec-num">05 / CONTACTO</div>
    <div class="sec-title">Conversemos</div>
    <div class="sec-sub">Abierto a roles de analista de datos, analista de procesos o soporte
    operativo en el sector agroindustrial.</div>""",
    unsafe_allow_html=True,
)

ct1, ct2, ct3 = st.columns(3)
with ct1:
    st.link_button("✉  pulachecarrenojob@gmail.com", "mailto:pulachecarrenojob@gmail.com", use_container_width=True)
with ct2:
    st.link_button("✆  +51 930 938 449 (WhatsApp)", "https://wa.me/51930938449", use_container_width=True)
with ct3:
    st.link_button("↗  linkedin.com/in/jobpulachecarreno", "https://www.linkedin.com/in/jobpulachecarreno/", use_container_width=True)

st.markdown(
    f"""
    <div class="footbar">
        <div>© 2026 JOB PULACHE CARREÑO · PIURA, PERÚ</div>
        <div>build:// streamlit + plotly · {C['mode_label']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)
