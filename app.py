import streamlit as st

st.set_page_config(page_title="Brooze", layout="centered")

# ---- STATE ----
if "route" not in st.session_state:
    st.session_state.route = "landing"

# ---- STYLES ----
st.markdown(
    """
<style>
.stApp {
  background: linear-gradient(180deg, #0b0b0d 0%, #0a0a0c 100%);
}

.container {
  max-width: 360px;
  margin: 0 auto;
  padding-top: 90px;
  text-align: center;
}

/* Logo */
.logo {
  width: 64px;
  margin: 0 auto 20px auto;
}

/* Text */
h1.title {
  margin: 0;
  color: #ffffff;
  font-size: 34px;
  font-weight: 800;
}
p.subtitle {
  margin: 8px 0 28px 0;
  color: rgba(255,255,255,0.7);
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

.filled div.stButton > button {
  background: #c56bff !important;
  color: #0b0b0d !important;
  border: 1px solid #c56bff !important;
}

.outlined div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1px solid #c56bff !important;
}

.divider {
  margin: 18px 0;
  height: 1px;
  background: rgba(255,255,255,0.12);
}
</style>
""",
    unsafe_allow_html=True,
)

# ---- SCREENS ----
def landing():
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Logo
    st.image("assets/logo.png", width=64)

    st.markdown(
        """
        <h1 class="title">Brooze</h1>
        <p class="subtitle">Bar hopping just got more rewarding</p>
        """,
        unsafe_allow_html=True,
    )

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

    with st.form("signup"):
        st.text_input("Name")
        st.text_input("Email")
        st.text_input("Password", type="password")
        if st.form_submit_button("SIGN UP"):
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

    with st.form("login"):
        st.text_input("Email")
        st.text_input("Password", type="password")
        if st.form_submit_button("LOGIN"):
            st.session_state.route = "landing"
            st.rerun()

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("Back"):
        st.session_state.route = "landing"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ---- ROUTER ----
if st.session_state.route == "landing":
    landing()
elif st.session_state.route == "signup":
    signup()
else:
    login()
