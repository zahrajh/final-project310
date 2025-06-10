import urllib.request
import urllib.parse
import json


def get_books(subject):

    subject_encoded = urllib.parse.quote(subject.lower().replace(" ", "_"))
    url = f"https://openlibrary.org/subjects/{subject_encoded}.json"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            books = data.get("works", [])[:10]  # Top 10 books

            # Format books with title and authors
            results = []
            for book in books:
                title = book.get("title", "Unknown Title")
                authors = [a.get("name", "Unknown Author") for a in book.get("authors", [])]
                results.append((title, authors))

            return results

    except Exception as e:
        print("Error fetching data:", e)
        return []



def get_news(keyword, api_key="ee61095926264b199dc1d5757a13fc3a"):
    base_url = "https://newsapi.org/v2/everything"
    query = urllib.parse.quote(keyword)
    url = f"{base_url}?q={query}&apiKey={api_key}"

    print(f"Fetching news for: {keyword}")

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            result = json.loads(data)

            if result['status'] == 'ok':
                articles = result['articles'][:10]  # Only print top 10 articles
                print(f"Found {len(articles)} articles containing '{keyword}':\n")
                for article in articles:
                    title = article.get('title')
                    if title:
                        print(f"- {title}")
            else:
                print("Error from API:", result.get('message', 'Unknown error'))
    except Exception as e:
        print("Error fetching news:", e)



