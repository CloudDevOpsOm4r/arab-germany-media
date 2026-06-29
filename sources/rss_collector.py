import json
from datetime import datetime, UTC
import feedparser
from rich.console import Console

console = Console()

RSS_URL = "https://www.tagesschau.de/xml/rss2"
OUTPUT_FILE = "sources/news.json"


def main():
    feed = feedparser.parse(RSS_URL)

    news_items = []

    for entry in feed.entries:
        news_items.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "source": feed.feed.get("title", "Unknown"),
            "collected_at": datetime.now(UTC).isoformat()
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(news_items, f, ensure_ascii=False, indent=2)

    console.print(f"[bold green]Saved:[/bold green] {len(news_items)} items to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()