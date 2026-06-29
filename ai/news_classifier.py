import json

INPUT_FILE = "ai/scored_news.json"
OUTPUT_FILE = "ai/classified_news.json"


def classify_item(item: dict) -> dict:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()

    if any(word in text for word in ["hitze", "hitzewelle", "hitzeschutz", "klimaanlagen"]):
        category = "weather_health_warning"
        arabic_category = "تحذير طقس وصحة"
        video_type = "quick_warning"
    elif any(word in text for word in ["bürgergeld", "kindergeld", "wohngeld"]):
        category = "financial_support"
        arabic_category = "مساعدات مالية"
        video_type = "explainer"
    elif any(word in text for word in ["aufenthalt", "einbürgerung", "visum"]):
        category = "residence_citizenship"
        arabic_category = "إقامة وجنسية"
        video_type = "explainer"
    else:
        category = "general_important"
        arabic_category = "خبر مهم"
        video_type = "short_news"

    item["category"] = category
    item["arabic_category"] = arabic_category
    item["video_type"] = video_type

    return item


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    news = json.load(f)

classified = [classify_item(item) for item in news]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(classified, f, ensure_ascii=False, indent=2)

print(f"Classified News: {len(classified)}")