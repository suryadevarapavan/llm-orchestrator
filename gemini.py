from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def gemini(question):
    load_dotenv()
    model_name = "models/gemini-2.5-flash"
    
    model = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        transport="rest",
        temperature=0.7,
        max_retries=2
    )
    response = model.invoke(question)
    print(f"\n[Gemini Response]: {response.content}")
    return response.content  
