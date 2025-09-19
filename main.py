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
    background: linear-gradient(-45deg, #0f1419, #1a202c, #2d3748, #1e2d3d, #0d1421, #1c2331);
    background-size: 400% 400%;
    overflow: hidden;
    animation: gradientShift 20s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        radial-gradient(circle at 20% 20%, rgba(100, 200, 255, 0.08) 2px, transparent 2px),
        radial-gradient(circle at 80% 80%, rgba(120, 180, 255, 0.06) 1px, transparent 1px),
        radial-gradient(circle at 40% 40%, rgba(90, 170, 240, 0.04) 3px, transparent 3px),
        radial-gradient(circle at 60% 60%, rgba(110, 190, 250, 0.05) 2px, transparent 2px);
    background-size: 120px 120px, 180px 180px, 100px 100px, 140px 140px;
    opacity: 0.4;
    z-index: 0;
    pointer-events: none;
    animation: floatShapes 25s linear infinite;
}

@keyframes floatShapes {
    0% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(-20px, -20px) rotate(120deg); }
    66% { transform: translate(20px, -15px) rotate(240deg); }
    100% { transform: translate(0, 0) rotate(360deg); }
}

[data-testid="stAppViewContainer"]::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: 
        linear-gradient(45deg, transparent 40%, rgba(100, 150, 200, 0.02) 50%, transparent 60%),
        linear-gradient(-45deg, transparent 40%, rgba(80, 130, 180, 0.015) 50%, transparent 60%);
    z-index: 0;
    pointer-events: none;
    animation: shimmer 12s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 0.4; }
}

.stApp > .main {
    position: relative;
    z-index: 1;
}

.stApp .main .block-container {
    background: rgba(20, 30, 45, 0.8);
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 2.5rem;
    margin: 1rem;
    border: 1px solid rgba(100, 150, 200, 0.15);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(150, 200, 255, 0.1);
    animation: containerGlow 6s ease-in-out infinite;
}

@keyframes containerGlow {
    0%, 100% { 
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(150, 200, 255, 0.1),
            0 0 15px rgba(80, 150, 220, 0.1);
    }
    50% { 
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(150, 200, 255, 0.15),
            0 0 25px rgba(80, 150, 220, 0.15);
    }
}

.stApp h1, .stApp h2, .stApp h3 {
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
    color: #e2e8f0 !important;
}

.stApp p, .stApp div, .stApp span {
    color: rgba(226, 232, 240, 0.85) !important;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.stApp > .main::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        radial-gradient(circle at 15% 25%, rgba(80, 150, 220, 0.15) 0%, transparent 1%),
        radial-gradient(circle at 85% 75%, rgba(100, 170, 240, 0.12) 0%, transparent 1%),
        radial-gradient(circle at 45% 35%, rgba(90, 160, 230, 0.18) 0%, transparent 1%),
        radial-gradient(circle at 65% 15%, rgba(110, 180, 250, 0.10) 0%, transparent 1%),
        radial-gradient(circle at 85% 45%, rgba(70, 140, 210, 0.14) 0%, transparent 1%);
    background-size: 250px 250px, 300px 300px, 180px 180px, 280px 280px, 220px 220px;
    z-index: -1;
    pointer-events: none;
    animation: particleFloat 30s linear infinite;
}

@keyframes particleFloat {
    0% { transform: translateY(0) translateX(0); }
    25% { transform: translateY(-15px) translateX(8px); }
    50% { transform: translateY(-25px) translateX(-4px); }
    75% { transform: translateY(-12px) translateX(10px); }
    100% { transform: translateY(0) translateX(0); }
}
</style>
""", unsafe_allow_html=True)

st.title("Welcome! 👨‍💻")
st.write("Hi my name is **rungo** I'm a passionate programmer with a broad interest in technology. I enjoy exploring different areas without limiting myself to a single field 🚀")

st.subheader("General Skills ")
st.markdown("""
<style>
.skill {
    margin: 15px 0;
}
.bar {
    background: rgba(30, 40, 55, 0.8);  
    border-radius: 12px;
    overflow: hidden;
    height: 24px;
    border: 1px solid rgba(100, 150, 200, 0.2);
}
.fill {
    background: linear-gradient(90deg, #1e3a5f, #4a90c2, #6bb6d6); 
    height: 100%;
    text-align: right;
    padding-right: 8px;
    color: #ffffff;
    font-weight: 500;
    font-size: 13px;
    line-height: 24px;
    box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.1);
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

st.markdown("""
<style>
.icon-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    margin: 15px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(30, 45, 65, 0.9), rgba(20, 35, 55, 0.95));
    border: 2px solid rgba(100, 150, 200, 0.3);
    transition: all 0.4s ease;
    backdrop-filter: blur(10px);
}
.icon-btn img {
    width: 32px;
    height: 32px;
    filter: brightness(0.9) contrast(1.1);
}
.icon-btn:hover {
    transform: scale(1.1) translateY(-2px);
    box-shadow: 
        0 8px 25px rgba(80, 150, 220, 0.25),
        0 0 20px rgba(100, 170, 240, 0.15);
    border-color: rgba(120, 180, 240, 0.5);
    background: linear-gradient(135deg, rgba(40, 60, 80, 0.95), rgba(30, 50, 70, 1));
}
.icon-btn:hover img {
    filter: brightness(1.2) contrast(1.2);
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


