import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from ai.providers.base import AIProvider

load_dotenv()


class OpenAIProvider(AIProvider):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in .env")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.prompt_path = Path("ai/prompts/editor_prompt.txt")

    def analyze_news(self, news_item: dict) -> dict:
        editor_prompt = self.prompt_path.read_text(encoding="utf-8")

        user_input = f"""
News item:

Title: {news_item.get("title", "")}
Summary: {news_item.get("summary", "")}
Link: {news_item.get("link", "")}
Source: {news_item.get("source", "")}
Published: {news_item.get("published", "")}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": editor_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content.strip()
        return json.loads(content)