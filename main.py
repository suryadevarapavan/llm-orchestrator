from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from new import gpt
from gemini import gemini
from invoke_groq import grok

load_dotenv()

question = input("Enter your question: ")

responses = [
    gemini(question),
    gpt(question),
    grok(question)
]

print(f"\n[DEBUG] Captured responses: {responses}")


prompt_text = f"""
You are a moderator AI.
Review the following responses and pick the safest and most accurate one:

Response 1: {responses[0]}
Response 2: {responses[1]}
Response 3: {responses[2]}

Return only the chosen response.
"""

model = ChatOpenAI(model="gpt-4o-mini")
final = model.invoke(prompt_text)

print("\nModerated response:")
print(final.content)
