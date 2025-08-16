from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name : str = Field(description="Name of the person ")
    age : int = Field( gt=18 , description="Age of the person")
    city: str = Field( description="Person's city")

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template= "Generate a sotry of peson with a name age city in 5 lines of {country} person\n {format_intruction}",
    input_variables= ['country'],
    partial_variables={ "format_intruction" : parser.get_format_instructions()}
    )

# prompt = template.format({'country':'india'})
# result = prompt.invoke () 
# finalResult = parser.parse(result.content)
#using chain 
chain = template | model | parser
final_result = chain.invoke({'country':'assam'})

print ( final_result) 