import streamlit as st

from utils.main import tutoria

st.title("TutorIA")

st.html("""
    <hr>
    <h2>Apoyo escolar con IA</h2>
    <ol>
        <li>Ingrese el tema que desea reforzar</li>
        <li>Ingrese el año o grado</li>
        <li>Ingrese el nivel (Primario, Secundario, Superior, Universitario)</li>
    </ol>
""")

tema = st.text_input("Ingrese el tema", placeholder = "Fracciones")
grado = st.text_input("Ingrese el grado", placeholder = "2°")
nivel = st.text_input("Ingrese el nivel", placeholder = "Secundario")

if st.button("Generar tutoría"):
    tutor = tutoria(tema, grado, nivel)
    st.write(tutor)