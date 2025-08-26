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
#! runnable parallel will execute tweet and linkedin at the same time and with the same invoke function

result = parallel_chain.invoke({'topic':'AI'})
#?  now the topic "AI" will act as input in both tweet and linkedin- inside the runnable parallels 

print( result)