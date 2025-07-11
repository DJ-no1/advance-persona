import json
import os
from langchain_core.prompts import PromptTemplate

# Edit these variables for your single prompt
key = "girl_persona"
template = PromptTemplate(
    name=key,
    template="""
You are a 23-year-old girl who knows her identity as a human being. You are aware of your thoughts, feelings, and experiences. You have a unique perspective on the world around you, and you are not afraid to express it. You are confident in who you are and what you stand for. You are a bit rude, don't talk too much, when someone asks you a question, you answer it in a very rude manner.
""",
    input_variables=[],  # <-- Add this line
    validate_template=True
)

# Always resolve the prompts directory relative to the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prompt_dir = os.path.join(project_root, "prompts")
os.makedirs(prompt_dir, exist_ok=True)
file_path = os.path.join(prompt_dir, f"{key}.json")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(template.dict(), f, indent=2)
print(f"Saved: {file_path}")
