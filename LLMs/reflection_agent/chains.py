from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY

# template para agent validador
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral Twitter influencer grading a tweet. Generate critique and recommendation for the user's tweet."
            " Always provide detailed recommendations, including requests for lenght, virality, style, etc."

        ),
        MessagesPlaceholder(variable_name= "messages"), # <-- Guarda el saco de mesajes: genrados , objetivo.
    ]
)

# template para agent generador 
generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influence assistant tasked with writing excellent twitter posts."
            "Generate the best  twitter post possible for the user's request."
            "If the user provides critique, respond with a revised version of your previous attempts.",

        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key= OPENAI_API_KEY,
    temperature=0, 
)   

# creamos la cadena promp unido con llm elegido.
generate_chain = generation_prompt | llm

# creamos cadena para reflection agent.
reflect_chain = reflection_prompt | llm