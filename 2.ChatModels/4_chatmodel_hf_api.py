from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-1.7B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("seduce me")

print(result.content)