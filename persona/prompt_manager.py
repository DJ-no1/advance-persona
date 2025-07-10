import os

class PromptManager:
    def __init__(self, prompt_dir):
        self.prompt_dir = prompt_dir
        self.prompts = {}
        self.load_prompts()

    def load_prompts(self):
        for filename in os.listdir(self.prompt_dir):
            if filename.endswith('.txt'):
                key = filename[:-4]
                with open(os.path.join(self.prompt_dir, filename), 'r', encoding='utf-8') as f:
                    self.prompts[key] = f.read()

    def get_prompt(self, key):
        return self.prompts.get(key)
