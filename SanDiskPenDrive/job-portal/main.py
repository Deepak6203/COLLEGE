
from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'job_portal'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Signup')
def Signup():
    return render_template('signup.html')


@app.route('/Signin')
def Signin():
    return render_template('signin.html')


@app.route('/Dashboard')
def Dasborad():
    return render_template('dashboard.html')


@app.route('/Work')
def Work():
    return render_template('work.html')

@app.route('/hire')
def hire():
    return render_template('hire.html')



@app.route('/signup_validation', methods=['GET', 'POST'])
def signup_validation():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            gender = request.form['gender']
            contact = request.form['contact']
            email = request.form['email']
            password = request.form['password']
            cur = mysql.connection.cursor()
            cur.execute(''' INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)''',
                        (name, age, gender, contact, email, password))
            mysql.connection.commit()
            cur.close()
            return redirect('/Signin')
        except mysql.connection.Error as error:
            print("Database Update Failed !: {}".format(error))
            mysql.connection.rollback()
            return redirect('/Signup')

    return redirect('/Signup')


@app.route('/signin_validation', methods=['GET', 'POST'])
def signin_validation():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            cur = mysql.connection.cursor()
            cur.execute('''SELECT * FROM users WHERE email=%s and password=%s''',(email,password))
            user=cur.fetchone()
            cur.close()
            print(user)
            if user is None:
                return redirect('/Signin')
            else:
                return redirect('/Dashboard')
        except mysql.connection.Error as error:
            print("Database Update Failed !: {}".format(error))
            mysql.connection.rollback()
            return redirect('/Signin')
    else:
        return redirect('/Signin')
            



if __name__ == '__main__':
    app.run(debug=True)
