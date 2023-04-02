import werkzeug.exceptions
from . import app
from flask import request, redirect, render_template, session, url_for
import random
import re

app.secret_key = b'secret'


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        current = session.get('user')
        if current:
            names = ['Natasha', 'Masha', 'Pasha', 'Sasha', 'Dasha', 'Lesha', 'Petya', 'Fedya', 'Senya', 'Vanya']
            random_names = []

            count_param = request.args.get('count')
            if count_param != None and count_param.isdigit():
                count = int(count_param)
            else:
                count = random.randint(0, 50)

            for i in range(count):
                name = random.choice(names)
                random_names.append(name)

            return render_template('users.html', names_context=random_names, user=current)

        else:
            return redirect(url_for('login'))

    elif request.method == 'POST':
        return redirect(url_for('logout'))


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        current = session.get('user')
        if current:
            books = ['Kobzar', 'Harry Potter', 'The Lord of the Rings', '1984', 'Fahrenheit 451', 'Romeo and Julie',
                     'Alice in Wonderland', 'The Adventures of Huckleberry Finn', 'Pride and Prejudice ', 'Moby Dick ']
            random_books = []

            count_param = request.args.get('count')
            if count_param != None and count_param.isdigit():
                count = int(count_param)
            else:
                count = random.randint(0, 50)

            for i in range(count):
                random_books.append(random.choice(books))

            return render_template('books.html', books_context=random_books, user=current)

        else:
            return redirect(url_for('login'))

    elif request.method == 'POST':
        return redirect(url_for('logout'))


@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def get_user_id(user_id):
    if request.method == 'GET':
        current = session.get('user')
        if current:
            return render_template('users_id.html', id=user_id, user=current)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        return redirect(url_for('logout'))


@app.route('/books/<book_title>', methods=['GET', 'POST'])
def get_book_title(book_title):
    if request.method == 'GET':
        current = session.get('user')
        if current:
            return render_template('books_title.html', title=book_title, user=current)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        return redirect(url_for('logout'))


@app.route('/params', methods=['GET', 'POST'])
def params():
    if request.method == 'GET':
        current = session.get('user')
        if current:
            return render_template('params.html', attributes=request.args, user=current)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        return redirect(url_for('logout'))


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