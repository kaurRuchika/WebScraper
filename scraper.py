import requests
from bs4 import BeautifulSoup
import csv

# Target website (can be modified)
URL = "https://example.com"

def fetch_html(url):
    """Fetch HTML content from the given URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code}: Unable to fetch page.")
        return None

def parse_html(html):
    """Parse HTML using BeautifulSoup and extract data."""
    soup = BeautifulSoup(html, "html.parser")
    
    # Example: Extract all article titles and links
    articles = []
    for article in soup.find_all("h2"):  # Modify based on website structure
        title = article.text.strip()
        link = article.find("a")["href"] if article.find("a") else "No link"
        articles.append({"title": title, "link": link})
    
    return articles

def save_to_csv(data, filename="output.csv"):
    """Save extracted data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    print("Fetching data...")
    html = fetch_html(URL)
    
    if html:
        extracted_data = parse_html(html)
        if extracted_data:
            save_to_csv(extracted_data)
            print("Scraping complete!")
        else:
            print("No data found.")
