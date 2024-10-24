from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv, json
from flask import Response
import os

# Initialize Flask app
app = Flask(__name__)

# SQLite configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Database Model for Inventory
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100))
    publication_date = db.Column(db.Date)
    isbn = db.Column(db.String(13), unique=True, nullable=False)


# Routes for the frontend and backend
@app.route('/')
def index():
    # Fetch all books from the database
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        publication_date_str = request.form['publication_date']
        isbn = request.form['isbn']

        # Convert publication_date from string to date object
        publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d').date() if publication_date_str else None

        new_book = Book(title=title, author=author, genre=genre, publication_date=publication_date, isbn=isbn)
        db.session.add(new_book)
        db.session.commit()

        return redirect('/')
    return render_template('add_book.html')


@app.route('/filter-books', methods=['GET'])
def filter_books():
    # Filter books based on form input
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    query = Book.query
    if title:
        query = query.filter(Book.title.like(f'%{title}%'))
    if author:
        query = query.filter(Book.author.like(f'%{author}%'))
    if genre:
        query = query.filter_by(genre=genre)

    books = query.all()
    return render_template('books.html', books=books)


# Export to CSV
@app.route('/export-csv', methods=['GET'])
def export_csv():
    books = Book.query.all()

    # Create a CSV response
    def generate():
        data = [['Title', 'Author', 'Genre', 'Publication Date', 'ISBN']]
        for book in books:
            data.append([book.title, book.author, book.genre, book.publication_date, book.isbn])

        output = '\n'.join([','.join(map(str, row)) for row in data])
        yield output

    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=books.csv"})


@app.route('/export-json', methods=['GET'])
def export_json():
    books = Book.query.all()
    book_list = []

    for book in books:
        book_data = {
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'isbn': book.isbn
        }

        # Check if publication_date is not None before formatting
        if book.publication_date:
            book_data['publication_date'] = book.publication_date.isoformat()
        else:
            book_data['publication_date'] = None  # or you can leave it out

        book_list.append(book_data)

    # Use json.dumps with indent for pretty printing
    json_output = json.dumps(book_list, indent=4)

    return Response(json_output, mimetype='application/json',
                    headers={"Content-Disposition": "attachment;filename=books.json"})

@app.route('/delete-book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This creates the 'books.db' file and the Book table
    app.run(debug=True)
