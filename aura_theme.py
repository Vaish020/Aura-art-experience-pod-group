"""
aura_theme.py — AURA India Group Dashboard Brand System
"""
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

# ── PALETTE ───────────────────────────────────────────────────
BG       = "#0e0c0a"
SURFACE  = "#161310"
SURFACE2 = "#1e1a16"
SURFACE3 = "#252018"
INK      = "#f0ece4"
MUTED    = "#8a8070"
GOLD     = "#e8c547"
TEAL     = "#5ec4a1"
ORANGE   = "#e07c3a"
ROSE     = "#e06b8b"
INDIGO   = "#7b8cde"
SAGE     = "#7ec8a0"
LAVENDER = "#b59ddc"

PALETTE = [GOLD, TEAL, ORANGE, ROSE, INDIGO, SAGE, LAVENDER, "#f0c080"]
CLUSTER_COLORS = [GOLD, TEAL, ORANGE, ROSE, INDIGO, SAGE, LAVENDER, "#e8a87c"]

# ── PLOTLY TEMPLATE ───────────────────────────────────────────
_aura_template = go.layout.Template()
_aura_template.layout = go.Layout(
    paper_bgcolor=SURFACE,
    plot_bgcolor=SURFACE2,
    font=dict(family="Inter, system-ui, sans-serif", color=INK, size=12),
    title=dict(font=dict(color=INK, size=16, family="Inter, sans-serif"), x=0.01),
    colorway=PALETTE,
    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.08)",
               linecolor="rgba(255,255,255,0.06)", tickcolor=MUTED),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.08)",
               linecolor="rgba(255,255,255,0.06)", tickcolor=MUTED),
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(255,255,255,0.06)", borderwidth=1),
    margin=dict(l=40, r=20, t=50, b=40),
)
pio.templates["aura"] = _aura_template
pio.templates.default = "aura"

# ── GLOBAL CSS ─────────────────────────────────────────────────
GLOBAL_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    background-color: {BG} !important;
    color: {INK} !important;
}}
.stApp {{ background-color: {BG} !important; }}
[data-testid="stSidebar"] {{
    background-color: {SURFACE} !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}}
[data-testid="stSidebar"] * {{ color: {INK} !important; }}
.stRadio > div > label {{ color: {INK} !important; }}
.stRadio > div > div[data-checked="true"] > label {{
    color: {GOLD} !important; font-weight: 600 !important;
}}
.stSelectbox > div > div {{ background-color: {SURFACE2} !important; color: {INK} !important; border-color: rgba(255,255,255,0.1) !important; }}
.stSlider > div {{ background: transparent !important; }}
.stSlider [data-baseweb="slider"] {{ background: transparent !important; }}
div[data-testid="metric-container"] {{
    background: {SURFACE2} !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 8px !important;
    padding: 16px !important;
}}
div[data-testid="metric-container"] label {{ color: {MUTED} !important; font-size: 11px !important; letter-spacing: 0.1em !important; text-transform: uppercase !important; }}
div[data-testid="metric-container"] [data-testid="metric-value"] {{ color: {GOLD} !important; font-weight: 700 !important; font-size: 26px !important; }}
.stDataFrame {{ border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 8px !important; }}
.stDownloadButton > button {{
    background: linear-gradient(135deg, {GOLD}22, {TEAL}22) !important;
    color: {GOLD} !important;
    border: 1px solid {GOLD}44 !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    font-size: 12px !important;
}}
.stDownloadButton > button:hover {{
    background: linear-gradient(135deg, {GOLD}44, {TEAL}44) !important;
    border-color: {GOLD} !important;
}}
.stButton > button {{
    background: linear-gradient(135deg, {GOLD}, {ORANGE}) !important;
    color: {BG} !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
}}
.stButton > button:hover {{ opacity: 0.9 !important; }}
hr {{ border-color: rgba(255,255,255,0.06) !important; }}
.stExpander {{ border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 8px !important; background: {SURFACE2} !important; }}
h1, h2, h3 {{ color: {INK} !important; }}
.stAlert {{ border-radius: 8px !important; }}
</style>
"""

# ── UI HELPERS ────────────────────────────────────────────────
def page_header(title: str, subtitle: str = "", badge: str = ""):
    badge_html = f'<span style="background:{SURFACE3};border:1px solid rgba(255,255,255,0.08);color:{MUTED};font-size:10px;letter-spacing:0.15em;text-transform:uppercase;padding:4px 12px;border-radius:20px;font-weight:600;">{badge}</span>' if badge else ""
    st.markdown(f"""
    <div style="padding:32px 0 24px;">
        {badge_html}
        <div style="font-size:32px;font-weight:800;color:{INK};margin-top:{'12px' if badge else '0'};line-height:1.1;">{title}</div>
        {f'<div style="font-size:15px;color:{MUTED};margin-top:10px;line-height:1.6;max-width:720px;">{subtitle}</div>' if subtitle else ""}
        <div style="width:48px;height:3px;background:linear-gradient(90deg,{GOLD},{TEAL});border-radius:2px;margin-top:16px;"></div>
    </div>
    """, unsafe_allow_html=True)

def section_header(title: str, color: str = GOLD):
    st.markdown(f"""
    <div style="margin:28px 0 14px;">
        <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:3px;height:18px;background:{color};border-radius:2px;"></div>
            <span style="font-size:14px;font-weight:700;color:{INK};letter-spacing:0.04em;">{title}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def info_card(title: str, body: str, color: str = TEAL):
    st.markdown(f"""
    <div style="background:{SURFACE2};border:1px solid rgba(255,255,255,0.06);border-left:3px solid {color};
    border-radius:8px;padding:18px 22px;margin:16px 0;">
        <div style="color:{color};font-size:11px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;margin-bottom:8px;">{title}</div>
        <div style="color:{MUTED};font-size:13px;line-height:1.7;">{body}</div>
    </div>
    """, unsafe_allow_html=True)

def kpi_card(label: str, value: str, delta: str = "", color: str = GOLD):
    delta_html = f'<div style="color:{TEAL};font-size:11px;margin-top:4px;">{delta}</div>' if delta else ""
    return f"""
    <div style="background:{SURFACE2};border:1px solid rgba(255,255,255,0.06);border-top:2px solid {color};
    border-radius:8px;padding:20px;text-align:center;">
        <div style="color:{MUTED};font-size:10px;letter-spacing:0.15em;text-transform:uppercase;font-weight:600;margin-bottom:8px;">{label}</div>
        <div style="color:{color};font-size:28px;font-weight:800;line-height:1;">{value}</div>
        {delta_html}
    </div>
    """
