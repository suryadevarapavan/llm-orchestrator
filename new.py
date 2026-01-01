from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def gpt(question):
    load_dotenv()
    model = ChatOpenAI(model="gpt-4o-mini")
    response = model.invoke(question)
    print(f"\n[GPT Response]: {response.content}")
    return response.content  
