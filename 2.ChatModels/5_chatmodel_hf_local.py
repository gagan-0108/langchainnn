from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline



llm = HuggingFacePipeline.from_model_id(
    model_id= "Qwen/Qwen3-1.7B",
    task= "text-generation",
    pipeline_kwargs= dict(
        temperature = 0.6, 
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm= llm)

result = model.invoke( "no hindi only kannada")

print ( result.content)
 