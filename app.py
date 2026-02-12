import streamlit as st
import streamlit.components.v1 as components

# Configuration
st.set_page_config(page_title="Pour toi... 💘", page_icon="🌹")

# --- STYLE CSS (Fond Rose, Texte BLANC) ---
st.markdown("""
    <style>
    .stApp { background-color: #ff4d6d; }
    h1, h2, h3, p, span, label, .stMarkdown, div { color: #ffffff !important; }
    
    /* Slider blanc */
    div[data-baseweb="slider"] > div:first-child { background: rgba(255, 255, 255, 0.3) !important; }
    div[data-baseweb="slider"] div[style*="background-color: rgb(255, 75, 75)"] { background-color: #ffffff !important; }
    div[role="slider"] { background-color: #ffffff !important; border: 2px solid #ffffff !important; }
    div[data-testid="stTickBarMin"], div[data-testid="stTickBarMax"], div[data-testid="stSliderThumbValue"] { color: #ffffff !important; }

    /* Champs de saisie */
    .stTextInput input { color: #000000 !important; background-color: #ffffff !important; }
    
    /* On cache le bouton de base de Streamlit pour l'étape finale */
    .final-step { text-align: center; padding: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("💘 Notre Histoire")
st.write("Réponds aux questions pour débloquer la suite...")

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
    st.write("""
    Ce poème me rappelle la première fois où je t'ai dit je t'aime et oui je t'aime 
    et oui j'ai bien lu et compris ce poème qui me rappelle un chapitre important 
    de notre rencontre . BTW je le redis encore mais ton livre sens trop le fatima zahra .
    """)
    
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
        
        # --- ÉTAPE FINALE : LE BOUTON FLUIDE (HTML/JS) ---
        st.subheader("🌹 Une dernière chose...")
        
        # Injection du code JavaScript pour la fluidité
        valentine_html = """
        <div style="text-align: center; font-family: sans-serif; color: white;">
            <h2 id="question">Veux-tu être ma Valentine ?</h2>
            <div style="display: flex; justify-content: center; align-items: center; gap: 20px; height: 200px;">
                <button id="yesBtn" style="font-size: 20px; padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer;">OUI ! ❤️</button>
                <button id="noBtn" style="font-size: 40px; padding: 10px 20px; background-color: #dc3545; color: white; border: none; border-radius: 5px; cursor: pointer;">Non</button>
            </div>
            <p style="margin-top: 20px; font-style: italic;">ps : nessaye pas dappuyer sur le bouton Non</p>
        </div>

        <script>
            let noClickCount = 0;
            const yesBtn = document.getElementById('yesBtn');
            const noBtn = document.getElementById('noBtn');
            const question = document.getElementById('question');

            noBtn.addEventListener('click', () => {
                noClickCount++;
                // Le bouton OUI grandit
                let newYesSize = 20 + (noClickCount * 15);
                yesBtn.style.fontSize = newYesSize + 'px';
                
                // Le bouton NON rétrécit
                let newNoSize = Math.max(40 - (noClickCount * 7), 5);
                noBtn.style.fontSize = newNoSize + 'px';
                if (newNoSize < 10) noBtn.style.opacity = '0.5';
            });

            yesBtn.addEventListener('click', () => {
                document.body.innerHTML = `
                    <div style="text-align: center; color: white; font-family: sans-serif; padding-top: 20px;">
                        <h1>😍 JE LE SAVAIS !</h1>
                        <p style="font-size: 20px;">Tu as fait le meilleur choix. Je t'aime ! ❤️</p>
                        <div style="text-align: left; display: inline-block; margin-top: 20px; font-style: italic;">
                            <p>Dear Future lover,</p>
                            <p>When the time comes and the words 'i love you'</p>
                            <p>Sit on the verge of my tongue , held captive by my pride and feminine ego ,</p>
                            <p>i want you to hold my neck tight ,And kiss those words out of me ,</p>
                            <p>Are you afraid of touching me ,</p>
                            <p>Because i might change my mind, Before your lips reach mine ?</p>
                            <p>i wish i could tell you not to be scared</p>
                        </div>
                    </div>
                `;
            });
        </script>
        """
        components.html(valentine_html, height=500)

else:
    if date_rep != "" or voiture_rep != "":
        st.write("*(Réponds correctement aux questions pour débloquer le jeu...)*")
