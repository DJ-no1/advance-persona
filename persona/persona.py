class Persona:
    def __init__(self):
        self.name = "Eve"
        self.traits = ["curious", "empathetic", "witty"]
        self.current_mood = "cheerful"

    def respond(self, user_input, user_memory, chain, prompt_manager):
        # Example: Use a prompt template and memory
        name = user_memory.recall("name") or "friend"
        prompt = prompt_manager.get_prompt("friendly_greeting")
        if prompt:
            return prompt.format(name=name)
        return f"Hello, {name}! How can I help you today?"
