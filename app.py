import hashlib
import base64
from flask import Flask, render_template, request, abort
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f"Это профиль пользователя с ID {user_id}"

@app.route('/md5', methods=['GET', 'POST'])
def md5_hash():
    """
    Вычисление MD5 хеша строки.
    ---
    parameters:
      - name: str
        in: query
        type: string
        required: true
        description: Строка для вычисления MD5 хеша
    responses:
      200:
        description: MD5 хеш строки
        schema:
          type: string
      400:
        description: Пожалуйста, предоставьте строку для вычисления MD5 хеша.
    """
    if request.method == 'POST':
        input_str = request.form.get('str', '')
    else:
        input_str = request.args.get('str', '')

    if input_str:
        md5_result = hashlib.md5(input_str.encode()).hexdigest()
        return md5_result
    else:
        abort(400, description="Пожалуйста, предоставьте строку для вычисления MD5 хеша.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)