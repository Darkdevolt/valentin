import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# Initialisation de l'état pour le jeu du bouton Non
if 'non_count' not in st.session_state:
    st.session_state.non_count = 0
if 'valentine_validee' not in st.session_state:
    st.session_state.valentine_validee = False

# --- STYLE CSS ---
# On calcule les tailles dynamiquement
size_oui = 20 + (st.session_state.non_count * 15)  # Le bouton OUI grandit vite
size_non = max(40 - (st.session_state.non_count * 8), 5) # Le bouton NON rétrécit

st.markdown(f"""
    <style>
    .stApp {{ background-color: #ff4d6d; }}
    h1, h2, h3, p, span, label, .stMarkdown, div {{ color: #ffffff !important; }}

    /* Slider blanc */
    div[data-baseweb="slider"] > div:first-child {{ background: rgba(255, 255, 255, 0.3) !important; }}
    div[data-baseweb="slider"] div[style*="background-color: rgb(255, 75, 75)"] {{ background-color: #ffffff !important; }}
    div[role="slider"] {{ background-color: #ffffff !important; border: 2px solid #ffffff !important; }}
    
    /* Champs de saisie */
    .stTextInput input {{ color: #000000 !important; background-color: #ffffff !important; }}

    /* Dynamisme des boutons Oui/Non */
    .btn-oui button {{
        font-size: {size_oui}px !important;
        background-color: #28a745 !important;
        color: white !important;
        width: 100%;
    }}
    .btn-non button {{
        font-size: {size_non}px !important;
        background-color: #dc3545 !important;
        color: white !important;
        width: 100%;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")

# --- ÉTAPE 1 : QUESTIONS ---
col1, col2 = st.columns(2)
with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")
with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()
love_score = st.slider("À quel point m'aimes-tu ?", 0, 100, 50)

# --- LOGIQUE PRINCIPALE ---
if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
    st.markdown("---")
    st.write("### 💌 Un petit mot pour toi")
    st.write("Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important de notre rencontre. BTW je le redis encore mais ton livre sens trop le fatima zahra.")
    
    st.markdown("---")
    st.write("### 🧩 Le Jeu")
    st.write("Je sais que tu aimes les puzzles donc on va y jouer de maniere tres simples voici le jeu :")

    poeme_correct = [
        "Dear Future lover,",
        "When the time comes and the words 'i love you'",
        "Sit on the verge of my tongue , held captive by my pride and feminine ego ,",
        "i want you to hold my neck tight ,And kiss those words out of me ,",
        "Are you afraid of touching me ,",
        "Because i might change my mind, Before your lips reach mine ?",
        "i wish i could tell you not to be scared"
    ]
    poeme_melange = sorted(poeme_correct)

    reponse_utilisateur = st.multiselect("Remets les vers dans l'ordre :", options=poeme_melange)

    if reponse_utilisateur == poeme_correct:
        st.success("Puzzle réussi ! ✨")
        st.markdown("---")
        
        # --- DERNIÈRE ÉTAPE : LA DEMANDE ---
        st.subheader("🌹 Une dernière chose...")
        st.header("Veux-tu être ma Valentine ?")

        col_oui, col_non = st.columns([1 + (st.session_state.non_count * 0.5), 1])

        with col_oui:
            st.markdown('<div class="btn-oui">', unsafe_allow_html=True)
            if st.button("OUI ! ❤️"):
                st.session_state.valentine_validee = True
            st.markdown('</div>', unsafe_allow_html=True)

        with col_non:
            st.markdown('<div class="btn-non">', unsafe_allow_html=True)
            if st.button("Non"):
                st.session_state.non_count += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("---")
        st.write("*ps : nessaye pas dappuyer sur le bouton Non*")

        # Affichage final si OUI
        if st.session_state.valentine_validee:
            st.balloons()
            st.write("### 😍 JE LE SAVAIS !")
            st.write("Tu as fait le meilleur choix. Je t'aime ! ❤️")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")

else:
    if date_rep != "" or voiture_rep != "":
        st.write("*(Réponds correctement aux questions pour débloquer la suite...)*")
