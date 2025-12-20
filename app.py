import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Brooze", page_icon="🍸", layout="centered")

# -------------------------
# STATE
# -------------------------
if "route" not in st.session_state:
    st.session_state.route = "landing"  # landing | signup | login

# -------------------------
# STYLES: iPhone 16 Pro Max canvas (portrait)
# CSS logical size: 440 x 956
# -------------------------
st.markdown(
    """
<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding-top: 0.5rem; padding-bottom: 0.5rem; }

/* Outside background (like the desktop page behind the phone) */
.stApp { background: #050506; }

/* iPhone 16 Pro Max "screen" */
.mobile {
  width: 440px;
  min-height: 956px;
  margin: 0 auto;
  background: linear-gradient(180deg, #0b0b0d 0%, #070709 100%);
  border-radius: 36px;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 18px 70px rgba(0,0,0,0.6);

  /* Safe areas */
  padding-top: 64px;     /* Dynamic Island safe space */
  padding-bottom: 36px;  /* Home indicator safe space */
  padding-left: 24px;
  padding-right: 24px;

  display: flex;
  flex-direction: column;
}

/* Center section */
.center { text-align: center; }

/* Headline + subtitle */
h1.title {
  margin: 0;
  font-size: 36px;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.3px;
}
p.subtitle {
  margin: 10px 0 32px 0;
  font-size: 15px;
  color: rgba(255,255,255,0.70);
}

/* Form header */
h2.pageTitle {
  margin: 0 0 10px 0;
  font-size: 26px;
  font-weight: 800;
  color: #ffffff;
}
p.pageSub {
  margin: 0 0 18px 0;
  color: rgba(255,255,255,0.7);
  font-size: 14px;
}

/* Buttons */
div.stButton > button {
  width: 100%;
  height: 56px;
  border-radius: 14px;
  font-weight: 800;
  letter-spacing: 0.8px;
  font-size: 15px;
}

/* Primary button */
.filled div.stButton > button {
  background: #c56bff !important;
  color: #0b0b0d !important;
  border: 1px solid #c56bff !important;
}
.filled div.stButton > button:hover {
  filter: brightness(1.05);
}

/* Divider */
.divider {
  margin: 22px 0;
  height: 1px;
  background: rgba(255,255,255,0.12);
}

/* Secondary (outlined) button */
.outlined div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1px solid #c56bff !important;
}
.outlined div.stButton > button:hover {
  background: rgba(197,107,255,0.08) !important;
}

/* Inputs: better contrast on dark */
label, .stTextInput label, .stPasswordInput label {
  color: rgba(255,255,255,0.75) !important;
}
div[data-baseweb="input"] input {
  background: rgba(255,255,255,0.06) !important;
  color: #fff !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
}
div[data-baseweb="input"] input:focus {
  border: 1px solid rgba(197,107,255,0.9) !important;
  box-shadow: 0 0 0 2px rgba(197,107,255,0.25) !important;
}

/* Form submit button uses same sizing */
div[data-testid="stFormSubmitButton"] button {
  width: 100% !important;
  height: 56px !important;
  border-radius: 14px !important;
  font-weight: 800 !important;
  letter-spacing: 0.8px !important;
  font-size: 15px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------
# UI HELPERS
# -------------------------
def goto(route: str):
    st.session_state.route = route
    st.rerun()


# -------------------------
# SCREENS
# -------------------------
def landing():
    st.markdown('<div class="mobile">', unsafe_allow_html=True)
    st.markdown('<div class="center">', unsafe_allow_html=True)

    # Logo
    st.image("assets/logo.png", width=72)

    # Title + subtitle
    st.markdown(
        """
        <h1 class="title">Brooze</h1>
        <p class="subtitle">Bar hopping just got more rewarding</p>
        """,
        unsafe_allow_html=True,
    )

    # Buttons
    st.markdown('<div class="filled">', unsafe_allow_html=True)
    if st.button("SIGN UP"):
        goto("signup")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("LOGIN"):
        goto("login")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # center
    st.markdown("</div>", unsafe_allow_html=True)  # mobile


def signup():
    st.markdown('<div class="mobile">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="center">
          <h2 class="pageTitle">Create account</h2>
          <p class="pageSub">Join Brooze in under a minute</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("signup_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("SIGN UP")
        if submitted:
            # Demo behavior (replace with real auth/DB)
            if not name or not email or not password:
                st.error("Please fill out all fields.")
            else:
                st.success("Account created (demo).")
                goto("landing")

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("Back"):
        goto("landing")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # mobile


def login():
    st.markdown('<div class="mobile">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="center">
          <h2 class="pageTitle">Welcome back</h2>
          <p class="pageSub">Log in to keep earning rewards</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("LOGIN")
        if submitted:
            # Demo behavior (replace with real auth check)
            if not email or not password:
                st.error("Please enter email and password.")
            else:
                st.success("Logged in (demo).")
                goto("landing")

    st.markdown('<div class="outlined">', unsafe_allow_html=True)
    if st.button("Back"):
        goto("landing")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # mobile


# -------------------------
# ROUTER
# -------------------------
if st.session_state.route == "landing":
    landing()
elif st.session_state.route == "signup":
    signup()
else:
    login()
