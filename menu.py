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

# --- Carga directa desde el archivo en el repo ---
df = pd.read_csv('Employee_data.csv')
st.write("### Datos de empleados")
st.dataframe(df)   # o st.write(df)
# 2) Mostrar las primeras 5 filas (header + datos)
st.write("**Primeras filas del DataFrame:**")
st.dataframe(df.head())

# — Control para seleccionar género —
gender_options = df['gender'].dropna().unique().tolist()

# Crea el selectbox
selected_gender = st.selectbox(
    "Selecciona el género del empleado", 
    options=gender_options
)

# Filtra el DataFrame según la selección
df_filtrado = df[df['gender'] == selected_gender]

# Muestra los datos filtrados
st.write(f"#### Empleados con género: {selected_gender}")
st.dataframe(df_filtrado)
