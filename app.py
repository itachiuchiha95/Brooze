# app.py
import streamlit as st

# ---------------------------------
# iPhone 16 Pro Max target (CSS px)
# Portrait logical size: 440 x 956
# ---------------------------------
st.set_page_config(page_title="Brooze", page_icon="🍷", layout="centered")

st.markdown(
    """
<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Full screen background */
.stApp {
  background: #050506;
}

/* "Screen" area that matches the screenshot layout */
.screen {
  width: 440px;              /* iPhone 16 Pro Max width */
  min-height: 956px;         /* iPhone 16 Pro Max height */
  margin: 0 auto;
  background: linear-gradient(180deg, #0b0b0d 0%, #070709 100%);
  padding: 84px 22px 34px;   /* top/bottom feel similar to iOS safe areas */
  box-sizing: border-box;
}

/* Center stack */
.stack {
  max-width: 360px;          /* content column like the screenshot */
  margin: 0 auto;
  text-align: center;
}

/* Logo */
.stack img {
  display: block;
  margin: 0 auto 18px auto;
}

/* Title + subtitle */
h1.title {
  margin: 0;
  color: #ffffff;
  font-size: 34px;
  font-weight: 800;
  letter-spacing: 0.2px;
}
p.subtitle {
  margin: 8px 0 28px 0;
  color: rgba(255,255,255,0.70);
  font-size: 14px;
}

/* Buttons base */
div.stButton > button {
  width: 100%;
  height: 54px;
  border-radius: 10px;
  font-weight: 800;
  letter-spacing: 0.8px;
  font-size: 14px;
}

/* SIGN UP (filled purple) */
.primary div.stButton > button {
  background: #c56bff !important;
  color: #0b0b0d !important;
  border: 1px solid #c56bff !important;
}
.primary div.stButton > button:hover { filter: brightness(1.04); }

/* Divider */
.divider {
  margin: 22px 0;
  height: 1px;
  background: rgba(255,255,255,0.14);
}

/* LOGIN (outlined purple) */
.secondary div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1.5px solid #c56bff !important;
}
.secondary div.stButton > button:hover {
  background: rgba(197,107,255,0.08) !important;
}

/* Make it responsive on non-phone screens */
@media (max-width: 460px) {
  .screen { width: 100%; min-height: 100vh; border-radius: 0; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- UI ----------
st.markdown('<div class="screen"><div class="stack">', unsafe_allow_html=True)

# Put your icon/logo here
# Repo structure:
#   assets/logo.png
st.image("assets/logo.png", width=70)

st.markdown(
    """
    <h1 class="title">Brooze</h1>
    <p class="subtitle">Bar hopping just got more rewarding</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="primary">', unsafe_allow_html=True)
st.button("SIGN UP")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="secondary">', unsafe_allow_html=True)
st.button("LOGIN")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)
