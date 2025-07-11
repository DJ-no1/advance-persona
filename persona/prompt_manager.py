import os
import json
from langchain_core.prompts import PromptTemplate

class PromptManager:
    def __init__(self, prompt_dir):
        self.prompt_dir = prompt_dir
        self.prompts = {}
        self.load_prompts()

    def load_prompts(self):
        for filename in os.listdir(self.prompt_dir):
            if filename.endswith('.json'):
                key = filename[:-5]
                with open(os.path.join(self.prompt_dir, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.prompts[key] = PromptTemplate(**data)

    def get_prompt(self, key):
        return self.prompts.get(key)

    def save_prompt(self, key, input_variables, template, template_format="f-string"):
        data = {
            "input_variables": input_variables,
            "template": template,
            "template_format": template_format
        }
        file_path = os.path.join(self.prompt_dir, f"{key}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        # Also update in-memory
        self.prompts[key] = PromptTemplate(**data)
