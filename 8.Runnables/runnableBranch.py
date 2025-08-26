from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough , RunnableParallel, RunnableSequence, RunnableBranch
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
 
parser = StrOutputParser();

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

report_generate =  RunnableSequence(prompt1, model , parser)

branch_chain = RunnableBranch(
    ( lambda x: len(x.split())>100 , RunnableSequence(prompt2, model , parser) ),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generate, branch_chain)

result = final_chain.invoke({'topic': 'pollution in india'})

print( result)