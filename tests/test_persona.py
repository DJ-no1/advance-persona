import unittest
from persona.memory import UserMemory
from persona.chain_of_thought import ChainOfThought
from persona.persona import Persona
from persona.prompt_manager import PromptManager

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.memory = UserMemory()
        self.chain = ChainOfThought()
        self.persona = Persona()
        self.prompt_manager = PromptManager("prompts/")

    def test_greeting(self):
        self.memory.remember("name", "TestUser")
        self.chain.start("Hello!")
        response = self.persona.respond("Hello!", self.memory, self.chain, self.prompt_manager)
        self.assertIn("TestUser", response)

if __name__ == "__main__":
    unittest.main()
