from flask import Flask, render_template

app = Flask(__name__)
app.config[
    'SECRET_KEY'] = ("b'\xa9\xe8\xb2\x12\x8f\xf3\xda\xbc\xd9\x0e\xaf\xb7\x13\xd1\xb0\xe9\x7a\xc4\x2b\x3c\x1a\x1d\x9e"
                     "\x8f'")


@app.route('/')
def index():
    return render_template('home/index.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/signup')
def signup():
    return render_template('auth/signup.html')


@app.route('/resetpassword')
def resetpassword():
    return render_template('auth/resetpassword.html')


if __name__ == '__main__':
    app.run()
