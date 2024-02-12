import streamlit as st
from PIL import Image
import requests
import numpy as np

def predict(image):
    files = {"file" :  image}

    req = requests.post("http://localhost:8000/predict", files=files)

    resultat = req.json()
    
    return resultat

st.title("Corn Plant Image Classification")

upload = st.file_uploader("Chargez votre image",
                           type=['png', 'jpeg', 'jpg'])

if upload:
    resultat = predict(upload.getvalue())
    pourcentage = "{:.2f}".format(resultat['confidence'] * 100)
    st.image(Image.open(upload), caption='Image', use_column_width=True)
    
    st.write(f"Classe prédite : {resultat['class']}")
    st.write(f"Probabilite : {pourcentage}%")


