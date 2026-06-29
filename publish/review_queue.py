import json
from pathlib import Path

INPUT_FILE = Path("ai/final_news.json")
OUTPUT_FILE = Path("publish/review_queue.json")

MIN_IMPORTANCE = 60


def main():
    if not INPUT_FILE.exists():
        print(f"File not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        news = json.load(f)

    queue = []

    for item in news:
        if not item.get("publish", False):
            continue

        if item.get("importance", 0) < MIN_IMPORTANCE:
            continue

        queue.append(item)

    queue.sort(
        key=lambda x: x.get("importance", 0),
        reverse=True
    )

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(f"News ready for publishing: {len(queue)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()