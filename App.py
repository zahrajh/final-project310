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
        for title, authors in books:
            author_list = ", ".join(authors) if authors else "Unknown Author"
            print(f"- {title} — by {author_list}")

    return render_template('index.html', books=books, topic=topic)

if __name__ == '__main__':
    app.run()

