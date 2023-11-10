import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("Espacio para aprender a construir aplicaciones")
st.write("Hub de Innovación SENA")
image = Image.open("propo.jpg")

st.image(image, caption='Somos el Hub de Innovación')

