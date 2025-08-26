from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

prompt1 = PromptTemplate(
    template="write a joke about {topic}", 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template=" Explain the following joke \n {joke}",
    input_variables=['joke']
)
model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model , parser , prompt2, model , parser )

print(chain.invoke ( {'topic': 'AI'}))