import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mission Saint-Valentin 💘", page_icon="❤️")

# CSS pour le fond rose et le texte NOIR (visibilité maximale)
st.markdown("""
    <style>
    .stApp { 
        background-color: #fff0f3; 
    }
    /* Force tout le texte en noir */
    h1, h2, h3, p, span, label, div { 
        color: #000000 !important; 
    }
    /* Style pour les champs de saisie et le slider */
    .stTextInput input {
        color: #000000 !important;
    }
    .stSlider label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Le Coffre-Fort de l'Amour")
st.write("Réponds correctement aux trois questions pour découvrir ton message secret...")

# --- Zone de saisie ---
col1, col2 = st.columns(2)

with col1:
    # Réponse attendue : 21/10/2025
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")

with col2:
    # Réponse attendue : phantom
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()

# Réponse attendue : 100
love_score = st.slider("À quel point m'aimes-tu (sur 100) ?", 0, 100, 50)

# --- Logique de validation ---
if st.button("Tenter d'ouvrir le coffre 🔓"):
    # Vérification des 3 conditions
    if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
        st.balloons()
        st.success("ACCÈS AUTORISÉ ! ✨")
        
        st.markdown("---")
        st.header("💌 Mon Message pour Toi")
        st.write("""
        Depuis ce fameux **21 octobre 2025**, ma vie est devenue un vrai rêve. 
        Même si on n'est pas encore en **Phantom**, on avance ensemble et c'est tout ce qui compte.
        
        **Je t'aime plus que tout ! Joyeuse Saint-Valentin !** 🌹
        """)
        # Optionnel : décommente la ligne du dessous si tu as une photo dans ton dossier
        # st.image("notre_photo.jpg", caption="Nous ❤️")
        
    else:
        # Message d'erreur si l'un des éléments est faux
        st.error("Oups... Le coffre reste fermé. Vérifie bien la date, le modèle de la voiture ou ton niveau d'amour ! 🕵️‍♂️")
