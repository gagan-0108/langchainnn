from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = 'fact_1' , description="Most crazy fact about the topic"),
    ResponseSchema(name = 'fact_2' , description="less crazy "),
    ResponseSchema(name = 'fact_3' , description="boring fact about the topic "),    
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about the {topic} /n {format_intruction} ',
    input_variables= ["topic"],
    partial_variables= {'format_intruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'blackhole'})

# result = model.invoke(prompt)
# finalResult = parser.parse(result.content)
# print(finalResult)

chain = template | model | parser

result = chain.invoke({'topic':'blackhole'})
print ( result)