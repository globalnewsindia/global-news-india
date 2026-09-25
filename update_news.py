import json
import html
import feedparser
from pathlib import Path


RSS_URL = "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=2&Regid=3"

OUTPUT_FILE = Path("news.js")

DEFAULT_IMAGE = (
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c"
    "?auto=format&fit=crop&w=1200&q=80"
)


def clean_text(text):
    if not text:
        return ""

    text = html.unescape(text)

    return " ".join(text.split())


def make_category(title):
    title_lower = title.lower()

    if any(word in title_lower for word in [
        "technology", "digital", "internet", "ai", "artificial intelligence"
    ]):
        return "टेक्नोलॉजी"

    if any(word in title_lower for word in [
        "economy", "business", "trade", "industry", "investment"
    ]):
        return "बिजनेस"

    return "भारत"


def main():

    feed = feedparser.parse(RSS_URL)

    news_items = []

    for index, item in enumerate(feed.entries[:12]):

        title = clean_text(item.get("title", ""))

        if not title:
            continue

        link = item.get("link", "")

        published = clean_text(
            item.get("published", "")
            or item.get("updated", "")
        )

        category = make_category(title)

        news_items.append({
            "id": f"pib-{index + 1}",
            "category": category,
            "title": title,
            "date": published,
            "source": "Press Information Bureau (PIB)",
            "sourceUrl": link,
            "image": DEFAULT_IMAGE,
            "body": (
                "यह खबर Press Information Bureau (PIB) "
                "के आधिकारिक स्रोत से ली गई है। "
                "पूरी जानकारी के लिए मूल स्रोत देखें।"
            )
        })


    if not news_items:
        print("No news found. Keeping existing news.js.")
        return


    javascript = (
        "const NEWS = "
        + json.dumps(news_items, ensure_ascii=False, indent=2)
        + ";\n"
    )

    OUTPUT_FILE.write_text(
        javascript,
        encoding="utf-8"
    )

    print(f"Updated {len(news_items)} news items.")


if __name__ == "__main__":
    main()
