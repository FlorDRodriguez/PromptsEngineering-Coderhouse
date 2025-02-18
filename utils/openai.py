from openai import OpenAI
from utils.env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def tutoria_openai(tema, grado, nivel):
    
    prompt = f"Genera una evaluación diagnóstica sobre el tema {tema} para estudiantes de {grado} año de {nivel} que permita identificar fortalezas y debilidades. Proporciona las respuestas correctas y completas para que el alumno pueda autoevaluarse. Basado en el puntaje obtenido, crea una plan de estudio con contenido detallado para cada rango de puntaje sobre {tema} que incluya una variedad de ejercicios teóricos y prácticos como preguntas y problemas para abordar diferentes aspectos de los subtemas, lista de lecturas recomendadas que cubran tanto conceptos básicos como avanzados del tema incluyendo artículos, capítulos de libros y otros recursos relevantes y videos educativos con explicaciones detalladas y ejemplos prácticos que expliquen los subtemas en los que el alumno necesita mejorar."

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user", 
                "content": prompt
            }
        ]
    )

    response = completion.choices[0].message.content

    print(response)

    return response