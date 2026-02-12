import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# --- STYLE CSS (Fond Rose, Texte BLANC et Slider BLANC) ---
st.markdown("""
    <style>
    .stApp { background-color: #ff4d6d; }
    h1, h2, h3, p, span, label, .stMarkdown, div { color: #ffffff !important; }

    /* Slider tout en blanc */
    div[data-baseweb="slider"] > div:first-child { background: rgba(255, 255, 255, 0.3) !important; }
    div[data-baseweb="slider"] div[style*="background-color: rgb(255, 75, 75)"] { background-color: #ffffff !important; }
    div[role="slider"] { background-color: #ffffff !important; border: 2px solid #ffffff !important; }
    div[data-testid="stTickBarMin"], div[data-testid="stTickBarMax"], div[data-testid="stSliderThumbValue"] { color: #ffffff !important; }

    /* Champs de saisie (fond blanc, texte noir) */
    .stTextInput input { color: #000000 !important; background-color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")
st.write("Réponds aux questions pour débloquer la suite...")

# --- ÉTAPE 1 : LES QUESTIONS DE BASE ---
col1, col2 = st.columns(2)
with col1:
    date_rep = st.text_input("Quelle est la date de notre rencontre ? (JJ/MM/AAAA)", "")
with col2:
    voiture_rep = st.text_input("Quelle est notre voiture préférée ?", "").lower().strip()

love_score = st.slider("À quel point m'aimes-tu ?", 0, 100, 50)

# Phrases du poème pour le puzzle
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

# --- LOGIQUE DE VALIDATION ---
if date_rep == "21/10/2025" and voiture_rep == "phantom" and love_score == 100:
    st.markdown("---")
    
    # LE TEXTE SUR FATIMA APPARAÎT ICI (Dès que les infos de base sont ok)
    st.write("### 💌 Un petit mot pour toi")
    st.write("""
    Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
    et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
    de notre rencontre . BTW je le redis encore mais ton livre sens trop le fatima zahra . 
    voici le poeme preferer pour linstant .
    """)
    
    st.markdown("---")
    st.subheader("🧩 Le Puzzle du Poème")
    st.write("Remets maintenant les vers dans l'ordre :")
    
    reponse_utilisateur = st.multiselect(
        "Choisis les phrases dans l'ordre chronologique :",
        options=poeme_melange
    )

    if st.button("Valider le puzzle ❤️"):
        if reponse_utilisateur == poeme_correct:
            # LES BALLONS APPARAISSENT UNIQUEMENT ICI
            st.balloons() 
            st.success("C'est parfait... ✨")
            
            st.subheader("📖 Ton Poème :")
            for ligne in poeme_correct:
                st.write(f"*{ligne}*")
        else:
            st.error("Le poème n'est pas encore dans le bon ordre. Retente ta chance !")
else:
    if date_rep != "" or voiture_rep != "":
        st.write("*(Réponds correctement aux questions pour voir la suite...)*")
