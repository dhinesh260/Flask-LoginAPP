from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8zabc\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        login = True
        name = session['username']
        return render_template('index.html', login=login, name=name)

    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if len(session) != 0:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'dhinesh' and password == 'kumar':
            session['username'] = request.form['username']
            print(len(session))
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if len(session) != 0:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        phno = request.form['phno']

        with open('details.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow((name, username, phno))
        
        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)




