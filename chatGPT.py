#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(
            api_key=self.api_key
        )

    def system_user_request_openai(self, system_definition, user_msg, role1="system", role2="user"):
        """
        Make a request to the OpenAI API, given a system definition and a user request .

        Args:
        - system_definition (str): The behavior the system will take.
        - user_msg (str, optional): The query for the user.
        - role1 (str, optional): The role associated with the system message
        - role2 (str):The role associated with the user message

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": role1,"content": system_definition},{"role": role2,"content": user_msg}]
        )

        # Return the message content from the API response
        return response.model_dump()["choices"][0]["message"]["content"]