
from .models import Book
from . import app 

@app.route('/books')
def books():
    # books: list[Book] = Book.query.all()
    # response = []
    # for book in books:
    #     response.append({
    #         book.name, 
    #         book.pages,
    #         book.author_name
    #     }) 
    return {
        "book":"50 tips to write better Python code"
    }