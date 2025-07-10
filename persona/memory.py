class UserMemory:
    def __init__(self):
        self.data = {
            "name": None,
            "preferences": {},
            "conversation_history": [],
            "important_dates": {},
        }

    def remember(self, key, value):
        self.data[key] = value

    def recall(self, key):
        return self.data.get(key)

    def add_to_history(self, message):
        self.data["conversation_history"].append(message)
