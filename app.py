import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Between Lines",
    page_icon="",
    layout="centered"
)

# ---------------- BACKGROUND + SPARKLE EFFECT ----------------
st.markdown("""
<style>

/* soft brown paper background */
.stApp {
    background: #f3eadc;
    color: #2b2b2b;
    font-family: "Georgia", serif;
    overflow-x: hidden;
}

/* floating sparkles layer */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background: transparent;
    background-image: radial-gradient(#c9a86a 1px, transparent 1px),
                      radial-gradient(#ffffff 1px, transparent 1px);
    background-size: 60px 60px, 90px 90px;
    background-position: 0 0, 30px 30px;
    animation: sparkleMove 18s linear infinite;
    opacity: 0.25;
}

@keyframes sparkleMove {
    0% { transform: translateY(0px); }
    100% { transform: translateY(-80px); }
}

/* intro text */
.intro {
    text-align: center;
    font-size: 16px;
    color: #5a4a3b;
    margin-top: 30px;
    margin-bottom: 40px;
    line-height: 2;
}

/* shayari block */
.poem {
    background: rgba(255,255,255,0.55);
    border: 1px solid #e7dccb;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    backdrop-filter: blur(2px);
}

/* Urdu text styling */
.text {
    font-size: 22px;
    line-height: 2.2;
    color: #2c2520;
    white-space: pre-wrap;   /* IMPORTANT: keeps Urdu line breaks */
    font-style: italic;
    direction: auto;
}

/* author */
.author {
    text-align: right;
    margin-top: 12px;
    font-style: italic;
    color: #7a6656;
}

/* divider */
.sep {
    text-align: center;
    color: #c8b7a3;
    margin-top: 10px;
    margin-bottom: 5px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- INTRO (NO TITLE) ----------------
st.markdown("""
<div class="intro">
For people that I met ·  
For the people I lost ·  
And for everything that I felt ·  
between the lines ·
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("shayari.csv")

# ---------------- DISPLAY SHAYARI ----------------
for _, row in df.iterrows():

    st.markdown(f"""
    <div class="poem">
        <div class="text">{row['shayari']}</div>
        <div class="sep">✦</div>
        <div class="author">— {row['author']}</div>
    </div>
    """, unsafe_allow_html=True)
