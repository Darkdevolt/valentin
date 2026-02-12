import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# --- STYLE CSS (Noir sur Rose) ---
st.markdown("""
    <style>
    .stApp { background-color: #fff0f3; }
    h1, h2, h3, p, span, label, div, .stMarkdown { 
        color: #000000 !important; 
    }
    .stTextInput input { color: #000000 !important; }
    /* Style pour le multiselect (le puzzle) */
    .stMultiSelect span { color: #000000 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")
st.write("Réponds aux questions pour débloquer le puzzle de notre poème...")

# --- ETAPE 1 : LES QUESTIONS DE BASE ---
col1, col2 = st.columns(2)
with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")
with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()

love_score = st.slider("À quel point m'aimes-tu ?", 0, 100, 50)

# --- ETAPE 2 : LE PUZZLE DU POÈME ---
# On définit les phrases dans le bon ordre
poeme_correct = [
    "Dear Future lover,",
    "When the time comes and the words 'i love you'",
    "Sit on the verge of my tongue, held captive by my pride and feminine ego,",
    "I want you to hold my neck tight, and kiss those words out of me,",
    "Are you afraid of touching me, because i might change my mind,",
    "Before your lips reach mine ?",
    "I wish i could tell you not to be scared"
]

# On crée une version mélangée pour le choix de l'utilisateur
poeme_melange = sorted(poeme_correct) 

if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
    st.markdown("---")
    st.success("Bravo ! Voici maintenant le puzzle final : Remets le poème dans l'ordre.")
    
    # L'utilisateur doit sélectionner les phrases une par une dans l'ordre
    reponse_utilisateur = st.multiselect(
        "Sélectionne les vers du poème dans le bon ordre chronologique :",
        options=poeme_melange
    )

    # --- ETAPE 3 : LA VALIDATION FINALE ---
    if st.button("Valider le poème ❤️"):
        if reponse_utilisateur == poeme_correct:
            st.balloons()
            st.markdown("---")
            st.header("✨ Félicitations ! ✨")
            
            # Ton texte personnel
            st.write("### 💌 Un petit mot pour toi")
            st.write("""
            Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
            et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
            de notre rencontre.
            """)
            
            st.info("BTW je le redis encore mais ton livre sent trop le fatima zahra.")
            
            # Affichage du poème complet et propre
            st.subheader("📖 Ton poème préféré :")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")
        else:
            st.error("Le poème n'est pas encore dans le bon ordre (ou il manque des phrases). Courage ! 💪")
else:
    if date_rep != "" or voiture_rep != "":
        st.info("Complète les informations de base correctement pour voir le puzzle.")
