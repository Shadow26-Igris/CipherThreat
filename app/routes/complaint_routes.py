from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from app import get_db_connection

complaint_routes = Blueprint('complaint_routes', __name__)  

@complaint_routes.route('/complaint', methods=['GET', 'POST'])
def complaint():
    if 'user_id' not in session:
        return redirect(url_for('auth_routes.login'))

    if request.method == 'POST':
        complaint_text = request.json.get('complaint')  # Use .json to parse the JSON body

        if not complaint_text:
            return jsonify({"message": "Complaint text is required."}), 400  # Bad request

        user_id = session['user_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO complaints (user_id, complaint) VALUES (%s, %s)', (user_id, complaint_text))
        conn.commit()
        conn.close()

        return jsonify({"message": "Complaint submitted successfully."}), 200  # Successful response

    return render_template('complaint.html')

    pass

    
