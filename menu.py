import streamlit as st
import pandas as pd
import numpy as np

# Título y una breve descripción de la aplicación web
st.title('Socialize your knowledge')
st.write('Se analizara el desempeño de los empleados de la empresa Socialize your knowledge')

#Logotipo de la empresa en la aplicación web
from PIL import Image, ImageDraw, ImageFont

image = Image.open('Streamlit.jpeg')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Socialize your Knowledge!", fill=(255, 0, 0), font=font)

st.image(image, caption='Socialize your Knowledge')


df = pd.read_csv('Employee_data.csv')
#st.write("### Datos de empleados")
#st.dataframe(df)   # o st.write(df)
# 2) Mostrar las primeras 5 filas (header + datos)
#st.write("**Primeras filas del DataFrame:**")
#st.dataframe(df.head())

# desplegar un control para seleccionar el género del empleado
gender_options = df['gender'].dropna().unique().tolist()

selected_gender = st.selectbox(
    "Selecciona el género del empleado", 
    options=gender_options
)

# seleccionar un rango del puntaje de desempeño del empleado
df_filtrado = df[df['gender'] == selected_gender]

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

# seleccionar el estado civil del empleado

marital_options = df['marital_status'].dropna().unique().tolist()

selected_marital = st.selectbox(
    "Selecciona el estado civil del empleado",
    options=marital_options
)

df_marital = df[df['marital_status'] == selected_marital]

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

#distribución de los puntajes de desempeño.
chart = (
    alt.Chart(df)
       .transform_aggregate(
           mean_hours="mean(average_work_hours)",
           groupby=["gender"]
       )
       .mark_bar()
       .encode(
           x=alt.X("gender:N", title="Género"),
           y=alt.Y("mean_hours:Q", title="Horas Trabajadas Promedio"),
           color=alt.Color("gender:N", legend=None)
       )
       .properties(
           title="Promedio de Horas Trabajadas por Género",
           width=600,
           height=400
       )
)

# Edad de los empleados con respecto al salario de los mismo
st.altair_chart(chart, use_container_width=True)

scatter = (
    alt.Chart(df)
       .mark_circle(size=60, opacity=0.7)
       .encode(
           x=alt.X('age:Q', title='Edad'),
           y=alt.Y('salary:Q', title='Salario'),
           tooltip=['age', 'salary']   # muestra valores al pasar el cursor
       )
       .properties(
           title='Relación Edad vs Salario de los Empleados',
           width=600,
           height=400
       )
)
st.altair_chart(scatter, use_container_width=True)

#Relación del promedio de horas trabajadas versus el puntaje de desempeño

scatter2 = (
    alt.Chart(df)
       .mark_circle(size=60, opacity=0.7)
       .encode(
           x=alt.X('average_work_hours:Q', title='Horas Trabajadas Promedio'),
           y=alt.Y('performance_score:Q', title='Puntaje de Desempeño'),
           tooltip=['average_work_hours', 'performance_score']
       )
       .properties(
           title='Relación: Horas Trabajadas vs Puntaje de Desempeño',
           width=600,
           height=400
       )
)
st.altair_chart(scatter2, use_container_width=True)

#— Conclusión Global del Análisis —
st.markdown("## Conclusión Global del Análisis")

#Métricas generales
total_emp   = len(df)
avg_perf    = df['performance_score'].mean()
avg_hours   = df['average_work_hours'].mean()
median_perf = df['performance_score'].median()

top_gender      = df['gender'].value_counts().idxmax()
top_marital     = df['marital_status'].value_counts().idxmax()
pct_top_gender  = df['gender'].value_counts(normalize=True).max() * 100
pct_top_marital = df['marital_status'].value_counts(normalize=True).max() * 100

corr = df['average_work_hours'].corr(df['performance_score'])

if corr > 0:
    relation = "positiva"
elif corr < 0:
    relation = "negativa"
else:
    relation = "nula"


st.markdown(f"- Se analizaron **{total_emp}** empleados en total.")
st.markdown(f"- El puntaje de desempeño promedio es **{avg_perf:.2f}** (mediana: {median_perf:.1f}).")
st.markdown(f"- Las horas trabajadas promedio son **{avg_hours:.2f}** horas.")
st.markdown(
    f"- El género más frecuente es **{top_gender}** ({pct_top_gender:.1f}% de la plantilla) "
    f"y el estado civil más común es **{top_marital}** ({pct_top_marital:.1f}%)."
)
st.markdown(
    f"- La correlación entre horas trabajadas y puntaje de desempeño es **{corr:.2f}**, "
    f"indicando una relación **{relation}**."
)



