import streamlit as st

st.set_page_config(
    page_title="AutoValuate MA | Vehicle Valuation",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap');

/* ── BASE ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0A0A0A !important;
    color: #E8E8E8 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stMain"] { background: #0A0A0A !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #111111 !important;
    border-right: 1px solid #2A2A2A !important;
    padding-top: 0 !important;
}

[data-testid="stSidebar"] > div:first-child { padding: 0 !important; }

.sidebar-logo-block {
    background: linear-gradient(135deg, #8B1A1A 0%, #5C0F0F 100%);
    padding: 28px 24px 22px 24px;
    margin-bottom: 8px;
}

.sidebar-logo-block .brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.3px;
    margin: 0;
}

.sidebar-logo-block .brand-sub {
    font-size: 11px;
    color: rgba(255,255,255,0.60);
    margin: 3px 0 0 0;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.nav-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #555555;
    text-transform: uppercase;
    padding: 20px 24px 8px 24px;
}

[data-testid="stSidebar"] .stRadio > label { display: none !important; }

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 2px !important;
    padding: 0 12px !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    padding: 10px 14px !important;
    border-radius: 8px !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    color: #888888 !important;
    background: transparent !important;
    border: none !important;
    width: 100% !important;
    margin: 1px 0 !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: #1E1E1E !important;
    color: #E8E8E8 !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"],
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, #8B1A1A 0%, #5C0F0F 100%) !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] input[type="radio"] {
    display: none !important;
}

.sidebar-footer {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    padding: 16px 24px;
    border-top: 1px solid #2A2A2A;
    background: #111111;
}

.sidebar-footer .status-dot {
    display: inline-block;
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #C0392B;
    margin-right: 6px;
    box-shadow: 0 0 6px #C0392B;
    animation: pulse-dot 2s infinite;
}

@keyframes pulse-dot {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.4; }
}

/* ── MAIN CONTENT ── */
.block-container {
    padding: 32px 40px 48px 40px !important;
    max-width: 1400px !important;
}

/* ── PAGE HEADER ── */
.page-header {
    margin-bottom: 32px;
    padding-bottom: 24px;
    border-bottom: 1px solid #2A2A2A;
}

.page-header .eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #C0392B;
    margin-bottom: 8px;
}

.page-header h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 32px !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    margin: 0 0 8px 0 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.5px !important;
}

.page-header p {
    font-size: 15px !important;
    color: #666666 !important;
    margin: 0 !important;
    line-height: 1.5 !important;
}

.gradient-text {
    background: linear-gradient(135deg, #C0392B, #E74C3C);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ── CARDS ── */
.card {
    background: #161616;
    border: 1px solid #2A2A2A;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    transition: border-color 0.2s ease;
}

.card:hover { border-color: #3A3A3A; }

.card-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #555555;
    margin: 0 0 16px 0;
}

/* ── METRIC CARDS ── */
.metric-card {
    background: #161616;
    border: 1px solid #2A2A2A;
    border-radius: 12px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
}

.metric-card.red::before    { background: #C0392B; }
.metric-card.white::before  { background: #FFFFFF; }
.metric-card.grey::before   { background: #888888; }
.metric-card.dark::before   { background: #444444; }

.metric-card .label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #555555;
    margin: 0 0 8px 0;
}

.metric-card .value {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 800;
    margin: 0;
    line-height: 1;
}

.metric-card .value.red   { color: #C0392B; }
.metric-card .value.white { color: #FFFFFF; }
.metric-card .value.grey  { color: #AAAAAA; }
.metric-card .value.dark  { color: #666666; }

.metric-card .sub {
    font-size: 12px;
    color: #555555;
    margin: 4px 0 0 0;
}

/* ── RESULT CARD ── */
.result-card {
    background: linear-gradient(135deg, #1A0A0A 0%, #0D0505 100%);
    border: 1px solid #8B1A1A;
    border-radius: 12px;
    padding: 28px 24px;
    text-align: center;
    margin-top: 8px;
}

.result-card .result-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #C0392B;
    margin: 0 0 12px 0;
}

.result-card .result-price {
    font-family: 'Syne', sans-serif;
    font-size: 42px;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0;
    line-height: 1;
}

.result-card .result-currency {
    font-size: 18px;
    color: #E74C3C;
    font-weight: 600;
}

.result-card .result-divider {
    height: 1px;
    background: #2A1010;
    margin: 18px 0;
}

.result-card .result-meta {
    display: flex;
    justify-content: space-around;
    gap: 8px;
}

.result-card .result-meta-item .meta-label {
    font-size: 10px;
    color: #555555;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 0 0 3px 0;
}

.result-card .result-meta-item .meta-value {
    font-size: 13px;
    font-weight: 600;
    color: #AAAAAA;
    margin: 0;
}

/* ── PLACEHOLDER ── */
.placeholder-card {
    background: #0A0A0A;
    border: 1px dashed #2A2A2A;
    border-radius: 12px;
    padding: 48px 24px;
    text-align: center;
    margin-top: 8px;
}

.placeholder-card p {
    font-size: 14px;
    color: #555555;
    margin: 0;
    line-height: 1.6;
}

/* ── FORM ELEMENTS ── */
[data-testid="stSelectbox"] > div > div,
[data-testid="stNumberInput"] input {
    background: #0A0A0A !important;
    border-color: #2A2A2A !important;
    color: #E8E8E8 !important;
    border-radius: 8px !important;
}

[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stNumberInput"] input:focus {
    border-color: #8B1A1A !important;
    box-shadow: 0 0 0 2px rgba(139,26,26,0.25) !important;
}

[data-testid="stSelectbox"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSlider"] label {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: #666666 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.8px !important;
    margin-bottom: 4px !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #8B1A1A !important;
    border-color: #8B1A1A !important;
}

/* ── BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, #8B1A1A 0%, #5C0F0F 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 24px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    box-shadow: 0 4px 14px rgba(139,26,26,0.35) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(139,26,26,0.5) !important;
    filter: brightness(1.1) !important;
}

.stButton > button:active { transform: translateY(0) !important; }

/* ── PIPELINE STEPS ── */
.pipeline-step {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    align-items: flex-start;
}

.step-number {
    flex-shrink: 0;
    width: 36px; height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, #8B1A1A, #5C0F0F);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 800;
    color: white;
    margin-top: 2px;
}

.step-body .step-title {
    font-size: 15px;
    font-weight: 700;
    color: #E8E8E8;
    margin: 0 0 6px 0;
}

.step-body .step-desc {
    font-size: 13px;
    color: #666666;
    line-height: 1.7;
    margin: 0;
}

.step-body code {
    background: #1E1E1E;
    color: #E74C3C;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 12px;
}

/* ── CHART TITLE ── */
.chart-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #555555;
    margin: 0 0 16px 0;
}

/* ── DIVIDER ── */
hr, [data-testid="stDivider"] { border-color: #2A2A2A !important; }

/* ── ALERTS ── */
[data-testid="stAlert"] {
    background: #161616 !important;
    border: 1px solid #2A2A2A !important;
    border-radius: 8px !important;
    color: #AAAAAA !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0A0A0A; }
::-webkit-scrollbar-thumb { background: #2A2A2A; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #3A3A3A; }

/* ── HIDE DEFAULT STREAMLIT UI (garde le menu hamburger) ── */
/* ── STREAMLIT UI ── */

/* Masquer uniquement le footer et la décoration */
footer,
[data-testid="stDecoration"] {
    display: none !important;
}

/* Garder le header et le menu visibles */
header[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: none !important;
    visibility: visible !important;
    display: block !important;
}

/* Garder la barre d'outils */
[data-testid="stToolbar"] {
    display: block !important;
    visibility: visible !important;
}ss

/* ── COLUMN GAP ── */
[data-testid="column"] { padding: 0 8px !important; }
</style>
""", unsafe_allow_html=True)


def main():
    # ── Sidebar ──
    st.sidebar.markdown("""
    <div class="sidebar-logo-block">
        <div style="font-size:28px; margin-bottom:10px;"> </div>
        <p class="brand-name">AutoValuate MA</p>
        <p class="brand-sub">AI Valuation Engine · v2.4</p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<div class="nav-label">Navigation</div>', unsafe_allow_html=True)

    page = st.sidebar.radio(
        "Go to",
        ["  Home", "  Dashboard", "  Architecture"],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("""
    <div class="sidebar-footer">
        <div style="font-size:12px; color:#555555; margin-bottom:6px;">
            <span class="status-dot"></span>Model active
        </div>
        <div style="font-size:11px; color:#333333;">© 2026 AutoValuate Labs</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Routing ──
    if "Home" in page:
        from views.Home import show_home
        show_home()
    elif "Dashboard" in page:
        from views.Dashboard import show_dashboard
        show_dashboard()
    elif "Architecture" in page:
        from views.About import show_about
        show_about()


if __name__ == "__main__":
    main()