from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel , RunnableBranch , RunnableLambda
from dotenv import load_dotenv , find_dotenv 
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import Field, BaseModel
from typing import Literal

load_dotenv(dotenv_path='/Users/gagan/Desktop/langchainnnn/.env')

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

class Feedback( BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(
    template= "Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}",
    input_variables= {'feedback'},
    partial_variables= {'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template= "Write an approriate response to this positive Feedback\n {Feedback}",
    input_variables= ['Feedback']
)

prompt3 = PromptTemplate(
    template= "Write an approriate response to this negative Feedback\n {Feedback}",
    input_variables= ['Feedback']
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke ( {'feedback':'This is a wonderful smartphone'}).sentiment

# print ( result)

branh_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find the sentiment")
)

chain = classifier_chain | branh_chain

result = chain.invoke({'feedback':'this is the a nice phone'})

print( result)