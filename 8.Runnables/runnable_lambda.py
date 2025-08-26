from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough , RunnableParallel, RunnableSequence, RunnableLambda
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/langchainnnn/.env")

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
 
parser = StrOutputParser();
prompt= PromptTemplate(
    template = 'generate a joke on the {topic}', 
    input_variables = ['topic']
)

def word_count(text):
    return len(text.split())

joke_generate = RunnableSequence(prompt, model , parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_Count': RunnableLambda( word_count ) 
})

final_chain = RunnableSequence(joke_generate, parallel_chain)
# joke_generate = RunnableSequence({
#     'joke': RunnablePassthrough()
#     'word_Count': RunnableLambda( lambda x: len(x.split())) 
# })

result = final_chain.invoke( {'topic':'AI'})

final_result = """ {} \n word count -> {} """.format ( result['joke'], result ['word_Count'])
print(final_result)