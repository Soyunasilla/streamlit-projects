import streamlit as st
import pandas as pd
import numpy as np


st.title('Socialize your knowledge')
st.write('Se analizara el desempeño de los empleados de la empresa Socialize your knowledge')

image = Image.open('streamlit.jpeg')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Zombies y!", fill=(255, 0, 0), font=font)

st.image(image, caption='Zombies vs Guerrera Ninja')
