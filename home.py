import streamlit as st

# Set Ghost of Tsushima-inspired background using CSS gradients and overlays
def set_bg():
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(120deg, #f8fafc 0%, #e0e7ef 100%),
                        url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80');
            background-blend-mode: lighten, normal;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .samurai-title {{
            color: #2d2d2d;
            text-shadow: 1px 1px 8px #fff, 0 0 10px #b87333;
            font-family: 'Montserrat', 'Cinzel', serif;
            font-size: 2.8em;
            margin-bottom: 0.5em;
            letter-spacing: 2px;
        }}
        .samurai-box label, .samurai-box input, .samurai-box textarea {{
            color: #2d2d2d !important;
            background: rgba(255,255,255,0.85) !important;
            border-radius: 12px;
            border: 1px solid #b87333 !important;
            font-size: 1.1em;
        }}
        .stButton>button {{
            background: linear-gradient(90deg, #b87333 0%, #f8fafc 100%);
            color: #2d2d2d;
            border-radius: 10px;
            font-weight: bold;
            border: none;
            box-shadow: 0 2px 8px #b8733340;
            font-size: 1.1em;
        }}
        .samurai-box {{
            box-shadow: 0 4px 32px #b8733320;
            padding: 2em 1.5em 1em 1.5em;
            background: rgba(255,255,255,0.7);
            border-radius: 18px;
            margin-bottom: 2em;
        }}
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Cinzel:wght@700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

set_bg()

st.markdown('<div class="samurai-title">⚔️ Tutoring Signup: Ghost of Tsushima Edition ⚔️</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#2d2d2d; font-size:1.2em; background:rgba(255,255,255,0.7); border-radius:10px; padding:0.5em 1em;'>Step onto the path of the samurai! Sign up below to begin your journey of learning, inspired by the honor and spirit of Tsushima. Your legend begins here.</p>", unsafe_allow_html=True)

with st.form("signup_form"):
    st.markdown('<div class="samurai-box">', unsafe_allow_html=True)
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    background = st.text_area("Background")
    courses = st.text_input("list of courses")
    address = st.text_input("Address")
    submit = st.form_submit_button("Join the Path")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        st.balloons()
        st.success(f"Thank you for signing up, {first_name} {last_name}! The spirit of Tsushima welcomes you to the way of knowledge.")
        st.write("**Background:**", background)
        st.write("**List of courses:**", courses)
        st.write("**Address:**", address)