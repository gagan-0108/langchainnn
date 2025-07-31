from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline



llm = HuggingFacePipeline.from_model_id(
    model_id= "HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation",
    pipeline_kwargs= dict(
        temperature = 1, 
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm= llm)

result = model.invoke( "no hindi only kannada")

print ( result.content)
 