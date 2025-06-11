import urllib.request
import urllib.parse
import json


def get_books(subject):

    subject_encoded = urllib.parse.quote(subject.lower().replace(" ", "_"))
    url = f"https://openlibrary.org/subjects/{subject_encoded}.json?details=true"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            books = data.get("works", [])[:3]

            results = []
            for book in books:
                title = book.get("title", "Unknown Title")
                authors = [a.get("name", "Unknown Author") for a in book.get("authors", [])]
                subjects = book.get("subject", [])[:3]
                cover_id = book.get("cover_id")

                results.append({
                    "title": title,
                    "authors": authors,
                    "subjects": subjects,
                    "cover_id": cover_id
                })

            if books and "subject" in books[0]:
                subjects = books[0]["subject"][:5]  # top 5 subjects
                for sub in subjects:
                    articles = get_news(sub)
                    if articles:
                        print(f"\nArticles on “{sub}”:")
                        for art in articles:
                            print(f"- {art['title']} ({art.get('source')})")

            return results


    except Exception as e:
        print("Error fetching data:", e)
        return []



def get_news(keyword, api_key="0b8d12a66aa3412eb225388a9408b11f"):
    base_url = "https://newsapi.org/v2/everything"
    query = urllib.parse.quote(keyword)
    url = f"{base_url}?q={query}&apiKey={api_key}"

    print(f"Fetching news for: {keyword}")

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            result = json.loads(data)

            if result['status'] == 'ok':
                articles = result['articles'][:5]
                return [
                    {
                        "title": article.get("title"),
                        "source": article.get("source", {}).get("name", "Unknown Source")
                    }
                    for article in articles if article.get("title")
                ]
            else:
                print("Error from API:", result.get('message', 'Unknown error'))
                return []
    except Exception as e:
        print("Error fetching news:", e)
        return []