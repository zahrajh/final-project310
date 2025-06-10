from flask import Flask, render_template, request
from Functions import get_books, get_news

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    books = []
    topic = None

    if request.method == 'POST':
        topic = request.form.get('topic')

        get_news(topic)

        books = get_books(topic)
        print(f"Found {len(books)} books on '{topic}':")
        for book in books:
            title = book.get("title", "Unknown Title")
            authors = book.get("authors", [])
            author_list = ", ".join(authors) if authors else "Unknown Author"
            print(f"- {title} — by {author_list}")

        articles_by_subject = []
        if books:
            for sub in books[0].get("subject", []):
                arts = get_news(sub)  # must return list of dicts, not print
                if arts:
                    articles_by_subject.append((sub, arts))

    return render_template('index.html', books=books, topic=topic, articles_by_subject=articles_by_subject)


if __name__ == '__main__':
    app.run()