import google.generativeai as genai

from utils.env import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def tutoria_gemini(tema, grado, nivel):
    
    prompt = f"Genera una evaluación diagnóstica sobre el tema {tema} para estudiantes de {grado} año de {nivel} que permita identificar fortalezas y debilidades. Proporciona las respuestas correctas y completas para que el alumno pueda autoevaluarse. Basado en el puntaje obtenido, crea contenido detallado para cada rango de puntaje sobre {tema} que incluya una variedad de ejercicios teóricos y prácticos como preguntas y problemas para abordar diferentes aspectos de los subtemas, lista de lecturas recomendadas que cubran tanto conceptos básicos como avanzados del tema incluyendo artículos, capítulos de libros y otros recursos relevantes y videos educativos con explicaciones detalladas y ejemplos prácticos que expliquen los subtemas en los que el alumno necesita mejorar."

    completion = model.generate_content(prompt)

    return completion.text
       