from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke("why girls in my college is not attractive/beautiful?")

print(result.content)

