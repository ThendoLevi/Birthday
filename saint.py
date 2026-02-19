import streamlit as st
import os

# --- CONFIG ---
st.set_page_config(page_title="HBD Hope Matsila", page_icon="🕊️", layout="centered")

# --- FILE LOADER (GitHub Compatible) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = "image_1e2067.png"
image_path = os.path.join(current_dir, image_filename)

# --- SENTIMENTS ---
sentiments = [
    "I just knew there was something about you as soon as we met...",
    "You smiled, you were confident and you spoke engagingly.",
    "I'm sure you remember how I couldn't take my eyes off of those beautiful brown eyes of yours. 👀",
    "I never stood a chance—I was hooked.",
    "I love how honest you are and how quickly you remind me to use my true voice when we speak.",
    "I love that ishhh, it gives me life! 🔥",
    "I love how playful you can be, even though you've got a serious side to you.",
    "You have a way of bringing out the generosity in me; every time I think of you I wanna give you my all.",
    "Ene nwana, seasons may shift and time may fade, but through it all I can never lose Hope.",
    "I'm so into you, I hate it ... 😛",
    "You are a beautiful soul and I know I am blessed with you in my life.",
    "Happy Birthday Muvhuya, you deserve everything good coming your way. ❤️"
]

if 'step' not in st.session_state:
    st.session_state.step = 0

# --- LUXURY STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Montserrat:wght@300;500&display=swap');

    .stApp {
        background-color: #000000;
    }

    .big-font {
        font-family: 'Playfair Display', serif;
        font-size: 65px !important;
        font-weight: 700;
        color: #800000; 
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .saint-sub {
        text-align: center; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 14px;
        margin-top: -10px;
        font-weight: 300;
        opacity: 0.8;
    }

    .sentiment-box {
        font-family: 'Playfair Display', serif;
        padding: 40px;
        border-radius: 50px; 
        font-size: 24px;
        text-align: center;
        line-height: 1.6;
        margin: 25px 0px;
        animation: fadeIn 1.2s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .msg-maroon {
        background-color: #800000;
        color: #ffffff;
        box-shadow: 0px 10px 20px rgba(128, 0, 0, 0.4);
    }
    
    .msg-white {
        background-color: #ffffff;
        color: #800000;
        box-shadow: 0px 10px 20px rgba(255, 255, 255, 0.1);
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }

    .portrait-frame {
        border: 12px solid #ffffff;
        border-radius: 10px;
        padding: 0px;
        background-color: #ffffff;
        box-shadow: 0px 0px 40px rgba(128, 0, 0, 0.3);
        margin-bottom: 30px;
    }
    
    .stButton>button {
        width: 100%;
        background-color: transparent;
        color: #ffffff;
        border-radius: 50px;
        border: 2px solid #800000;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 2px;
        padding: 15px;
        transition: 0.4s;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #800000;
        color: white;
        border: 2px solid #ffffff;
        transform: translateY(-2px);
    }

    .footer-text {
        text-align: center;
        color: #444;
        font-family: 'Montserrat', sans-serif;
        font-size: 11px;
        margin-top: 60px;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="big-font">Hope Matsila</p>', unsafe_allow_html=True)
st.markdown('<p class="saint-sub">Saint Nomayini</p>', unsafe_allow_html=True)

# --- THE PAINTED PORTRAIT ---
if os.path.exists(image_path):
    st.markdown('<div class="portrait-frame">', unsafe_allow_html=True)
    st.image(image_path, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error(f"Portrait not found. Make sure '{image_filename}' is in the root of your GitHub repo.")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- INTERACTIVE SENTIMENTS ---
for i in range(st.session_state.step + 1):
    style_class = "msg-maroon" if i % 2 == 0 else "msg-white"
    st.markdown(f'<div class="sentiment-box {style_class}">{sentiments[i]}</div>', unsafe_allow_html=True)

# Story Progression
if st.session_state.step < len(sentiments) - 1:
    if st.button("KEEP READING ❤️"):
        st.session_state.step += 1
        st.balloons() # This now triggers every time she clicks!
        st.rerun()
else:
    st.markdown("<h2 style='text-align: center; color: #800000; font-family: Playfair Display; margin-top: 20px;'>Happy Birthday, Muvhuya. 🌹</h2>", unsafe_allow_html=True)
    if st.button("START OVER"):
        st.session_state.step = 0
        st.balloons()
        st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #800000;'>February 16</h2>", unsafe_allow_html=True)
    st.write("For the one who inspires.")
    if st.button("Sparkle"):
        st.snow()

st.markdown('<p class="footer-text">MADE 4 MISS HOPE</p>', unsafe_allow_html=True)


