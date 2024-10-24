
# Book Inventory Management System

This project is a simple web-based book inventory management system. It allows users to add, filter, delete, and export book records. The backend is powered by Flask and SQLite, and the frontend uses HTML, CSS, and Bootstrap for a clean user interface.

## Features

- Add, filter, and delete books in the inventory.
- Export book records to CSV and JSON formats.
- Responsive design using Bootstrap.
- Fullstack application with Flask (backend) and SQLite (database).

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Libraries**:
  - Flask-SQLAlchemy: For database management
  - Flask: For routing and handling HTTP requests

## Prerequisites

To run the project locally, ensure you have the following installed:

- Python 3.x
- Virtualenv (recommended)

## Setup and Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/book-inventory.git
cd book-inventory
```

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts ctivate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

You don't need to manually create the database; it will be created automatically when the app runs. Ensure the following line is included in your `app.py` file to create the database and tables:

```python
db.create_all()
```

### 5. Run the Flask Application

Start the Flask development server by running the following command:

```bash
flask run
```

### 6. Access the Application

After starting the server, open your browser and navigate to:

```
http://127.0.0.1:5000/
```

## Application Features

### 1. Add a Book

- Navigate to the "Add Book" page using the "Add New Book" button.
- Fill in the form fields (Title, Author, Genre, Publication Date, ISBN).
- Submit the form to add the book to the inventory.

### 2. Filter Books

- Use the filter form on the home page to search for books by title, author, or genre.
- The list of books will dynamically update based on the filters applied.

### 3. Delete a Book

- Use the "Delete" button next to each book entry to remove it from the inventory.

### 4. Export Book Records

- You can export the book records as a CSV or JSON file using the respective export buttons.

## License

This project is licensed under the MIT License.
