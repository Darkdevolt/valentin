import streamlit as st

# Configuration
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# Initialisation des états
if 'non_count' not in st.session_state:
    st.session_state.non_count = 0
if 'bravo' not in st.session_state:
    st.session_state.bravo = False

# --- STYLE CSS (Fluide et Rose) ---
size_oui = 20 + (st.session_state.non_count * 12)
size_non = max(35 - (st.session_state.non_count * 6), 5)

st.markdown(f"""
    <style>
    .stApp {{ background-color: #ff4d6d; }}
    h1, h2, h3, p, span, label, .stMarkdown, div {{ color: #ffffff !important; font-family: 'Arial', sans-serif; }}
    
    /* Animation de transition pour la fluidité */
    .stButton button {{
        transition: all 0.4s ease-in-out !important; 
        border-radius: 10px !important;
    }}

    /* Taille dynamique du bouton OUI */
    div[data-testid="column"]:nth-child(1) button {{
        font-size: {size_oui}px !important;
        height: auto !important;
        padding: 10px !important;
        background-color: #28a745 !important;
        border: none !important;
        color: white !important;
    }}

    /* Taille dynamique du bouton NON */
    div[data-testid="column"]:nth-child(2) button {{
        font-size: {size_non}px !important;
        background-color: #dc3545 !important;
        border: none !important;
        color: white !important;
        opacity: {max(1 - st.session_state.non_count*0.1, 0.3)} !important;
    }}

    /* Champs de saisie */
    .stTextInput input {{ color: #000000 !important; background-color: #ffffff !important; }}
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

# --- LOGIQUE ---
if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
    st.markdown("---")
    st.write("### 💌 Un petit mot pour toi")
    st.write("Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important de notre rencontre. BTW je le redis encore mais ton livre sens trop le fatima zahra.")
    
    st.markdown("---")
    st.write("### 🧩 Le Jeu")
    st.write("Je sais que tu aimes les puzzles donc on va y jouer de maniere tres simples voici le jeu :")

    poeme_correct = ["Dear Future lover,", "When the time comes and the words 'i love you'", "Sit on the verge of my tongue , held captive by my pride and feminine ego ,", "i want you to hold my neck tight ,And kiss those words out of me ,", "Are you afraid of touching me ,", "Because i might change my mind, Before your lips reach mine ?", "i wish i could tell you not to be scared"]
    
    reponse_utilisateur = st.multiselect("Remets les vers dans l'ordre :", options=sorted(poeme_correct))

    if reponse_utilisateur == poeme_correct:
        st.markdown("---")
        st.header("Veux-tu être ma Valentine ?")

        c1, c2 = st.columns([2, 1]) # Le bouton Oui a plus d'espace
        
        with c1:
            if st.button("OUI ! ❤️"):
                st.session_state.bravo = True
        
        with c2:
            if st.button("Non"):
                st.session_state.non_count += 1
                st.rerun()

        st.write("*ps : nessaye pas dappuyer sur le bouton Non*")

        if st.session_state.bravo:
            st.balloons() # ICI les ballons vont fonctionner car c'est du Python pur
            st.success("JE LE SAVAIS ! 😍")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")
else:
    if date_rep != "" or voiture_rep != "":
        st.write("*(Réponses incorrectes...)*")
