import google.generativeai as genai
from pandas import DataFrame
import os


def generate_insights(data: DataFrame) -> str:
    """
    Generate insights from a dataset using GPT-3.

    Args:
        data (DataFrame): The dataset to generate insights from.

    Returns:
        str: Returns the generated insights.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"O dataset a seguir corresponse a metricas de negócio de uma operação de suporte. Me informe 5 insights sobre este dataset. {data}"
    response = model.generate_content(prompt)
    return response
