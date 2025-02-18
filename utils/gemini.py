import google.generativeai as genai

from utils.env import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def tutoria_gemini(tema, grado, nivel):
    
    prompt = f"Genera una evaluación diagnóstica completa sobre el tema {tema} para estudiantes de {grado} año de {nivel}. Luego, proporciona las respuestas correctas para cada pregunta y problema, junto con una tabla de puntajes. Según el puntaje obtenido, se deben indicar las fortalezas del estudiante, las áreas que requieren mejora y un plan de estudio detallado para cada rango de puntaje. Este plan debe incluir ejercicios teóricos y prácticos, una lista de lecturas recomendadas que cubran conceptos básicos y avanzados del tema (artículos, capítulos de libros y otros recursos relevantes), así como videos educativos con explicaciones detalladas y ejemplos prácticos que expliquen los subtemas en los que el alumno necesita mejorar."

    completion = model.generate_content(prompt)

    return completion.text
       