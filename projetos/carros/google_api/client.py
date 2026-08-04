import logging

import google.generativeai as genai
from django.conf import settings

logger = logging.getLogger(__name__)

PROMPT = (
    'Escreva uma descricao curta e vendedora, de no maximo 250 caracteres, '
    'para o carro {brand} {model}, ano {year}. '
    'Responda em portugues do Brasil, sem usar titulos ou listas.'
)

def get_car_ai_bio(model, brand, year):
    if not settings.GEMINI_API_KEY:
        logger.warning('GEMINI_API_KEY nao configurada, bio nao sera gerada.')
        return None

    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        gemini = genai.GenerativeModel(settings.GEMINI_MODEL)
        response = gemini.generate_content(
            PROMPT.format(brand=brand, model=model, year=year)
        )
        return response.text.strip()
    except Exception:
        logger.exception('Falha ao gerar bio no Gemini para %s %s.', brand, model)
        return None
