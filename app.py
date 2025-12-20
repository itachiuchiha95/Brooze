import streamlit as st

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Brooze", page_icon="🍸", layout="centered")

# -------------------------
# STYLES (matches the image: full screen, no phone frame, centered stack)
# -------------------------
st.markdown(
    """
<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Full-screen dark background */
.stApp {
  background: #050506;
}

/* Full-viewport centering */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;     /* vertical center */
  justify-content: center; /* horizontal center */
  padding: 48px 18px;      /* mobile-friendly side padding */
  box-sizing: border-box;
}

/* The actual content column (like a mobile screen width) */
.card {
  width: 100%;
  max-width: 360px;
  text-align: center;
}

/* Logo spacing */
.card img {
  display: block;
  margin: 0 auto 18px auto;
}

/* Title + subtitle */
h1.title {
  margin: 0;
  color: #ffffff;
  font-size: 36px;
  font-weight: 800;
  letter-spacing: 0.2px;
}
p.subtitle {
  margin: 10px 0 30px 0;
  color: rgba(255,255,255,0.70);
  font-size: 14px;
}

/* Buttons */
div.stButton > button {
  width: 100%;
  height: 54px;
  border-radius: 14px;
  font-weight: 800;
  letter-spacing: 0.8px;
  font-size: 15px;
}

/* SIGN UP filled */
.filled div.stButton > button {
  background: #c56bff !important;
  color: #0b0b0d !important;
  border: 1px solid #c56bff !important;
}
.filled div.stButton > button:hover {
  filter: brightness(1.05);
}

/* Divider line */
.divider {
  margin: 20px 0;
  height: 1px;
  background: rgba(255,255,255,0.12);
}

/* LOGIN outlined */
.outlined div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1px solid #c56bff !important;
}
.outlined div.stButton > button:hover {
  background: rgba(197,107,255,0.08) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------
# LAYOUT (exact landing screen)
# -------------------------
st.markdown('<div class="hero"><div class="card">', unsafe_allow_html=True)

# Your logo file here
st.image("assets/logo.png", width=72)

st.markdown(
    """
    <h1 class="title">Brooze</h1>
    <p class="subtitle">Bar hopping just got more rewarding</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="filled">', unsafe_allow_html=True)
st.button("SIGN UP", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div class="outlined">', unsafe_allow_html=True)
st.button("LOGIN", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)
