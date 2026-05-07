import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# -----------------------------
# Comptes utilisateurs
# -----------------------------

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },

        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# -----------------------------
# Authentification
# -----------------------------

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

authenticator.login()

# -----------------------------
# Vérification connexion
# -----------------------------

if st.session_state["authentication_status"]:

    # -----------------------------
    # Sidebar
    # -----------------------------

    with st.sidebar:

        st.write(f"Bienvenue {st.session_state['name']}")

        selection = option_menu(
            menu_title="Menu",
            options=[
                "Accueil",
                "Album photos des animaux de compagnie"
            ],
            icons=["house", "camera"]
        )

        authenticator.logout("Déconnexion")

    # -----------------------------
    # Page accueil
    # -----------------------------

    if selection == "Accueil":

        st.title("Bienvenue sur la page d'accueil !")

        st.image(
            "https://tse4.mm.bing.net/th/id/OIP.ts__Dlf1cpPK_ltNVB1SowHaE8?rs=1&pid=ImgDetMain&o=7&rm=3"
        )

    # -----------------------------
    # Album photos
    # -----------------------------

    elif selection == "Album photos des animaux de compagnie":

        st.title("Album de mes animaux")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Chat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("Chien")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        with col3:
            st.header("Hibou")
            st.image("https://static.streamlit.io/examples/owl.jpg")

# -----------------------------
# Mauvais mot de passe
# -----------------------------

elif st.session_state["authentication_status"] is False:

    st.error("Nom d'utilisateur ou mot de passe incorrect")

# -----------------------------
# Champs vides
# -----------------------------

elif st.session_state["authentication_status"] is None:

    st.warning("Veuillez remplir les champs")