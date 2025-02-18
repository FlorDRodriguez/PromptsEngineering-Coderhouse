# TutorIA

**TutorIA** es una aplicación web que proporciona tutorías personalizadas a estudiantes de todas las edades y niveles educativos, utilizando IA para identificar fortalezas y debilidades y ofrecer contenido personalizado a las necesidades particulares.

## Funcionalidades

1. **Recopilación de dastos**: El usuario debe ingresar los datos iniciales (tema a reforzar, año que cursa y nivel educativo).
2. **Evaluación diagnóstica**: La IA proporciona una evaluación diagnóstica con sus respectivos puntajes para identificar temas puntuales que se necesitan mejorar.
3. **Resultados**: La IA proporcionar los resultados correctos de la evaluación para que el alumno pueda autocorregirse.
4. **Puntajes**: La IA proporciona una tabla de puntaje con una breve descripción identificando fortalezas y debilidades del estudiante.
5. **Plan de estudio**: La IA genera un plan de estudio personalizado que se adapta a las necesidades del estudiante, en el cual se incluyan ejercicios teóricos, prácticos, material de lectura y videos educativos.

## Requisitos

- Python
- OpenAI API Key (GPT-4) [Enlace](https://platform.openai.com/api-keys)
- Gemini API Key [Enlace](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419)
- Streamlit [Enlace](https://streamlit.io/)

## Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/FlorDRodriguez/PromptsEngineering-Coderhouse.git
  ```
2. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```
3. Crea un archivo .env y agrega las claves de API para OpenAI y Gemini:

  ```bash
  OPENAI_API_KEY = api_key_openai
  GEMINI_API_KEY = api_key_gemini
  TYPE_AI = gemini  # Cambia 'gemini' por 'openai' para usar OpenAI GPT-4o-mini
  ```
4. Ejecuta la aplicación:
  ```bash
  streamlit run app.py
  ```

## Uso

1. Abre la aplicación en tu navegador.
2. Ingresa el tema due necesitas reforzar.
3. Ingresa el año en el que se encuentra el tema.
4. Ingresa el nivel educativo (primario, secundario, terciario, universitario)
5. Haz clic en "Generar tutoría" para comenzar.


## Enlaces

- [Aplicación en Streamlit](https://tutoria-coder.streamlit.app/)
- [Repositorio en GitHub](https://github.com/FlorDRodriguez/PromptsEngineering-Coderhouse.git)
