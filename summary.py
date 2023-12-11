#!/usr/bin/env python3
from chatGPT import ChatGPT


class SummaryGPT(ChatGPT):
    def summary_openai(self, text):
        """
        Make a request to the OpenAI API.

        Args:
        - text (str): The text to be sent to the OpenAI API to extract the main topic

        Returns:
        - str: The response content from the OpenAI API, which is going to be the main topic of the given text.
        """

        return ChatGPT.system_user_request_openai(self, "You can extract one main topic of a given text", text)