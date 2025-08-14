from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me name age and city of a fictional person\n {format_intruction}',
    input_variables= [],
    partial_variables={ 'format_intruction': parser.get_format_instructions()}
)
prompt = template.format()

result = model.invoke();

finalResult = parser.parse(result.content)

print(finalResult)