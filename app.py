from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f"Это профиль пользователя с ID {user_id}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)