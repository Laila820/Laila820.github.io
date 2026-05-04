import streamlit as st
import pandas as pd
st.title("Bienvenue sur le site web de Laïla")
choix = st.selectbox ("Indiquez votre arrondissement de récupération", ["Manhatan", "Bronx", "Queens","NaN"])
st.write (f'tu as choisi {choix}')
if choix == "Manhatan":
    st.image(["https://storage.googleapis.com/assets_upload_prod/T3ergNADp0c7j0byzc8KhnhqB4LtkFKr.png"])
elif choix == "Bronx":
    st.image(["https://storage.googleapis.com/assets_upload_prod/RFUCtivKdJrOH3Kbd62gigrL43I3zsiP.png"])
elif choix == "NaN":
    st.image(["https://storage.googleapis.com/assets_upload_prod/laDwm37mWnEWhQdp03pUFnrJ6AhVvVgz.png"])
elif choix == "Queens":
    st.image(["https://storage.googleapis.com/assets_upload_prod/SfnSAb2ECl8hVJoGX71An2DizMzaZQGK.png"])
