from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI( model = 'gemini-2.5-flash')

chatHistory = [
    SystemMessage(content="You are burtally honest")
]

while True: 
    user_input = input("You: ")
    chatHistory.append(HumanMessage(content=user_input))
    if user_input.lower().strip() == "exit":
        break;
    
    result = model.invoke(chatHistory)
    chatHistory.append(AIMessage(content=result.content))
    print("Astrotalk: ",result.content)

print(chatHistory)