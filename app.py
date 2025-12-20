import streamlit as st

st.set_page_config(page_title="Brooze", layout="centered")

# ---- STATE ----
if "route" not in st.session_state:
    st.session_state.route = "landing"

# ---- STYLES ----
st.markdown(
    """
<style>
/* Hide Streamlit chrome */
#MainMenu, header, footer { visibility: hidden; }

/* App background */
.stApp {
  background: #050506;
}

/* iPhone 16 Pro Max frame */
.mobile {
  width: 440px;           /* iPhone 16 Pro Max width */
  min-height: 956px;      /* iPhone 16 Pro Max height */
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

/* Centered content */
.center {
  text-align: center;
}

/* Logo */
.center img {
  display: block;
  margin: 0 auto 20px auto;
}

/* Title */
h1.title {
  margin: 0;
  font-size: 36px;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.3px;
}

/* Subtitle */
p.subtitle {
  margin: 10px 0 32px 0;
  font-size: 15px;
  color: rgba(255,255,255,0.7);
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

/* Divider */
.divider {
  margin: 22px 0;
  height: 1px;
  background: rgba(255,255,255,0.12);
}

/* Secondary button */
.outlined div.stButton > button {
  background: transparent !important;
  color: #c56bff !important;
  border: 1px solid #c56bff !important;
}
</style>
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
