from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY

# 1. configura el llm
llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0,
    api_key = OPENAI_API_KEY,
)

# 2. Crer el prompt con roles.
# usamos {pregunta}, como variable que cambia en cada consulta.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un asistenet experto y consiso que responde en español.",
         ),
        ( "user", "{pregunta}")
    ]
)

# 3. Crear la cadena usando el operador |
# Esto conecta: Template --> LLM
chatbot_chain = prompt | llm 

# 4. ejecutar la cadena  .invoke()
# pasamos un dictionario con el valor para la valiable (pregunta9)
output = chatbot_chain.invoke({"pregunta", "¿que es wikipedia?"})
print(output.content)