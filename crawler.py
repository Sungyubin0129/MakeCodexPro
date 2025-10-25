import sys
import requests
from bs4 import BeautifulSoup


def crawl(url: str):
    """Fetch the given URL and return its title and list of links."""
    resp = requests.get(url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title found"
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return title, links


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        title, links = crawl(url)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(1)

    print("Page title:", title)
    print("Links found:")
    for link in links:
        print(link)
