import json
import inspect

from .llms import Llm

class Rag(Llm):
    def __init__(self, drag_setup) -> None:
        super().__init__(drag_setup)

    def execute_prompt(self, prompt, **kwargs):
        with open(prompt, 'r') as file:
            prompt = json.load(file)
            completed_prompt = prompt['prompt'][-1]['content'] % tuple(kwargs.values())
            prompt['prompt'][-1]['content'] = completed_prompt
            return self.submit_prompt(prompt= prompt['prompt'])

    def similarity(self):
        pass
    
    def retrival(self):
        pass

    def web_scrape(self):
        pass