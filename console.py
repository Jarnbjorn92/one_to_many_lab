import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author_1 = Author('J R R', 'Tolken')
author_repository.save(author_1)

book_1 = Book('Lord Of The Rings', 'Fantasy', author_1)
book_repository.save(book_1)

book_repository.select()