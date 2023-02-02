from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import pdb
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, authors_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    pdb.set_trace()
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['user_id'])
        book = Book(
            row['title'], 
            row['genre'],
            author, 
            row['id']
            )
        books.append(book)
    return books


def select(id):
    task = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['authors_id'])
        book = Book(
            result['title'], 
            result['genre'], 
            author, 
            result['id'] )
    return book


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)