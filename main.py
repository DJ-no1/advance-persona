from persona.memory import UserMemory
from persona.chain_of_thought import ChainOfThought
from persona.persona import Persona
from persona.prompt_manager import PromptManager
from utils.timer import IdleTimer

# Example usage
if __name__ == "__main__":
    user_memory = UserMemory()
    chain = ChainOfThought()
    persona = Persona()
    prompt_manager = PromptManager("prompts/")
    idle_timer = IdleTimer(timeout=60)

    print("Persona Bot started. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        idle_timer.reset()
        chain.start(user_input)
        thoughts = chain.get_thoughts()
        for t in thoughts:
            print(f"[Thought] {t}")
        response = persona.respond(user_input, user_memory, chain, prompt_manager)
        print(f"Bot: {response}")
