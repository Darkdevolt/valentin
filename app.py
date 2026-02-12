import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# --- STYLE CSS (Fond Sombre, Texte Rose/Blanc) ---
st.markdown("""
    <style>
    /* Fond de la page en noir profond */
    .stApp { 
        background-color: #0e1117; 
    }
    /* Titres en Rose Fuchsia */
    h1, h2, h3 { 
        color: #ff4d6d !important; 
        font-family: 'Georgia', serif;
    }
    /* Textes et Labels en Blanc pour le contraste */
    p, span, label, .stMarkdown { 
        color: #ffffff !important; 
        font-size: 18px;
    }
    /* Style spécifique pour les champs de saisie (texte noir sur fond blanc pour écrire) */
    .stTextInput input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    /* Style pour le puzzle (multiselect) */
    .stMultiSelect div div {
        background-color: #ff4d6d !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Un Chapitre de Notre Histoire")
st.write("Réponds aux questions pour débloquer le puzzle de notre poème...")

# --- ÉTAPE 1 : LES QUESTIONS ---
col1, col2 = st.columns(2)
with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", placeholder="21/10/2025")
with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", placeholder="Indice : Luxe...").lower().strip()

love_score = st.slider("À quel point m'aimes-tu ?", 0, 100, 50)

# --- CONFIGURATION DU POÈME ---
poeme_correct = [
    "Dear Future lover,",
    "When the time comes and the words 'i love you'",
    "Sit on the verge of my tongue , held captive by my pride and feminine ego ,",
    "i want you to hold my neck tight ,And kiss those words out of me ,",
    "Are you afraid of touching me ,",
    "Because i might change my mind, Before your lips reach mine ?",
    "i wish i could tell you not to be scared"
]

# Mélange des phrases pour le jeu
poeme_melange = sorted(poeme_correct)

# --- LOGIQUE DE VALIDATION ---
if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
    st.markdown("---")
    st.subheader("🧩 Le Puzzle du Poème")
    st.write("Remets les vers dans l'ordre pour découvrir mon message :")
    
    # Le puzzle interactif
    reponse_utilisateur = st.multiselect(
        "Choisis les phrases dans l'ordre chronologique :",
        options=poeme_melange
    )

    if st.button("Valider le poème ❤️"):
        if reponse_utilisateur == poeme_correct:
            st.balloons()
            st.markdown("---")
            
            # Message personnel
            st.write("### 💌 Mon Message")
            st.write(f"""
            Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
            et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
            de notre rencontre.
            """)
            
            # Note sur le livre
            st.info("BTW je le redis encore mais ton livre sent trop le fatima zahra. ✨")
            
            # Affichage final du poème
            st.subheader("📖 Ton poème préféré :")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")
        else:
            st.error("Le poème n'est pas encore dans le bon ordre. Retente ta chance ! 💪")
else:
    if date_rep != "" or voiture_rep != "":
        st.warning("Certaines informations sont incorrectes. Vérifie la date ou le modèle de voiture !")
