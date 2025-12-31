import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Brooze – Auth",
    page_icon="🍷",
    layout="centered",
)

# Approx iPhone 16 Pro Max logical size (you can tweak these)
iphone_width = 430
iphone_height = 932

# ---------- Custom CSS ----------
css = """
<style>
body {
    background-color: #000000;
}

/* Center the phone frame */
.app-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #000000;
}

.phone-frame {
    width: {iphone_width}px;
    height: {iphone_height}px;
    background-color: #000000;
    border-radius: 36px;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
    border: 1px solid #222222;
    display: flex;
    justify-content: center;
    align-items: center;
}

.screen {
    width: 100%;
    height: 100%;
    padding: 40px 32px 40px 32px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: flex-start;
    color: #FFFFFF;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
                 "Segoe UI", sans-serif;
}

.logo-section {
    margin-top: 80px;
    text-align: center;
    margin-bottom: 120px;
}

.logo-icon {
    font-size: 60px;
    color: #D46BFF;
    margin-bottom: 16px;
}

.app-name {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 4px;
}

.tagline {
    font-size: 14px;
    color: #B5B5B5;
}

.btn-primary {
    width: 100%;
    background-color: #D46BFF;
    color: #000000;
    border-radius: 8px;
    padding: 16px 0;
    text-align: center;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    border: none;
    margin-bottom: 24px;
    cursor: pointer;
}

.divider {
    width: 100%;
    height: 1px;
    background-color: #333333;
    margin-bottom: 24px;
}

.btn-secondary {
    width: 100%;
    background-color: transparent;
    color: #D46BFF;
    border-radius: 8px;
    padding: 16px 0;
    text-align: center;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    border: 1px solid #D46BFF;
    cursor: pointer;
}

/* Hide default Streamlit chrome */
header[data-testid="stHeader"] {
    display: none;
}
footer {
    visibility: hidden;
}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: none;
}
</style>
""".format(iphone_width=iphone_width, iphone_height=iphone_height)

st.markdown(css, unsafe_allow_html=True)

# ---------- Layout HTML ----------
html = """
<div class="app-container">
  <div class="phone-frame">
    <div class="screen">
      <div class="logo-section">
        <div class="logo-icon">🥂</div>
        <div class="app-name">Brooze</div>
        <div class="tagline">Bar hopping just got more rewarding</div>
      </div>

      <div style="flex:1;"></div>

      <button class="btn-primary">Sign Up</button>
      <div class="divider"></div>
      <button class="btn-secondary">Login</button>

      <div style="flex:1;"></div>
    </div>
  </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
