from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, jsonify
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date
import data
import random
import os

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'transaxi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.secret_key = os.urandom(16)

#init MySQL
mysql = MySQL(app)

# Users = data.Users()
# Wallets = data.Wallets()
# Transactions = data.Transactions()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# class SubForm(Form):
#     email = EmailField('Email', [validators.DataRequired(), validators.Email()])

@app.route('/users/<string:id>', methods=['GET'])
def users(id):
    # for usr in Users:
    #     name = usr['name']
    #     email = usr['email']
    #     password = usr['password']
    #     wallet_id = usr['wallet_id']
    #     role = usr['role']

    #     cur = mysql.connection.cursor()
    #     cur.execute('INSERT INTO users(name, email, password, wallet_id, role) VALUES(%s, %s, %s, %s, %s)', (name, email, password, wallet_id, role))

    #     mysql.connection.commit()
    #     cur.close()

    # for wlt in Wallets:
    #     user_id = wlt['user_id']
    #     amount = wlt['amount']

    #     cur = mysql.connection.cursor()
    #     cur.execute('INSERT INTO wallets(user_id, amount) VALUES(%s, %s)', (user_id, amount))

    #     mysql.connection.commit()
    #     cur.close()
    # for trns in Transactions:
    #     user_from = trns['user_from']
    #     user_to = trns['user_to']
    #     amount = trns['amount']

    #     cur = mysql.connection.cursor()
    #     cur.execute('INSERT INTO transactions(user_from, user_to, amount) VALUES(%s, %s, %s)', (user_from, user_to, amount))

    #     mysql.connection.commit()
    #     cur.close()

    # Create cursor
    cur = mysql.connection.cursor()

    # Get user by username
    result = cur.execute('SELECT * from users WHERE id=%s', (id,))

    data = cur.fetchone()
    return jsonify(data)

@app.route('/wallets/<string:id>', methods=['GET'])
def wallets(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get user by username
    result = cur.execute('SELECT * from wallets WHERE id=%s', (id,))

    data = cur.fetchall()
    return jsonify(data)
    
@app.route('/transact', methods=['GET', 'POST'])
def transact():
    if request.method == 'GET':
        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute('SELECT users.id, users.name, wallets.amount from users INNER JOIN wallets on users.wallet_id=wallets.id WHERE users.id=%s', (id,))

        data = cur.fetchall()
        
# class RegisterForm(Form):
#     name = StringField('Name', [validators.Length(min=1, max=50)])
#     username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
#     email = EmailField('Email', [validators.DataRequired(), validators.Email()])
#     password = PasswordField('Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords do not match.'),
#     ])
#     confirm = PasswordField('Confirm Password')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # Get data from form
#         name = form.name.data
#         email = form.email.data
#         username = form.username.data
#         password = sha256_crypt.encrypt(str(form.password.data))

#         # Create cursor
#         cur = mysql.connection.cursor()

#         # Get user by username
#         result = cur.execute('SELECT * from users WHERE email=%s', (email,))

#         data = cur.fetchone()
        
#         if result and data['username']:
#             flash('Email already in use', 'danger')
#             return render_template('register.html', form=form)
#         elif result and not data['username']:
#             cur.execute("UPDATE users SET name=%s, username=%s, password=%s WHERE email=%s", (name, username, password, email))
#         elif not result:
#             cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

#         # Commit to db
#         mysql.connection.commit()

#         # Close connection
#         cur.close()

#         flash('You are now registered and can log in', 'success')
#         return redirect(url_for('index'))
#     return render_template('register.html', form=form)

# class LoginForm(Form):
#     email = EmailField('Email', [validators.DataRequired(), validators.Email()])
#     password = PasswordField('Password', [validators.DataRequired()])

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # Get data from form
#         email = form.email.data
#         password_candidate = form.password.data

#         # Create cursor
#         cur = mysql.connection.cursor()

#         # Get user by username
#         result = cur.execute('SELECT * from users WHERE email = %s', [email])

#         if result:
#             # Get stored hash
#             data = cur.fetchone()
#             password = data['password']
#             username = data['username']

#             # Compare passwords
#             if sha256_crypt.verify(password_candidate, password):
#                 session['logged_in'] = True
#                 session['username'] = username

#                 if data['role'] == 'admin':
#                     session['admin'] = True
#                     flash('You are now logged in as admin', 'success')
#                     return redirect(url_for('dashboard'))
#                 else:
#                     session['admin'] = False
#                     flash('You are now logged in', 'success')
#                     return redirect(url_for('index'))

#             else:
#                 error = 'Invalid email or password'
#                 return render_template('login.html', error=error, form=form)
#         else:
#             error = 'Invalid email or password'
#             return render_template('login.html', error=error, form=form)
#         cur.close()
#     return render_template('login.html', form=form)

# # Check if user is logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, please log in', 'danger')
#             return redirect(url_for('login'))
#     return wrap

# # Check if user is admin
# def is_admin(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if ('logged_in' in session) and session['admin']:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized', 'danger')
#             return redirect(url_for('login'))
#     return wrap

# @app.route('/logout')
# @is_logged_in
# def logout():
#     session.clear()
#     flash('You are now logged out', 'success')
#     return redirect(url_for('login'))

# @app.route('/dashboard')
# @is_admin
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/dashboard/users')
# @is_admin
# def users():
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Get Articles
#     result = cur.execute("SELECT * FROM users WHERE subscribed!=0")

#     users = cur.fetchall()

#     # Close Connection
#     cur.close()

#     if result > 0:
#         return render_template('users.html', users=users)
#     else:
#         msg = 'No Users Found'
#         return render_template('users.html', msg=msg)


# @app.route('/dashboard/companies')
# @is_admin
# def companies():
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Get Articles
#     result = cur.execute("SELECT * FROM companies")

#     companies = cur.fetchall()

#     # Close Connection
#     cur.close()

#     if result:
#         return render_template('companies.html', companies=companies)
#     else:
#         msg = 'No Companies Found'
#         return render_template('companies.html', msg=msg)

# @app.route('/dashboard/users/email')
# @is_admin
# def users_email():
#     mailto = ""
    
#     # Create cursor
#     cur = mysql.connection.cursor()
    
#     # Get Articles
#     result = cur.execute("SELECT email FROM users WHERE subscribed=1")

#     emails = cur.fetchall()

#     for email in emails:
#         mailto += email['email'] + ";"

#     # Close Connection
#     cur.close()

#     return redirect('https://mail.google.com/mail/u/0/?view=cm&fs=1&to=' + mailto + '&tf=1')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port="80")
