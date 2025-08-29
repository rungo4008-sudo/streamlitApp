import streamlit as st
from streamlit import page_link
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components
from streamlit.components.v1 import html


st.set_page_config(
    page_title="Rungo's Portfolio",
    page_icon="🛡",
    layout="wide",
)



st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)




st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    position: relative;
    background-color: #000; 
    overflow: hidden;
}


[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top:0; left:0; right:0; bottom:0;
    background-image: radial-gradient(#39ff14 1px, transparent 1px);
    background-size: 15px 15px; 
    opacity: 0.5;
    z-index: 0;
    pointer-events: none;
    animation: moveMesh 20s linear infinite, twinkle 1.5s ease-in-out infinite;
}


@keyframes moveMesh {
    0% { background-position: 0 0; }
    100% { background-position: 400px 400px; }
}


@keyframes twinkle {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 0.4; }
}


.stApp > .main {
    position: relative;
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)





st.title("Welcome! 👨‍💻")
st.write("Hi my name is **rungo** I'm a passionate programmer with a broad interest in technology. I enjoy exploring different areas without limiting myself to a single field 🚀")
import streamlit as st

import streamlit as st
st.subheader("General Skills ")
st.markdown("""
<style>
.skill {
    margin: 10px 0;
}
.bar {
    background: #E1D9D1;  
    border-radius: 10px;
    overflow: hidden;
    height: 22px;
}
.fill {
    background: linear-gradient(90deg, #013220, #9bbf9c); 
    height: 100%;
    text-align: right;
    padding-right: 6px;
    color: #000000;
    font-weight: 500;
    font-size: 12px;
}
</style>

<div class="skill">
  <p>Python</p>
  <div class="bar"><div class="fill" style="width:55%;">55%</div></div>
</div>

<div class="skill">
  <p>Java</p>
  <div class="bar"><div class="fill" style="width:60%;">60%</div></div>
</div>

<div class="skill">
  <p>Problem Solving</p>
  <div class="bar"><div class="fill" style="width:85%;">85%</div></div>
</div>
""", unsafe_allow_html=True)


st.subheader("💻 Digital Forensics & Cybersecurity Skills")

st.write("""
- **Digital Forensics:** Experienced in using tools like **Autopsy** and **FTK Imager** for disk and file analysis.  
- **Password Recovery:** Knowledge of **password cracking** techniques using **brute force** methods for educational purposes only.  
- **Steganography:** Practical experience in detecting and analyzing hidden data within images, audio, and other media.  
- **Data Analysis & Investigation:** Skilled in examining digital evidence and extracting relevant information safely and responsibly.  
""")

st.subheader("🔒 Cybersecurity & Programming Experiments")

st.write("""
- **Screen Logger (Educational)** – Learned how to capture periodic screenshots and organize them into folders. For learning purposes only.

- **Keylogger Simulation (Educational)** – Learned how keyboard events are handled in Python. 
  For learning purposes only.

- **Encrypted Password Generator** – Generates secure passwords and stores them in a file encrypted using **Base64 encoding**.
  Focused on encryption, file handling, and security best practices.
""")




st.title("Contact Me")

import streamlit as st

st.markdown("""
<style>
.icon-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    margin: 10px;
    border-radius: 50%;
    background-color: #111;
    transition: transform 0.3s, box-shadow 0.3s;
}
.icon-btn img {
    width: 30px;
    height: 30px;
}
.icon-btn:hover {
    transform: scale(1.15);
    box-shadow: 0 0 20px #39ff14;
}
</style>

<div style="text-align:center;">
    <a class="icon-btn" href="https://discord.com/users/695577291496882186" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111370.png"/>
    </a>
    <a class="icon-btn" href="https://www.instagram.com/fearhiro/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png"/>
    </a>
</div>
""", unsafe_allow_html=True)





