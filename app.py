import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ink & Silence",
    page_icon="📜",
    layout="centered"
)

# ----------------- STYLE -----------------
st.markdown("""
<style>

.stApp {
    background-color: #f6f1e7;  /* warm paper */
    color: #2b2b2b;
    font-family: "Georgia", serif;
}

/* Title */
h1 {
    text-align: center;
    color: #3b2f2f;
    font-weight: 400;
    letter-spacing: 1px;
}

/* Shayari card */
.poem {
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid #e6dccf;
    padding: 22px;
    border-radius: 12px;
    margin-bottom: 18px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
}

/* Shayari text */
.text {
    font-size: 20px;
    line-height: 1.8;
    color: #2f2a26;
    white-space: pre-wrap;
}

/* Author */
.author {
    text-align: right;
    margin-top: 10px;
    font-style: italic;
    color: #6b5e55;
    font-size: 14px;
}

/* tiny separator like journal ink mark */
.sep {
    text-align: center;
    color: #c9b8a8;
    margin: 10px 0;
}

</style>
""", unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.title("Ink & Silence")

st.markdown("""
<div style='text-align:center; color:#6b5e55; margin-top:-10px'>
A collection of shayari that stayed when everything else passed.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------- LOAD DATA -----------------
df = pd.read_csv("shayari.csv")

# ----------------- DISPLAY -----------------
for _, row in df.iterrows():

    st.markdown(f"""
    <div class="poem">
        <div class="text">{row['shayari']}</div>
        <div class="sep">✦ ✦ ✦</div>
        <div class="author">— {row['author']}</div>
    </div>
    """, unsafe_allow_html=True)
