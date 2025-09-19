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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.main-title {
    font-family: 'Inter', sans-serif;
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e2e8f0, #cbd5e1, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin: 2rem 0;
    animation: titleGlow 3s ease-in-out infinite alternate, fadeInUp 1s ease-out;
    text-shadow: 0 0 30px rgba(148, 163, 184, 0.5);
}

@keyframes titleGlow {
    0% { 
        filter: brightness(1) drop-shadow(0 0 10px rgba(148, 163, 184, 0.3));
        transform: scale(1);
    }
    100% { 
        filter: brightness(1.2) drop-shadow(0 0 20px rgba(148, 163, 184, 0.6));
        transform: scale(1.02);
    }
}

@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}

.intro-text {
    font-family: 'Inter', sans-serif;
    font-size: 1.3rem;
    font-weight: 400;
    color: rgba(226, 232, 240, 0.9) !important;
    text-align: center;
    line-height: 1.8;
    margin: 2rem auto;
    max-width: 800px;
    padding: 1.5rem;
    background: rgba(30, 45, 70, 0.3);
    border-radius: 15px;
    border: 1px solid rgba(100, 150, 200, 0.2);
    backdrop-filter: blur(10px);
    animation: slideInFromLeft 1.2s ease-out 0.3s both;
    position: relative;
    overflow: hidden;
}

.intro-text::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.1), transparent);
    animation: shimmerText 2s ease-in-out infinite;
}

@keyframes shimmerText {
    0% { left: -100%; }
    100% { left: 100%; }
}

@keyframes slideInFromLeft {
    0% { opacity: 0; transform: translateX(-50px); }
    100% { opacity: 1; transform: translateX(0); }
}

.section-header {
    font-family: 'Inter', sans-serif;
    font-size: 2.2rem;
    font-weight: 600;
    background: linear-gradient(135deg, #f1f5f9, #e2e8f0, #cbd5e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 3rem 0 1.5rem 0;
    position: relative;
    animation: fadeInRight 1s ease-out 0.6s both;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, #4a90c2, #6bb6d6, transparent);
    border-radius: 2px;
    animation: underlineExpand 1.5s ease-out 1s both;
}

@keyframes fadeInRight {
    0% { opacity: 0; transform: translateX(30px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes underlineExpand {
    0% { width: 0; }
    100% { width: 120px; }
}

.skills-section {
    animation: fadeInUp 1s ease-out 0.9s both;
}
</style>

<div class="main-title">Welcome! 👨‍💻</div>

<div class="intro-text">
Hi my name is <strong>rungo</strong> I'm a passionate programmer with a broad interest in technology. I enjoy exploring different areas without limiting myself to a single field 🚀
</div>

<div class="section-header">General Skills</div>
<div class="skills-section">
""", unsafe_allow_html=True)
st.markdown("""
<style>
.skill {
    margin: 20px 0;
    opacity: 0;
    animation: skillFadeIn 0.8s ease-out forwards;
}

.skill:nth-child(2) { animation-delay: 0.2s; }
.skill:nth-child(3) { animation-delay: 0.4s; }
.skill:nth-child(4) { animation-delay: 0.6s; }

@keyframes skillFadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.skill p {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    font-weight: 500;
    color: #e2e8f0 !important;
    margin-bottom: 8px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.bar {
    background: rgba(30, 40, 55, 0.8);  
    border-radius: 12px;
    overflow: hidden;
    height: 28px;
    border: 1px solid rgba(100, 150, 200, 0.2);
    position: relative;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

.bar::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.05) 50%, transparent 70%);
    animation: barShimmer 2s ease-in-out infinite;
}

@keyframes barShimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.fill {
    background: linear-gradient(90deg, #1e3a5f, #4a90c2, #6bb6d6); 
    height: 100%;
    text-align: right;
    padding-right: 10px;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 14px;
    line-height: 28px;
    box-shadow: inset 0 1px 3px rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
    transition: width 2s ease-out;
}

.fill.animate-python { width: 55%; animation-delay: 0.7s; }
.fill.animate-java { width: 60%; animation-delay: 0.9s; }
.fill.animate-problem { width: 85%; animation-delay: 1.1s; }

.fill::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 2px;
    height: 100%;
    background: rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
    animation: fillGlow 1.5s ease-in-out infinite alternate;
}

@keyframes fillGlow {
    0% { opacity: 0.5; }
    100% { opacity: 1; }
</style>

<div class="skill">
  <p>Python</p>
  <div class="bar"><div class="fill animate-python">55%</div></div>
</div>

<div class="skill">
  <p>Java</p>
  <div class="bar"><div class="fill animate-java">60%</div></div>
</div>

<div class="skill">
  <p>Problem Solving</p>
  <div class="bar"><div class="fill animate-problem">85%</div></div>
</div>
</div>

<script>
setTimeout(function() {
    document.querySelectorAll('.fill').forEach(function(el, index) {
        setTimeout(function() {
            if (el.classList.contains('animate-python')) {
                el.style.width = '55%';
            } else if (el.classList.contains('animate-java')) {
                el.style.width = '60%';
            } else if (el.classList.contains('animate-problem')) {
                el.style.width = '85%';
            }
        }, index * 200);
    });
}, 1000);
</script>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header">💻 Digital Forensics & Cybersecurity Skills</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content-section" style="animation: fadeInUp 1s ease-out 1.2s both;">
<div class="skills-list">
<div class="skill-item">
<strong>Digital Forensics:</strong> Experienced in using tools like <strong>Autopsy</strong> and <strong>FTK Imager</strong> for disk and file analysis.
</div>
<div class="skill-item">
<strong>Password Recovery:</strong> Knowledge of <strong>password cracking</strong> techniques using <strong>brute force</strong> methods for educational purposes only.
</div>
<div class="skill-item">
<strong>Steganography:</strong> Practical experience in detecting and analyzing hidden data within images, audio, and other media.
</div>
<div class="skill-item">
<strong>Data Analysis & Investigation:</strong> Skilled in examining digital evidence and extracting relevant information safely and responsibly.
</div>
</div>
</div>

<style>
.content-section {
    background: rgba(30, 45, 70, 0.2);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid rgba(100, 150, 200, 0.15);
    backdrop-filter: blur(8px);
}

.skills-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.skill-item {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    color: rgba(226, 232, 240, 0.9) !important;
    padding: 1.2rem;
    background: rgba(20, 35, 55, 0.4);
    border-radius: 12px;
    border-left: 4px solid #4a90c2;
    transition: all 0.3s ease;
    animation: slideInFromRight 0.8s ease-out forwards;
    opacity: 0;
    position: relative;
    overflow: hidden;
}

.skill-item:nth-child(1) { animation-delay: 0.1s; }
.skill-item:nth-child(2) { animation-delay: 0.3s; }
.skill-item:nth-child(3) { animation-delay: 0.5s; }
.skill-item:nth-child(4) { animation-delay: 0.7s; }

@keyframes slideInFromRight {
    0% { opacity: 0; transform: translateX(30px); }
    100% { opacity: 1; transform: translateX(0); }
}

.skill-item:hover {
    transform: translateY(-2px);
    background: rgba(20, 35, 55, 0.6);
    border-left-color: #6bb6d6;
    box-shadow: 0 8px 25px rgba(74, 144, 194, 0.15);
}

.skill-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(74, 144, 194, 0.1), transparent);
    transition: left 0.5s ease;
}

.skill-item:hover::before {
    left: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header">🔒 Cybersecurity & Programming Experiments</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content-section" style="animation: fadeInUp 1s ease-out 1.5s both;">
<div class="experiments-list">
<div class="experiment-item">
<h4>Screen Logger (Educational)</h4>
<p>Learned how to capture periodic screenshots and organize them into folders. For learning purposes only.</p>
</div>
<div class="experiment-item">
<h4>Keylogger Simulation (Educational)</h4>
<p>Learned how keyboard events are handled in Python. For learning purposes only.</p>
</div>
<div class="experiment-item">
<h4>Encrypted Password Generator</h4>
<p>Generates secure passwords and stores them in a file encrypted using <strong>Base64 encoding</strong>. Focused on encryption, file handling, and security best practices.</p>
</div>
</div>
</div>

<style>
.experiments-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
}

.experiment-item {
    background: rgba(25, 40, 60, 0.5);
    border-radius: 15px;
    padding: 1.8rem;
    border: 1px solid rgba(100, 150, 200, 0.2);
    transition: all 0.4s ease;
    animation: popIn 0.6s ease-out forwards;
    opacity: 0;
    transform: scale(0.9);
    position: relative;
    overflow: hidden;
}

.experiment-item:nth-child(1) { animation-delay: 0.2s; }
.experiment-item:nth-child(2) { animation-delay: 0.4s; }
.experiment-item:nth-child(3) { animation-delay: 0.6s; }

@keyframes popIn {
    0% { opacity: 0; transform: scale(0.9) translateY(20px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}

.experiment-item:hover {
    transform: scale(1.02) translateY(-5px);
    box-shadow: 0 15px 35px rgba(74, 144, 194, 0.2);
    border-color: rgba(107, 182, 214, 0.4);
}

.experiment-item h4 {
    font-family: 'Inter', sans-serif;
    font-size: 1.3rem;
    font-weight: 600;
    color: #e2e8f0 !important;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #f1f5f9, #cbd5e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.experiment-item p {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    color: rgba(226, 232, 240, 0.8) !important;
    line-height: 1.6;
}

.experiment-item::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(74, 144, 194, 0.1), transparent);
    animation: rotate 4s linear infinite;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.experiment-item:hover::before {
    opacity: 1;
}

@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-header">Contact Me</div>
<div class="contact-container">
    <div class="contact-title">Let's connect and collaborate!</div>
    <div class="buttons-wrapper">
        <a class="icon-btn discord-btn" href="https://discord.com/users/695577291496882186" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111370.png" alt="Discord"/>
        </a>
        <a class="icon-btn instagram-btn" href="https://www.instagram.com/fearhiro/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram"/>
        </a>
    </div>
</div>

<style>
.contact-container {
    text-align: center;
    padding: 2rem;
    margin: 2rem 0;
    animation: fadeInUp 1s ease-out 1.8s both;
}

.contact-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.2rem;
    color: rgba(226, 232, 240, 0.8) !important;
    margin-bottom: 2rem;
}

.buttons-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.icon-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(30, 45, 65, 0.9), rgba(20, 35, 55, 0.95));
    border: 2px solid rgba(100, 150, 200, 0.3);
    transition: all 0.5s ease;
    backdrop-filter: blur(15px);
    position: relative;
    overflow: hidden;
    text-decoration: none;
    animation: bounceIn 0.8s ease-out forwards;
    opacity: 0;
}

.discord-btn { animation-delay: 0.2s; }
.instagram-btn { animation-delay: 0.4s; }

@keyframes bounceIn {
    0% { opacity: 0; transform: scale(0.3) translateY(50px); }
    50% { transform: scale(1.05) translateY(-10px); }
    70% { transform: scale(0.95) translateY(5px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}

.icon-btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(120, 180, 240, 0.3), transparent);
    transition: all 0.4s ease;
    transform: translate(-50%, -50%);
}

.icon-btn:hover::before {
    width: 100px;
    height: 100px;
}

.icon-btn img {
    width: 36px;
    height: 36px;
    filter: brightness(0.9) contrast(1.1);
    transition: all 0.3s ease;
    position: relative;
    z-index: 2;
}

.icon-btn:hover {
    transform: scale(1.15) translateY(-8px);
    box-shadow: 
        0 15px 35px rgba(80, 150, 220, 0.3),
        0 0 30px rgba(100, 170, 240, 0.2);
    border-color: rgba(120, 180, 240, 0.6);
    background: linear-gradient(135deg, rgba(40, 60, 80, 0.95), rgba(30, 50, 70, 1));
}

.icon-btn:hover img {
    filter: brightness(1.3) contrast(1.3);
    transform: scale(1.1);
}

.icon-btn::after {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, #4a90c2, #6bb6d6, #4a90c2);
    z-index: -1;
    opacity: 0;
    transition: opacity 0.3s ease;
    animation: spin 3s linear infinite;
}

.icon-btn:hover::after {
    opacity: 1;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>
""", unsafe_allow_html=True)
