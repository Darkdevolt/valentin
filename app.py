import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# CSS : Fond rose et texte NOIR
st.markdown("""
    <style>
    .stApp { 
        background-color: #fff0f3; 
    }
    /* Force le noir pour tous les textes */
    h1, h2, h3, p, span, label, .stMarkdown, div { 
        color: #000000 !important; 
    }
    /* Style pour les champs de texte */
    .stTextInput input {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")
st.write("Réponds à ces quelques questions pour débloquer la suite...")

# --- Formulaire de base ---
col1, col2 = st.columns(2)

with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")

with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()

love_score = st.slider("À quel point m'aimes-tu ?", 0, 100, 50)

# --- Validation et affichage du message ---
if st.button("Valider ❤️"):
    if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
        st.balloons()
        
        st.markdown("---")
        st.success("Accès accordé... ✨")
        
        # Ton texte personnel
        st.write("### 💌 Un petit mot pour toi")
        st.write("""
        Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
        et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
        de notre rencontre.
        """)
        
        st.info("BTW je le redis encore mais ton livre sent trop le fatima zahra.")
        
        st.write("---")
        st.subheader("📖 Voici ton poème préféré pour l'instant :")
        
        # ICI : Tu peux copier-coller le texte du poème à la place de l'exemple
        st.markdown("""
        > *[Insère ici le texte du poème que tu as choisi]* > *S'il est long, il s'affichera parfaitement ici.*
        """)
        
    else:
        st.error("Les réponses ne sont pas encore les bonnes... Réessaie ! 🕵️‍♂️")
