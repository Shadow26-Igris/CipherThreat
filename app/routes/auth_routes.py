# app/routes/auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app as app
from app.utils.db import get_db_connection 
from app.__init__ import bcrypt
from app.utils.login import generate_reset_token, send_reset_email
from datetime import datetime, timedelta

auth_routes = Blueprint('auth_routes', __name__)



# Register route (Change the path to /register)
@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        phone = request.form['phone']
        address = request.form['address']
        nationality = request.form['nationality']
        gender = request.form['gender']
        password = request.form['password']

        # Hash the password before saving to the database
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if username or email exists
        conn = get_db_connection()  
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s OR email = %s', (username, email))
        user = cursor.fetchone()

        if user:
            flash('Username or Email already exists. Please choose another one.', 'danger')
            cursor.close()
            conn.close()    
            return redirect(url_for('auth_routes.register'))

        try:
            # Insert new user into the database
            cursor.execute(
                """INSERT INTO users (username, email, age, phone, address, nationality, gender, password)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (username, email, age, phone, address, nationality, gender, hashed_password)
            )
            conn.commit()
            cursor.close()
            conn.close()    
            flash('Registration successful!', 'success')
            return redirect(url_for('auth_routes.login'))
        except Exception as e:
            flash('Error: ' + str(e), 'danger')
            cursor.close()
            conn.close()    
            return redirect(url_for('auth_routes.register'))

    return render_template('register.html')

# Login route (no change needed, just make sure it's the only /login route)
@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Please enter both username and password.", "danger")
            return redirect(url_for('auth_routes.login'))

        conn = get_db_connection()
        cursor = conn.cursor()  

        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            if bcrypt.check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                flash("Login successful!", "success")
                return redirect(url_for('complaint_routes.complaint'))
            else:
                flash("Invalid password.", "danger")
        else:
            flash("User not found.", "danger")

        return redirect(url_for('home')) # Redirect to home page if login fails    
    
    return render_template('login.html')

# Forgot password route (change path to /forgot-password)
@auth_routes.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()

        if user:
            reset_token = generate_reset_token()
            token_expiry = datetime.now() + timedelta(hours=1)

            cursor.execute('UPDATE users SET reset_token = %s, token_expiry = %s WHERE email = %s',
                           (reset_token, token_expiry, email))
            conn.commit()

            send_reset_email(email, reset_token)

            flash("A password reset link has been sent to your email.", "success")
        else:
            flash("Email not found.", "danger")

    return render_template('forgot_password.html')

# Reset password route (change path to /reset-password/<reset_token>)
@auth_routes.route('/reset-password/<reset_token>', methods=['GET', 'POST'])
def reset_password(reset_token):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE reset_token = %s AND token_expiry > %s', (reset_token, datetime.now()))
    user = cursor.fetchone()

    if request.method == 'POST':
        new_password = request.form['password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('reset_password.html', reset_token=reset_token)

        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        cursor.execute('UPDATE users SET password = %s, reset_token = NULL, token_expiry = NULL WHERE reset_token = %s',
                       (hashed_password, reset_token))
        conn.commit()

        flash("Your password has been reset successfully.", "success")
        return redirect(url_for('auth_routes.login'))

    if user:
        return render_template('reset_password.html', reset_token=reset_token)
    else:
        flash("Invalid or expired token.", "danger")
        return redirect(url_for('auth_routes.login'))
