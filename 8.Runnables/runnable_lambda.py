 from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough , RunnableParallel, RunnableSequence, RunnableLambda
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
 
parser = StrOutputParser();