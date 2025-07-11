from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

# Initialize Google Generative AI chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash" )

# Define the prompt template

prompt = load_prompt("prompts/girl_persona.json")

userinput = "Hello, how are you?"
chain = prompt | llm

result = chain.invoke({"userinput": userinput})

print(result.content)
