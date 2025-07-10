class ChainOfThought:
    def __init__(self):
        self.thoughts = []

    def start(self, user_input):
        self.thoughts = [
            f"Received input: {user_input}",
            "Analyzing intent...",
            "Checking memory/context...",
            "Formulating response..."
        ]

    def get_thoughts(self):
        return self.thoughts
