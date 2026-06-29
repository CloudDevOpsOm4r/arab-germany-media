import json
from pathlib import Path

from ai.provider import AI


PROMPT_FILE = Path("ai/prompts/storyboard_prompt.txt")
PACKAGES_DIR = Path("media/packages")


def generate_storyboard(package: dict) -> dict:
    prompt = PROMPT_FILE.read_text(encoding="utf-8")

    news_item = {
        "title": package["video"]["title"],
        "summary": package["social"]["caption"],
        "script": package["video"]["script"],
        "category": package.get("category", "general"),
        "source_title": package["source"]["title"],
        "link": package["source"]["url"],
        "custom_prompt": prompt,
    }

    return AI.analyze_news(news_item)


def main():
    packages = sorted(PACKAGES_DIR.glob("*.json"))

    if not packages:
        print("No packages found.")
        return

    for package_file in packages:
        print(f"Generating storyboard: {package_file.name}")

        with open(package_file, "r", encoding="utf-8") as f:
            package = json.load(f)

        result = generate_storyboard(package)

        package["video"]["storyboard"] = result.get("storyboard", [])

        with open(package_file, "w", encoding="utf-8") as f:
            json.dump(package, f, ensure_ascii=False, indent=2)

        print(f"Scenes: {len(package['video']['storyboard'])}")

    print("Storyboards generated.")


if __name__ == "__main__":
    main()