import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from tqdm import tqdm

def fetch_post_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.title.string
    content = soup.get_text()
    return {"title": title, "content": content, "url": url}

def scrape_discourse(start_date, end_date, base_url, output_file):
    all_posts = []
    for page in tqdm(range(1, 10)):  # Adjust as needed
        url = f"{base_url}?page={page}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            href = link["href"]
            if "/t/" in href and "tools-in-data-science" in href:
                post_url = f"https://discourse.onlinedegree.iitm.ac.in{href}"
                post = fetch_post_data(post_url)
                all_posts.append(post)

    with open(output_file, "w") as f:
        json.dump(all_posts, f, indent=2)

# Example usage:
# scrape_discourse("2025-01-01", "2025-04-14", "https://discourse.onlinedegree.iitm.ac.in/c/courses/tools-in-data-science", "data/discourse_data.json")
