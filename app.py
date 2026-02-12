import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mission Saint-Valentin 💘", page_icon="❤️")

# Petit style personnalisé pour l'ambiance
st.markdown("""
    <style>
    .stApp { background-color: #fff0f3; }
    h1 { color: #d00000; }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Le Coffre-Fort de l'Amour")
st.write("Réponds correctement aux questions pour débloquer ton message...")

# Utilisation de colonnes pour le rendu
col1, col2 = st.columns(2)

with col1:
    q1 = st.text_input("Quelle est la date de notre rencontre ? (ex: 12/05)", "")
with col2:
    q2 = st.text_input("Quel est notre plat préféré ?", "").lower()

q3 = st.slider("À quel point m'aimes-tu (sur 100) ?", 0, 100, 50)

if st.button("Tenter d'ouvrir le coffre 🔓"):
    # Remplacez les valeurs ci-dessous par vos vraies réponses
    if q1 == "14/02" and "pizza" in q2 and q3 == 100:
        st.balloons() # Effet de ballons
        st.success("BRAVO ! Tu as ouvert mon cœur !")
        st.header("✨ Ton message spécial ✨")
        st.write("Je t'aime plus que Python et Streamlit réunis. Bon voyage à Venise !")
        # st.image("votre_photo.jpg") # Vous pouvez ajouter une photo ici
    else:
        st.error("Oups... Ce n'est pas encore ça. Réessaie ! ❤️")
