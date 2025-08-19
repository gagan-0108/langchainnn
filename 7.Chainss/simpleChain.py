from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

prompt = PromptTemplate(
    template = 'My name is {name} and I am {age} year old, write random five lines about the person',
    input_variables= ['name','age'],
    
)

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
parse = StrOutputParser()
chain = prompt | model | parse
result = chain.invoke({'name':'Gagan', 'age':20})

print(result)