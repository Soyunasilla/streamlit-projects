import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write('Menu')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.title('Socialize your knowledge')
st.write('Se analizara el desempeño de los empleados de la empresa Socialize your knowledge')

dataframe = pd.DataFrame(
    np.random.randint(1, 57, size=(6, 10)),
    columns=[f'AM {i}' for i in range(10)]
)

st.dataframe(dataframe)
x = st.slider('x') # 👈 este es un widget
st.write(x, 'al cuadrado es', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

from PIL import Image, ImageDraw, ImageFont

image = Image.open('streamlit.jpeg')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Zombies y!", fill=(255, 0, 0), font=font)

st.image(image, caption='Zombies vs Guerrera Ninja')

# Abres el archivo OGG en modo binario
with open('myaudio.ogg', 'rb') as audio_file:
    audio_bytes = audio_file.read()

# Aquí Streamlit muestra el player
st.audio(audio_bytes, format='audio/ogg')

video_file = open('mi_video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
