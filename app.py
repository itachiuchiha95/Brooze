import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Brooze – Auth",
    page_icon="🍷",
    layout="centered",
)

# ---------- Custom CSS ----------
iphone_width = 430   # approx "points" for iPhone 16 Pro Max logical width
iphone_height = 932  # safe-ish height for browser viewport

st.markdown(
    f"""
    <style>
    body {{
        background-color: #000000;
    }}

    /* Center the phone frame */
    .app-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000000;
    }}

    .phone-frame {{
        width: {iphone_width}px;
        height: {iphone_height}px;
        background-color: #000000;
        border-radius: 36px;
        box-shadow: 0 0 40px rgba(0,0,0,0.6);
        border: 1px solid #222222;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .screen {{
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
    }}

    .logo-section {{
        margin
