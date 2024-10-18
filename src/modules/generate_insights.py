import google.generativeai as genai
from pandas import DataFrame
import os

def generate_insights(data: DataFrame):
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"O dataset a seguir corresponse a metricas de negócio de uma operação de suporte. Me informe 5 insights sobre este dataset. {data}"
    response = model.generate_content(prompt)
    return response
        
