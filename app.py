import streamlit as st
import pandas as pd
import base64

st.set_page_config(
    page_title="Between Lines",
    page_icon="🌙",
    layout="centered"
)

# ---------------- BACKGROUND IMAGE (for sparkle illusion) ----------------
def add_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f3eadc;
            font-family: Georgia, serif;
            color: #2b2b2b;
        }

        /* soft floating glow effect (works in Streamlit) */
        .stApp::after {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            background: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.35), transparent 40%),
                        radial-gradient(circle at 80% 30%, rgba(255,215,160,0.25), transparent 45%),
                        radial-gradient(circle at 50% 80%, rgba(255,255,255,0.2), transparent 50%);
            animation: floatGlow 10s ease-in-out infinite alternate;
        }

        @keyframes floatGlow {
            0% { transform: scale(1) translateY(0px); }
            100% { transform: scale(1.05) translateY(-10px); }
        }

        .poem {
            background: rgba(255,255,255,0.6);
            border: 1px solid #e7dccb;
            padding: 22px;
            border-radius: 14px;
            margin-bottom: 18px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.05);
            backdrop-filter: blur(2px);
        }

        .text {
            font-size: 22px;
            line-height: 2.3;
            white-space: pre-wrap;
            color: #2c2520;
        }

        .author {
            text-align: right;
            margin-top: 12px;
            color: #7a6656;
            font-style: italic;
        }

        .intro {
            text-align: center;
            margin-top: 25px;
            margin-bottom: 35px;
            color: #5a4a3b;
            line-height: 2;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# ---------------- INTRO ----------------
st.markdown("""
<div class="intro">
For people that I met ·  
For the people I lost ·  
And for everything that I felt ·  
between the lines ·
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD CSV (UTF-8 FIX) ----------------
df = pd.read_csv("shayari.csv", encoding="utf-8")

# ---------------- DISPLAY ----------------
for _, row in df.iterrows():

    shayari = str(row["shayari"]).replace("\\n", "\n")

    st.markdown(f"""
    <div class="poem">
        <div class="text">{shayari}</div>
        <div class="author">— {row['author']}</div>
    </div>
    """, unsafe_allow_html=True)
