import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Brooze",
    page_icon="🍸",
    layout="centered",
)

# ---------- Custom styles ----------
st.markdown(
    """
    <style>
        body {
            background-color: #000000;
        }
        .main {
            background-color: #000000;
        }
        .brooze-title {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            color: #FFFFFF;
            text-align: center;
            font-size: 28px;
            font-weight: 600;
            margin-top: 24px;
        }
        .brooze-subtitle {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            color: #B3B3B3;
            text-align: center;
            font-size: 14px;
            margin-top: 4px;
            margin-bottom: 40px;
        }
        .icon-circle {
            width: 80px;
            height: 80px;
            border-radius: 40px;
            border: 2px solid #C95CFF;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 80px auto 0 auto;
        }
        .icon-glass {
            font-size: 40px;
            color: #C95CFF;
        }
        .primary-btn button {
            width: 100%;
            border-radius: 6px;
            height: 52px;
            background-color: #C95CFF !important;
            color: #000000 !important;
            border: none !important;
            font-weight: 600;
        }
        .secondary-btn button {
            width: 100%;
            border-radius: 6px;
            height: 52px;
            background-color: transparent !important;
            color: #C95CFF !important;
            border: 1.5px solid #C95CFF !important;
            font-weight: 600;
        }
        hr {
            border: none;
            border-top: 1px solid #262626;
            margin: 32px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Layout ----------
# Centered column
col = st.container()

with col:
    # Icon
    st.markdown(
        """
        <div class="icon-circle">
            <span class="icon-glass">🍸</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Title & subtitle
    st.markdown('<div class="brooze-title">Brooze</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="brooze-subtitle">Bar hopping just got more rewarding</div>',
        unsafe_allow_html=True,
    )

    # Primary button (SIGN UP)
    signup = st.container()
    with signup:
        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        sign_up_clicked = st.button("SIGN UP")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Secondary button (LOGIN)
    login = st.container()
    with login:
        st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
        login_clicked = st.button("LOGIN")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- Button handlers ----------
if sign_up_clicked:
    st.success("Sign up tapped (wire this to your sign-up flow).")

if login_clicked:
    st.info("Login tapped (wire this to your login flow).")
