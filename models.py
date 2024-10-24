from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Database Model for Inventory
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(100))
    publication_date = db.Column(db.Date)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
