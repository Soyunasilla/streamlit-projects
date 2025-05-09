import streamlit as st
import pandas as pd
import numpy as np


st.title('Socialize your knowledge')
st.write('Se analizara el desempeño de los empleados de la empresa Socialize your knowledge')

from PIL import Image, ImageDraw, ImageFont

image = Image.open('Streamlit.jpeg')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Socialize your Knowledge!", fill=(255, 0, 0), font=font)

st.image(image, caption='Socialize your Knowledge')
