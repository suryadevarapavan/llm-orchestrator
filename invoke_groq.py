from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

def grok(question):
    load_dotenv()
    groq = ChatGroq(
        model="qwen/qwen3-32b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2
    )
    response = groq.invoke(question)
    print(f"\n[Groq Response]: {response.content}")
    return response.content  
