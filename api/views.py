import json


from flask import render_template
from .models import Book
from . import app
from .db import db
from .forms import BookForm
from logger import logger

@app.route('/',methods=['POST', 'GET'])
def home():
    bookForm = BookForm()

    if bookForm.validate_on_submit():
        book = Book(
            name=bookForm.name.data,
            pages=bookForm.pages.data,
            author_name=bookForm.author_name.data
        )
        try:
            db.session.add(book)
            db.session.commit()
            logger.debug(f"book '{book.name}' added successfully")
        except Exception as ex:
            logger.error(ex)

    return render_template('addbook.html', bookForm=bookForm)

@app.route('/books')
def books():
    books: list[Book] = Book.query.all()
    booksList = []
    for book in books:
        booksList.append({
            "name": book.name, 
            "pages": book.pages,
            "author_name": book.author_name
        }) 
    response = booksList
    logger.info(response)
    return response