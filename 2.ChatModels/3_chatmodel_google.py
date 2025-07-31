from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI( model = 'gemini-2.5-flash')

result = model.invoke('what will happen if bihar removed from India?')
print (result.content)