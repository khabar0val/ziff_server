from flask import Flask, request, render_template

from src.models.auth import sign_up

app = Flask(__name__)

@app.route('/signup', methods = ['POST'])
def signup(username, password):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        sign_up(username, password)

    else:
        return render_template('signup.html', username=username, password=password)

if __name__ == '__main__':
    app.run()
