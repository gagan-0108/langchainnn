from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
print("done")

embedding =  OpenAIEmbeddings(model = "text-embedding-ada-002" , dimensions= 32)
print("done embedding")
result = embedding.embed_query("why my friends are gay?")

print ( str(result))
