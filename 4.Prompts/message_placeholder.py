from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

chatTemplate = ChatPromptTemplate(
    [
        ('system', 'you are the customer support agent'),
        MessagesPlaceholder(variable_name='chatHistory'),
        ('human', '{query}')
    ]
)

#! loading chats from .txt file 
chatHistory = []
with open ( 'chatHistory.txt' ) as file:
    chatHistory.append(file.readlines())


#! Creating prompts
query = "Where is my refund? "
prompt = chatTemplate.invoke({'chatHistory':chatHistory, 'query': query} )