from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(
    template = 'My name is {name} and I am {age} year old, write random five lines about the person base on their name' ,
    input_variables= ['name','age']
)

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen3-1.7B",
    task = 'text generation',
    pipeline_kwargs= dict(
        temperature = 1, 
        max_new_tokens = 100
    )
)

parser = StrOutputParser()
chain = prompt | llm | parser 
result = chain.invoke({'name':'gagan' , 'age':20})

print( result )