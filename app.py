import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# --- STYLE CSS (Fond Rose et Texte BLANC) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #ff4d6d; /* Un rose plus vif pour que le blanc ressorte */
    }
    /* Force le blanc pour tous les textes */
    h1, h2, h3, p, span, label, .stMarkdown, div { 
        color: #ffffff !important; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2); /* Ombre légère pour la lisibilité */
    }
    /* Champs de saisie blancs avec texte noir pour pouvoir écrire */
    .stTextInput input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")
st.write("Réponds aux questions pour débloquer le puzzle de notre poème...")

# --- ÉTAPE 1 : LES QUESTIONS DE BASE ---
col1, col2 = st.columns(2)
with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")
with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()

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
    st.balloons() # Animation dès la première réussite
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
            st.balloons() # Animation finale
            st.markdown("---")
            
            # Ton texte personnel exact
            st.write("### 💌 Mon Message")
            st.write("""
            Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
            et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
            de notre rencontre . BTW je le redis encore mais ton livre sens trop le fatima zahra . 
            voici le poeme preferer pour linstant .
            """)
            
            # Affichage final du poème
            st.subheader("📖 Le Poème :")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")
        else:
            st.error("Le poème n'est pas encore dans le bon ordre. Retente ta chance ! 💪")
else:
    if date_rep != "" or voiture_rep != "":
        st.write("*(En attente des bonnes réponses pour libérer le puzzle...)*")
