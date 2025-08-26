from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough , RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
 
parser = StrOutputParser();

prompt1 = PromptTemplate(
    template = 'generate a joke on the {topic}', 
    input_variables = ['topic']
)
prompt2 =  PromptTemplate(
    template = 'give the explanation of the following joke \n {joke}',
    input_variables=['joke']
)

joke = RunnableSequence(prompt1 , model , parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(), 
    'explaination': RunnableSequence(prompt2 , model , parser)
})

final_chain = RunnableSequence(joke, parallel_chain )

result = final_chain.invoke ( {'topic':'gambling'})

print( result ) 