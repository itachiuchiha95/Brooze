import streamlit as st

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Brooze",
    page_icon="🍸",
    layout="centered"
)

# ----- BASIC STYLES -----
st.markdown(
    """
    <style>
    /* Overall page */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
    }

    /* Center everything vertically */
    .main-block {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Logo icon */
    .logo-icon {
        font-size: 64px;
        color: #C86BFF; /* purple */
        margin-bottom: 16px;
    }

    .app-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .subtitle {
        font-size: 14px;
        color: #CCCCCC;
        margin-bottom: 48px;
    }

    /* Buttons container: max "phone" width */
    .phone-width {
        width: 100%;
        max-width: 360px;
        padding: 0 16px;
        box-sizing: border-box;
    }

    /* Primary button */
    .primary-btn {
        width: 100%;
        padding: 14px 0;
        border-radius: 4px;
        border: none;
        background-color: #C86BFF;
        color: #FFFFFF;
        font-weight: 600;
        text-align: center;
        margin-bottom: 24px;
        cursor: pointer;
    }

    /* Divider line */
    .divider {
        width: 100%;
        border-top: 1px solid #333333;
        margin-bottom: 24px;
    }

    /* Secondary (outline) button */
    .secondary-btn {
        width: 100%;
        padding: 14px 0;
        border-radius: 4px;
        border: 2px solid #C86BFF;
        background-color: transparent;
        color: #C86BFF;
        font-weight: 600;
        text-align: center;
        cursor: pointer;
    }

    /* Remove Streamlit default padding/margins for a tighter mobile feel */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----- LAYOUT -----
st.markdown('<div class="main-block">', unsafe_allow_html=True)

# Logo + title + subtitle
st.markdown(
    """
    <div style="text-align: center;">
        <!-- Simple glass + pin glyph using emoji; swap with SVG later if desired -->
        <div class="logo-icon">🍸</div>
        <div class="app-title">Brooze</div>
        <div class="subtitle">Bar hopping just got more rewarding</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Buttons area in "phone" width
st.markdown('<div class="phone-width">', unsafe_allow_html=True)

# Using html buttons so we can control styling; you’d wire these up later
signup_clicked = st.button("SIGN UP", key="signup", use_container_width=True)
login_clicked = False  # placeholder

# Replace default button with styled HTML block
st.markdown(
    """
    <button class="primary-btn">SIGN UP</button>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <button class="secondary-btn">LOGIN</button>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)  # close phone-width
st.markdown('</div>', unsafe_allow_html=True)  # close main-block

# ----- INTERACTIONS (LOGIC PLACEHOLDER) -----
# In real usage, you’d use st.button for interaction and navigate or show forms.
# For example:
# if signup_clicked:
#     st.session_state['screen'] = 'signup'
# if login_clicked:
#     st.session_state['screen'] =
