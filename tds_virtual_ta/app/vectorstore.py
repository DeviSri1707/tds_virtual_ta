import json
from difflib import get_close_matches

DATA_PATH = "data/discourse_data.json"

def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def search_relevant_content(query):
    posts = load_data()
    combined_texts = [" ".join((p["title"], p["content"])) for p in posts]
    matches = get_close_matches(query, combined_texts, n=3, cutoff=0.3)

    result = ""
    for m in matches:
        for post in posts:
            if m in post["content"]:
                result += f"\nPost: {post['title']}\n{post['content']}\nLink: {post['url']}\n"

    return result
