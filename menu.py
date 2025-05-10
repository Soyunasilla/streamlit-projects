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
#st.write("### Datos de empleados")
#st.dataframe(df)   # o st.write(df)
# 2) Mostrar las primeras 5 filas (header + datos)
#st.write("**Primeras filas del DataFrame:**")
#st.dataframe(df.head())

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

# Calcular los valores mínimos y máximos

min_score = int(df['performance_score'].min())
max_score = int(df['performance_score'].max())

selected_range= st.slider(
"Selecciona un rango de desempeño",
    min_value=min_score,
    max_value=max_score,
    value=(min_score, max_score),
    step=1
    )

low, high = selected_range
df_filtered=df[(df['performance_score'] >= low) & (df['performance_score'] <= high)]

st.write(f"### Empleados con desempeño entre {low} y {high}")
st.dataframe(df_filtered)

# — Control para seleccionar estado civil —
# 1) Lista de valores únicos (sin NaN)
marital_options = df['marital_status'].dropna().unique().tolist()

# 2) Selectbox de Streamlit
selected_marital = st.selectbox(
    "Selecciona el estado civil del empleado",
    options=marital_options
)

# 3) Filtrado del DataFrame
df_marital = df[df['marital_status'] == selected_marital]

# 4) Mostrar resultados
st.write(f"### Empleados con estado civil: {selected_marital}")
st.dataframe(df_marital)

import altair as alt

chart = (
    alt.Chart(df)
       .mark_bar()
       .encode(
           alt.X('performance_score:Q', bin=alt.Bin(step=1), title='Score'),
           alt.Y('count()', title='Número de empleados')
       )
       .properties(title='Distribución de Puntajes')
)
st.altair_chart(chart, use_container_width=True)

