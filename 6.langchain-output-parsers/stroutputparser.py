from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#prompt1 --> detailed report 

template1= PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)
 
 #prompt2 --> to  generate summary

template2 = PromptTemplate (
    template = 'Write a 5 line summary on this given text. /n {text}',
    input_variables = ['text']
)


#now we are sending prompt to the llm 

prompt1= template1.invoke({'topic': 'poverty'});

result=  model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print ( result2.content)

