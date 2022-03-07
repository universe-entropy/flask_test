from flask import Flask, request, render_template    # render template use jinja
import os

app = Flask(__name__, template_folder='../templates')  # 

@app.route('/', methods=['GET', 'POST'])  # decorator to link url to function
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    else:
        return render_template('form.html', message='Wrong username or password', username=username)

if __name__ == '__main__':
    print(os.getcwd())
    app.run()    # flask default localhost:5000

