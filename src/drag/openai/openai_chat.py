import os
import re
from abc import abstractmethod

import pandas as pd
from openai import OpenAI

from ..base.base import Drag


class OpenAI_Chat(Drag):
    def __init__(self, file_path, client=None, config=None):
        Drag.__init__(self, file_path)

        if client is not None:
            self.client = client
            return

        if config is None and client is None:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            return

        if "api_type" in config:
            raise Exception(
                "Passing api_type is now deprecated. Please pass an OpenAI client instead."
            )

        if "api_base" in config:
            raise Exception(
                "Passing api_base is now deprecated. Please pass an OpenAI client instead."
            )

        if "api_version" in config:
            raise Exception(
                "Passing api_version is now deprecated. Please pass an OpenAI client instead."
            )

        if "api_key" in config:
            self.client = OpenAI(api_key=config["api_key"])

    def system_message(self, message: str) -> any:
        return {"role": "system", "content": message}

    def user_message(self, message: str) -> any:
        return {"role": "user", "content": message}

    def assistant_message(self, message: str) -> any:
        return {"role": "assistant", "content": message}

    def submit_prompt(self, prompt, **kwargs) -> str:
        if prompt is None:
            raise Exception("Prompt is None")

        if len(prompt) == 0:
            raise Exception("Prompt is empty")

        # Count the number of tokens in the message log
        num_tokens = 0
        for message in prompt:
            num_tokens += (
                len(message["content"]) / 4
            )  # Use 4 as an approximation for the number of characters per token

        if self.config is not None and "engine" in self.config:
            print(
                f"Using engine {self.config['engine']} for {num_tokens} tokens (approx)"
            )
            response = self.client.chat.completions.create(
                engine=self.config["engine"],
                messages=prompt,
                max_tokens=500,
                stop=None,
                temperature=0.7,
            )
        elif self.config is not None and "model" in self.config:
            print(
                f"Using model {self.config['model']} for {num_tokens} tokens (approx)"
            )
            response = self.client.chat.completions.create(
                model=self.config["model"],
                messages=prompt,
                max_tokens=500,
                stop=None,
                temperature=0.7,
            )
        else:
            if num_tokens > 3500:
                model = "gpt-3.5-turbo-16k"
            else:
                model = "gpt-3.5-turbo"

            print(f"Using model {model} for {num_tokens} tokens (approx)")
            response = self.client.chat.completions.create(
                model=model, messages=prompt, max_tokens=500, stop=None, temperature=0.7
            )

        for (
            choice
        ) in (
            response.choices
        ):  # Find the first response from the chatbot that has text in it (some responses may not have text)
            if "text" in choice:
                return choice.text

        return response.choices[
            0
        ].message.content  # If no response with text is found, return the first response's content (which may be empty)
