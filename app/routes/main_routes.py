from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.index import get_db_connection

main_routes = Blueprint('main_routes', __name__)

# Home route
@main_routes.route('/')
def home():
   
    return render_template('index.html')

@main_routes.route('/cybercrime')
def cybercrime():
    return render_template('cybercrime.html')

@main_routes.route('/cyberthreat')
def cyberthreat():
    return render_template('cyberthreat.html')

@main_routes.route('/bs')
def bs():
    return render_template('bs.html')


# Volunteer submission route
@main_routes.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        skills = request.form['skills']
        availability = request.form['availability']
        motivation = request.form['motivation']

        # Save the volunteer information to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO volunteers (name, email, skills, availability, motivation)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, skills, availability, motivation))
        conn.commit()
        conn.close()

        flash('Thank you for volunteering! We will contact you soon.', 'success')
        return redirect(url_for('main_routes.volunteer'))

    return render_template('volunteer.html')

# Volunteers list route
@main_routes.route('/volunteers')
def volunteers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM volunteers')
    volunteers = cursor.fetchall()
    conn.close()
    return render_template('volunteers_list.html', volunteers=volunteers)
