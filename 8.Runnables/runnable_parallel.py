from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

prompt1 = PromptTemplate(
    template= 'generate a tweet about {topic}',
    input_variables='topic'
)
prompt2 = PromptTemplate(
    template = "genearte a linkedin post about {topic}" , 
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI( model = 'gemini-2.5-flash')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1 , model , parser), 
    'linkedin': RunnableSequence*(prompt2, model , parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print( result)