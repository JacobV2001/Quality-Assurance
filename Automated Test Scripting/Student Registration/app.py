from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            return render_template('error.html', message="Invalid username or password.")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        parent_name = request.form['parent_name']
        email = request.form['email']
        phone = request.form['phone']

        # backend validation
        errors = []
        if not name or len(name) < 2 or not name.replace(" ", "").isalpha:
            errors.append("Invalid name. Name must be at least 2 characters long and only contain letters.")
        if not age or not age.isdigit() or int(age) < 3 or int(age) > 80:
            errors.append("Invalid age. Age must be a number between 3 and 80.")
        if not grade or grade not in ["Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8"]:
            errors.append("Invalid grade. Please select a valid grade.")
        if not parent_name or not parent_name.replace(" ", "").isalpha():
            errors.append("Invalid parent name. Name must be at least 2 characters long and only contain letters.")
        if not email or not re.match(r"^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z{2,}$]", email):
            errors.append("Invalid email address.")
        #if not phone or not phone.isdigit or len(phone) != 10:
        #    errors.append("Invalid phone number. Phone number must be exactly 10 digits.")
        
        if errors:
            return render_template('error,html', message="; ".join(errors))

        user_data = {
            'name': name,
            'age': age,
            'grade': grade,
            'parent_name': parent_name,
            'email': email,
            'phone': phone
        }

        return render_template('confirm.html', **user_data)

    return render_template('register.html')

@app.route('/error')
def error():
    return render_template('error.html', message="An unexpected error occurred.")

if __name__ == '__main__':
    app.run(debug=True)
