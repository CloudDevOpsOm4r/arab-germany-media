import json

KEYWORDS = [
    "aufenthalt",
    "einbürgerung",
    "staatsangehörigkeit",
    "bamf",
    "visum",
    "bürgergeld",
    "kindergeld",
    "wohngeld",
    "deutsche bahn",
    "streik",
    "hitze",
    "warnung",
    "polizei",
    "migration",
    "integration",
]

with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

filtered = []

for item in news:
    text = (
        item["title"] + " " + item["summary"]
    ).lower()

    if any(keyword in text for keyword in KEYWORDS):
        filtered.append(item)

with open("filtered_news.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f"Total News: {len(news)}")
print(f"Relevant News: {len(filtered)}")