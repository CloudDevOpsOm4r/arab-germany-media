import json
from pathlib import Path

from ai.provider import AI


INPUT_FILE = Path("ai/scored_news.json")
OUTPUT_FILE = Path("ai/final_news.json")
ERROR_FILE = Path("ai/analyze_errors.json")


def main():
    if not INPUT_FILE.exists():
        print(f"File not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        news_list = json.load(f)

    results = []
    errors = []

    total = len(news_list)

    for index, news in enumerate(news_list, start=1):
        print(f"[{index}/{total}] Analyzing: {news.get('title')}")

        try:
            analyzed = AI.analyze_news(news)

            analyzed["original_title"] = news.get("title")
            analyzed["source"] = news.get("source")
            analyzed["link"] = news.get("link")
            analyzed["published"] = news.get("published")

            results.append(analyzed)

        except Exception as e:
            errors.append({
                "title": news.get("title"),
                "link": news.get("link"),
                "error": str(e),
            })
            print(f"Error: {e}")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    with open(ERROR_FILE, "w", encoding="utf-8") as f:
        json.dump(errors, f, ensure_ascii=False, indent=2)

    print()
    print("Finished.")
    print(f"Saved {len(results)} analyzed news to {OUTPUT_FILE}")
    print(f"Saved {len(errors)} errors to {ERROR_FILE}")


if __name__ == "__main__":
    main()