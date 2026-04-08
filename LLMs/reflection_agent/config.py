import logging
import os

from dotenv import load_dotenv

# Cargamos claves al entorno.
load_dotenv()

# recuperamos claves del entorno.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logging.error("No se encontro token valido para openAI")

LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")


if __name__ == "__main__":
    print(f"openai api key:{OPENAI_API_KEY}")