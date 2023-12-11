#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv

class TranscriptorGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=self.api_key
        )

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "Bullet points of a transcript"

    #def request_openai(self, message, role="system"):
    def sound_to_text_openai(self, audio_path):
        """
        Make a request to the OpenAI API.

        Args:
        - audio_path (str): The path to the audio to be transcripted by OpenAI API

        Returns:
        - str: OpenAI API audio transcription
        """
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=open(audio_path, "rb"),
            language="en"
        )
        return transcript.text