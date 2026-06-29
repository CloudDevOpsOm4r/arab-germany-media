from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def analyze_news(self, news_item: dict) -> dict:
        pass