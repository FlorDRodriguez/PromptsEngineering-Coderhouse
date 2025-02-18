from openai import OpenAI
from utils.env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def tutoria_openai(tema, grado, nivel):
    
    prompt = f"Genera una evaluación diagnóstica completa sobre el tema {tema} para estudiantes de {grado} año de {nivel}. Luego, proporciona las respuestas correctas para cada pregunta y problema, junto con una tabla de puntajes. Según el puntaje obtenido, se deben indicar las fortalezas del estudiante, las áreas que requieren mejora y un plan de estudio detallado para todos y cada uno de los rangos de puntaje. Este plan debe incluir ejercicios teóricos y prácticos, una lista de lecturas recomendadas que cubran conceptos básicos y avanzados del tema (artículos, capítulos de libros y otros recursos relevantes), así como videos educativos con explicaciones detalladas y ejemplos prácticos que expliquen los subtemas en los que el alumno necesita mejorar."

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