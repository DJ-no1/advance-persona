from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

# Initialize Google Generative AI chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash" )

# Define the prompt template

prompt = load_prompt("prompts/day2.json")


chain = prompt | llm

conversation_history = []


while True:
    user_message = input("You: ")
    if user_message == "exit":
        print("Exiting the conversation.")
        print(f"Conversation History:" + str(conversation_history))
        break
    else:
        current_time = "5:36 PM"  
        result = chain.invoke({"User": user_message, "Time": current_time }, conversation_history=conversation_history)
        print("Persona:", result.content)

    # Update conversation history
    conversation_history.append({"User": user_message, "Time": current_time, "Response": result.content})
