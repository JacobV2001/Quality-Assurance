from flask import Flask, render_template, request, redirect, url_for

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
