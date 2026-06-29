import json
from datetime import datetime
from pathlib import Path

INPUT_FILE = Path("publish/review_queue.json")
OUTPUT_DIR = Path("media/packages")


def build_package(item: dict, index: int) -> dict:
    package_id = f"{datetime.now().strftime('%Y%m%d')}-{index:03d}"

    return {
        "id": package_id,
        "status": "ready",
        "priority": item.get("importance", 0),
        "category": item.get("category", "general"),
        "source": {
            "title": item.get("original_title", ""),
            "url": item.get("link", ""),
            "publisher": item.get("source", ""),
            "published": item.get("published", ""),
        },
        "video": {
            "title": item.get("title_ar", ""),
            "hook": item.get("title_ar", ""),
            "script": item.get("script_ar", ""),
            "duration": 55,
            "voice": "Hijazi",
            "music": "soft_news",
            "style": "news",
        },
        "social": {
            "caption": item.get("summary_ar", ""),
            "hashtags": item.get("hashtags", []),
        },
        "production": {
            "voice_ready": False,
            "video_ready": False,
            "thumbnail_ready": False,
            "published": False,
        },
    }


def main():
    if not INPUT_FILE.exists():
        print(f"File not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        items = json.load(f)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for index, item in enumerate(items, start=1):
        package = build_package(item, index)
        output_file = OUTPUT_DIR / f"{package['id']}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)

        print(f"Created package: {output_file}")

    print(f"Total packages created: {len(items)}")


if __name__ == "__main__":
    main()