from flask import Flask, render_template, redirect, request
from repositories import author_repository
from repositories import book_repository
from models.book import Book


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)


