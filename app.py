import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="A Window Into My Soul",
    page_icon="🌙",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
}

h1,h2,h3,p {
    color: white;
}

.poem-box {
    background-color: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    margin-top: 15px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

.quote {
    color: white;
    font-size: 22px;
    line-height: 1.9;
}

.author {
    color: #cbd5e1;
    text-align: right;
    font-style: italic;
}

.reflection {
    color: #f8fafc;
    margin-top: 15px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

st.title("🌙 A Window Into My Soul")

st.markdown("""
These are not necessarily the greatest shayaris ever written.

They are the ones that stayed.

The ones that understood me before I understood myself.
""")

st.divider()

df = pd.read_csv("shayari.csv")

if len(df) > 0:

    poem = df.sample(1).iloc[0]

    st.subheader("✨ Shayari of the Visit")

    st.markdown(
        f"""
        <div class='poem-box'>
        <div class='quote'>
        {poem['shayari']}
        </div>
        <br>
        <div class='author'>
        — {poem['author']}
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.header("Browse My Collection")

categories = ["All"] + sorted(df["category"].dropna().unique().tolist())

selected = st.selectbox(
    "Choose a chapter",
    categories
)

if selected != "All":
    display_df = df[df["category"] == selected]
else:
    display_df = df

for _, row in display_df.iterrows():

    st.markdown(
        f"""
        <div class='poem-box'>
        <div class='quote'>
        {row['shayari']}
        </div>

        <br>

        <div class='author'>
        — {row['author']}
        </div>

        <div class='reflection'>
        💭 {row['reflection']}
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.header("About This Collection")

st.write("""
Every poem here has left a mark on me.

Some describe people I met.

Some describe people I lost.

Some describe versions of myself.

Together they tell a story I could never tell directly.
""")
