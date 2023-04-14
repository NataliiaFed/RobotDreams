import json

import werkzeug.exceptions
from . import app, db
from flask import request, redirect, render_template, session, url_for
import re
import os
from .models import User, Book, Purchase

app.secret_key = os.getenv('SECRET_KEY')


def is_logged_in(func):
    def wrap(*args, **kwargs):
        if request.method == 'GET':
            if not session.get('user'):
                return redirect(url_for('login'))
            else:
                return func(*args, **kwargs)
        elif request.method == 'POST':
            return redirect(url_for('logout'))
    return wrap


@is_logged_in
@app.route('/users', methods=['GET', 'POST'])
def users():
    count = request.args.get('size')
    users = User.query.limit(count).all()
    return render_template('users.html', users=users, user_session=session.get('user'))


@is_logged_in
@app.route('/books', methods=['GET', 'POST'])
def books():
    count = request.args.get('size')
    books = Book.query.limit(count).all()
    return render_template('books.html', books=books, user_session=session.get('user'))


@is_logged_in
@app.route('/purchases', methods=['GET', 'POST'])
def purchases():
    count = request.args.get('size')
    purchases = Purchase.query.limit(count).all()
    return render_template('purchases.html', purchases=purchases, user_session=session.get('user'))


@is_logged_in
@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def get_user_id(user_id):
    user = db.get_or_404(User, user_id)
    return render_template('users_id.html', user=user, user_session=session.get('user'))


@is_logged_in
@app.route('/books/<book_id>', methods=['GET', 'POST'])
def get_book_id(book_id):
    book = db.get_or_404(Book, book_id)
    return render_template('books_id.html', book=book, user_session=session.get('user'))


@is_logged_in
@app.route('/purchases/<int:purchase_id>', methods=['GET', 'POST'])
def get_purchase_id(purchase_id):
    purchase = db.get_or_404(Purchase, purchase_id)
    return render_template('purchases_id.html', purchase=purchase, user_session=session.get('user'))


@app.post('/newuser')
def create_user():
    user = User(
        first_name=request.json.get('first_name'),
        last_name=request.json.get('last_name'),
        age=request.json.get('age')
    )
    db.session.add(user)
    db.session.commit()
    return f'User {user.id} created', 201


@app.post('/newbook')
def create_book():
    book = Book(
        title=request.json.get('title'),
        author=request.json.get('author'),
        year=request.json.get('year'),
        price=request.json.get('price'),
    )
    db.session.add(book)
    db.session.commit()
    return f'Book {book.title} created', 201


@app.route('/newpurchase', methods=['GET', 'POST'])
def create_purchase():
    if request.method == 'GET':
        return render_template('newpurchase.html')

    elif request.method == 'POST':
        user_id = int(request.form.get("user_id")) # entered ID
        user = User.query.get(user_id)

        book_id = int(request.form.get("book_id"))
        book = Book.query.get(book_id)

        if user != None and book != None:
            purchase = Purchase(user_id=user_id, book_id=book_id)
            db.session.add(purchase)
            db.session.commit()
            return f'Purchase {purchase.id} created', 201
        else:
            return f"User {user_id} and/or book {book_id} doesn't exist"


@is_logged_in
@app.route('/params', methods=['GET', 'POST'])
def params():
    return render_template('params.html', attributes=request.args, user_session=session.get('user'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':

        username = request.form.get("username")
        password = request.form.get("password")

        password_pattern = "^(?=.*?[A-Z])(?=.*?[0-9]).{8,}$"
        password_check = re.match(password_pattern, password)

        if username == "" or password == "":
            return 'Missing data', 400
        elif len(username) < 5:
            return f'Usernames must be at least 5 characters long, {password_check}', 400
        elif password_check == None:
            return 'Password must be at least 8 characters long, contain at least one number and one uppercase letter', 400
        else:
            session['user'] = username
            return redirect(url_for('users'))


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user')
    return redirect(url_for('login'))


@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return "<div>Not found</div>"


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def default_500(e):
    return "<div>Internal Server Error</div>"


@app.get('/')
def links():
    res = """
    <div><a target="_blank" href="/login">Login</a></div>
    <div><a target="_blank" href="/users">Users</a></div>
    <div><a target="_blank" href="/books">Books</a></div>
    <div><a target="_blank" href="/params">Params</a></div>"""
    return res