from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI( model = 'gemini-2.5-flash')

messages = [
    SystemMessage(content = "you are brutally honest"),
    HumanMessage(content="What's the future of AI?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)