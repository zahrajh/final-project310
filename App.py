from flask import Flask, render_template, request, redirect, url_for
from Functions import get_books, get_news

app = Flask(__name__)
books_cache = []  # simple global cache to hold books temporarily


@app.route('/', methods=['GET', 'POST'])
def index():
    global books_cache
    books = []
    topic = None

    if request.method == 'POST':
        topic = request.form.get('topic')
        books = get_books(topic)[:5]  # show top 5 books
        books_cache = books



    return render_template('index.html', books=books, topic=topic)


@app.route('/book/<int:book_id>')
def book_articles(book_id):
    if 0 <= book_id < len(books_cache):
        book = books_cache[book_id]
        articles_by_subject = []

        for sub in book.get("subjects", []):
            articles = get_news(sub)
            if articles:
                articles_by_subject.append({"subject": sub, "articles": articles})

        return render_template('book_articles.html', book=book, articles_by_subject=articles_by_subject)
    else:
        return "Book not found", 404


if __name__ == '__main__':
    app.run()
