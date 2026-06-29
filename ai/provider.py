from ai.providers.openai_provider import OpenAIProvider


class AI:
    provider = OpenAIProvider()

    @classmethod
    def analyze_news(cls, news_item: dict) -> dict:
        return cls.provider.analyze_news(news_item)