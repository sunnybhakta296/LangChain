from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import sys
import time
from dotenv import load_dotenv

# Set your Groq API key (consider using environment variables for security)
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Language Models
model = init_chat_model("llama-3.1-8b-instant", model_provider="groq")
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]
final_result = model.invoke(messages)
print("Final Result:")
print(final_result.content)

sys.stdout.flush()
time.sleep(0.5)


# Prompt Templates
system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})
prompt.to_messages()

response = model.invoke(prompt)
print("Prompt Template Result:")
print(response.content)