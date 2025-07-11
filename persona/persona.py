from langchain_google_genai import GoogleGenerativeAI

# Initialize Google Generative AI chat model
llm = GoogleGenerativeAI(model="gemini-2.0-flash" )

# Define the prompt template

prompt = ("../prompts/girl_persona.json")

response = llm.generate(prompt)

userinput = "Hello, how are you?"
chain = 

response = llm.generate(userinput)