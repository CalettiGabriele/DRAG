import os
import re
from abc import abstractmethod

import pandas as pd
from groq import Groq

from ..base.base import Drag


class Groq_Chat(Drag):
    def __init__(self, config=None):
        Drag.__init__(self, config=config)

        if "api_key" in config:
            self.client = client = Groq(api_key=config["api_key"])

    def submit_prompt(self, prompt, model="mixtral-8x7b-32768", temperature=0, **kwargs) -> str:
        if prompt is None:
            raise Exception("Prompt is None")
        if len(prompt) == 0:
            raise Exception("Prompt is empty")
        
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.,
        )

        return chat_completion.choices[0].message.content
    
    def clear_llm_response(self, prompt, **kwargs):
        prompt = prompt.replace("```", "")
        prompt = prompt.replace("python", "")
        prompt = prompt.strip()
        return prompt