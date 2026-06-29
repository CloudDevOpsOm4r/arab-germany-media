from ai.providers.base import AIProvider


class OpenAIProvider(AIProvider):
    def analyze_news(self, news_item: dict) -> dict:
        return {
            "provider": "openai",
            "publish": False,
            "importance": 0,
            "reason": "OpenAI provider not connected yet",
            "title": news_item.get("title", ""),
        }