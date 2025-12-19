import streamlit as st

st.set_page_config(page_title="Brooze", page_icon="🍷", layout="centered")

# --- STATE ---
if "route" not in st.session_state:
    st.session_state.route = "landing"  # landing | signup | login

# --- STYLES (match the screenshot vibe) ---
st.markdown(
    """
<style>
/* Page background */
.stApp {
  background: linear-gradient(180deg, #0b0b0d 0%, #0a0a0c 100%);
}

/* Center everything and control width */
.container {
  max-width: 360px;
  margin: 0 auto;
  padding-top: 90px;
  text-align: center;
}

/* Icon */
.icon-wrap {
  width: 70px;
  height: 70px;
  margin: 0 auto 16px auto;
  display: grid;
  place-items: center;
}
.icon {
  font-size: 44px;
  line-height: 1;
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

/* Buttons */
div.stButton > button {
  width: 100%;
  height: 48px;
  border-radius: 10px;
  font-weight: 700;
  letter-spacing: 0.6px;
}

/* Filled (SIGN UP) button — we’ll apply via a wrapper class */
.filled div.stButton > button {
  background: #c56bff !important;
  color: #0b0b0d !important;
  border: 1px solid #c56bff !important;
}
.filled div.stButton > button:hover {
  filter: brightness(1.05);
}

/* Outlined (LOGIN) button — wrapper class */
.outlined div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1px solid #c56bff !important;
}
.outlined div.stButton > button:hover {
  background: rgba(197,107,255,0.08) !important;
}

/* Divider line */
.divider {
  margin: 18px 0;
  height: 1px;
  background: rgba(255,255,255,0.12);
}

/* Form labels */
label, .stTextInput label, .stPasswordInput label {
  color: rgba(255,255,255,0.75) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --- ROUTES ---
def landing():
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Icon (simple emoji substitute for the pin-glass logo)
    st.markdown(
        """
        <div class="icon-wrap">
          <div class="icon">📍</div>
        </div>
        <h1 class="title">Brooze</h1>
        <p class="subtitle">Bar hopping just got more rewarding</p>
        """,
        unsafe_allow_html=True,
    )

    # Buttons
    st.markdown('<div class="filled">', unsafe_allow_html=True)
    if st.button("SIGN UP"):
        st.session_state.route = "signup"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("LOGIN"):
        st.session_state.route = "login"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def signup():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">Create account</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Join Brooze in under a minute</p>', unsafe_allow_html=True)

    with st.form("signup_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        pwd = st.text_input("Password", type="password")
        submitted = st.form_submit_button("SIGN UP")
        if submitted:
            # Replace with real auth (DB, Firebase, etc.)
            st.success(f"Signed up (demo): {name} / {email}")
            st.session_state.route = "landing"
            st.rerun()

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.route = "landing"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def login():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">Welcome back</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Log in to keep earning rewards</p>', unsafe_allow_html=True)

    with st.form("login_form"):
        email = st.text_input("Email")
        pwd = st.text_input("Password", type="password")
        submitted = st.form_submit_button("LOGIN")
        if submitted:
            # Replace with real auth check
            st.success(f"Logged in (demo): {email}")
            st.session_state.route = "landing"
            st.rerun()

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.route = "landing"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# --- RENDER ---
route = st.session_state.route
if route == "landing":
    landing()
elif route == "signup":
    signup()
else:
    login()

