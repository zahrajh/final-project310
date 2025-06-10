from flask import Flask, render_template, request
import json
from Functions import get_books, get_news
#BOOOKS
if __name__ == "__main__":

    subject = "science fiction"
    print(f"Testing get_books('{subject}')...\n")
    books = get_books(subject)

    print(f"Found {len(books)} books on '{subject}':\n")
    for idx, (title, authors) in enumerate(books, start=1):
        author_list = ", ".join(authors) if authors else "Unknown Author"
        print(f"{idx}. {title} — by {author_list}")

#NEWS
api_key = "ee61095926264b199dc1d5757a13fc3a"
keyword = "Science fiction"
get_news(keyword, api_key)
