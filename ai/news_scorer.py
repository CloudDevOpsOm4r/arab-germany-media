import json
import re

HIGH_VALUE = [
    "aufenthalt",
    "einbürgerung",
    "staatsangehörigkeit",
    "bürgergeld",
    "kindergeld",
    "wohngeld",
    "migration",
    "integration",
    "visum",
]

MEDIUM_VALUE = [
    "hitze",
    "hitzeschutz",
    "hitzewelle",
    "rekordtemperaturen",
    "warnung",
    "polizei",
    "streik",
    "deutsche bahn",
    "gesundheit",
    "schule",
    "miete",
    "klimaanlagen",
]

LOW_VALUE = [
    "klima",
    "tiny forest",
    "börse",
    "dax",
    "sport",
    "podcast",
]


def contains_word(text: str, word: str) -> bool:
    pattern = r"\b" + re.escape(word) + r"\b"
    return re.search(pattern, text, re.IGNORECASE) is not None


def calculate_score(item: dict) -> int:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    score = 0

    for word in HIGH_VALUE:
        if contains_word(text, word):
            score += 30

    for word in MEDIUM_VALUE:
        if contains_word(text, word):
            score += 15

    for word in LOW_VALUE:
        if contains_word(text, word):
            score -= 20

    return max(0, min(score, 100))


with open("sources/news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

scored_news = []

for item in news:
    score = calculate_score(item)
    item["score"] = score

    if score >= 30:
        scored_news.append(item)

scored_news = sorted(scored_news, key=lambda x: x["score"], reverse=True)

with open("ai/scored_news.json", "w", encoding="utf-8") as f:
    json.dump(scored_news, f, ensure_ascii=False, indent=2)

print(f"Total News: {len(news)}")
print(f"Scored Relevant News: {len(scored_news)}")