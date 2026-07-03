import os
from dotenv import load_dotenv
from groq import Groq
from services.chatbot_services.prompt import SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

client = Groq(api_key=API_KEY)

def generate_response(
    question,
    context
):
    if not context.strip():
        return "I couldn't find that information in the current inventory data."
    messages = [

    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },

    {
        "role": "user",
        "content": f"""
Inventory Context:

{context}

User Question:

{question}
"""
    }

]
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.1,
            max_tokens=600
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating response: {e}"