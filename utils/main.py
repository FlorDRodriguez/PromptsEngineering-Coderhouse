from utils.env import TYPE_AI
from utils.openai import tutoria_openai
from utils.gemini import tutoria_gemini
 
def tutoria(tema, grado, nivel):
    if TYPE_AI == "openai":
        return tutoria_openai(tema, grado, nivel)
    elif TYPE_AI == "gemini":
        return tutoria_gemini(tema, grado, nivel)
    else:
        return "No se ha definido un tipo de IA"