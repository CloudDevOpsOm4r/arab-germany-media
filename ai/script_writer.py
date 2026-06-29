import json

INPUT_FILE = "ai/classified_news.json"
OUTPUT_FILE = "ai/video_scripts.json"


def write_script(item: dict) -> dict:
    title = item.get("title", "")
    summary = item.get("summary", "")
    category = item.get("arabic_category", "خبر مهم")
    source = item.get("source", "")
    link = item.get("link", "")

    script = f"""
{category}

في ألمانيا يوجد خبر مهم اليوم.

الخبر يقول:
{title}

المعنى ببساطة:
{summary}

لماذا يهمك؟
لأن هذا الموضوع قد يؤثر على حياتك اليومية في ألمانيا، خصوصًا إذا كنت تعيش هنا مع عائلتك.

تابعنا حتى تصلك أهم الأخبار التي تهم العرب في ألمانيا بدون تعقيد.

المصدر: {source}
""".strip()

    return {
        "title": title,
        "category": item.get("category"),
        "arabic_category": category,
        "video_type": item.get("video_type"),
        "score": item.get("score"),
        "script": script,
        "source_link": link,
    }


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    news = json.load(f)

scripts = [write_script(item) for item in news]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(scripts, f, ensure_ascii=False, indent=2)

print(f"Video Scripts: {len(scripts)}")