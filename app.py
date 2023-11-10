import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("Espacio para aprender a construir aplicaciones")
st.write("Hub de Innovación SENA")
image = Image.open("propo.jpg")

st.image(image, caption='Somos el Hub de Innovación')

st.write("Equipo de trabajo especializado")
image = Image.open("equipo.jpg")

st.image(image, caption='Contamos con un equipo de profesionales expertos en innovación y tecnologías emergentes')

