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


# Relación del promedio de horas trabajadas versus el puntaje de desempeño

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


# — Cálculo de correlación —
corr = df['average_work_hours'].corr(df['performance_score'])

# — Cálculo de promedios para empleados por encima y por debajo de la media de horas —
mean_hours = df['average_work_hours'].mean()
high_df   = df[df['average_work_hours'] > mean_hours]
low_df    = df[df['average_work_hours'] <= mean_hours]

avg_perf_high = high_df['performance_score'].mean()
avg_perf_low  = low_df['performance_score'].mean()

# — Despliegue de la conclusión —
st.markdown("## Conclusión del Análisis")

# Texto principal sobre la correlación
if corr > 0:
    relation = "positiva"
elif corr < 0:
    relation = "negativa"
else:
    relation = "nula"

st.markdown(f"- La **correlación** entre horas trabajadas y puntaje de desempeño es de **{corr:.2f}**, " \
            f"indicando una relación **{relation}**.")

# Comparativa de desempeño según horas
st.markdown(
    f"- Los empleados que trabajan **por encima** de la media de horas ({mean_hours:.1f} h) tienen un puntaje " \
    f"promedio de **{avg_perf_high:.1f}**, mientras que quienes trabajan **igual o menos** horas que la media " \
    f"tienen un puntaje promedio de **{avg_perf_low:.1f}**."
)

# Recomendación práctica
st.markdown(
    "> 💡 **Recomendación:** Si buscamos mejorar el desempeño, podríamos revisar qué prácticas llevan " \
    "aquellos que trabajan más horas y replicarlas en el resto del equipo."
)


