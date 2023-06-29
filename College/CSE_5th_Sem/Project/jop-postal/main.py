
from flask import Flask, render_template, request, redirect, session, flash,url_for,session
from datetime import datetime
from flask_mysqldb import MySQL
# from flask_session import Session

#Instance Of Flask
app = Flask(__name__)

#Configuration Of Mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'job_portal'
app.config['SECRET_KEY'] = 'the random string' 
# app.config["SESSION_PERMANENT"] = True

#Instance Of Mysql
mysql = MySQL(app)
# app.secret_key  = 'the random string'

# Home Pages
@app.route('/')
def index():
    return render_template('index.html')



#Signin Pages
@app.route('/Signin')
def Signin():
    return render_template('signin.html')



# Signup Pages
@app.route('/Signup')
def Signup():
    return render_template('signup.html')



# Sign_out Pages
@app.route('/Sign_out')  
def Sign_out():  
    if 'email' in session:  
        session.pop('email',None)  
        return render_template('signin.html')  
    else:
        return render_template('signin.html')
        # return '<h3>User Already Sign Out</h3>'

# Profile Pages
@app.route('/Profile/<string:profileid>',methods=['GET','POST'])#profileid
def Profile(profileid):    
    cur=mysql.connection.cursor()
    cur.execute("SELECT name,age,gender,contact,email,password,profileid FROM users WHERE profileid=profileid "%(profileid))
    all_fetch = cur.fetchall()
    cur.close()      
    return render_template('profile.html', all_fetched=all_fetch)
    




# Dashboard Pages
@app.route('/Dashboard',methods=['GET','POST'])
def Dasborad():
    if request.method == 'POST':
        session['email'] = request.form['email']
        email = session['email']
        return render_template('dashboard.html')
    return render_template('dashboard.html')
    


# Work Pages
@app.route('/Work')
def Work():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM post")
    users = cur.execute("SELECT * FROM users")
    post = cur.fetchall()
    return render_template('work.html',posts=post,users=users)



# Delete_card Pages
@app.route('/Delete_card/<string:id_data>', methods=['GET'])
def Delete_card(id_data):
    try:
        # flash("Record Has Been Deleted Successfully")
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM post WHERE id=%s"%(id_data))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Work'))#render Through Function
        
    except mysql.connection.Error as error:
        print("Database Update Failed !: {}".format(error))
        mysql.connection.rollback()
        return redirect('/Work')



# Update_card Pages
@app.route('/Update_card/<string:Editid>',methods=['GET','POST'])
def Update_card(Editid):
    try:
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,job_title,job_experience,job_description FROM post WHERE id=%s "%(Editid))
        all_fetch = cur.fetchall()
        cur.close()
        msg=''
        if request.method == 'POST':
            Job_title = request.form['job_title']
            Job_experience = request.form['job_experience']
            Job_description = request.form['job_description']
            Time = request.form['time']
            cur=mysql.connection.cursor()
            # cur.execute("UPDATE post SET job_title=%s,job_experience=%s,job_description=%s,time=%s WHERE id=%s "%(Job_title,Job_experience,Job_description,Time,Editid))
            cardup = "UPDATE post SET job_title=%s,job_experience=%s,job_description=%s,time=%s WHERE id=%s "
            cur.execute(cardup,(Job_title,Job_experience,Job_description,Time,Editid))
            mysql.connection.commit()
            cur.close()
            msg="Updated Successfull"
            return render_template('update_card.html',msg=msg)
        return render_template('update_card.html', all_fetched = all_fetch)
        
    except mysql.connection.Error as error:
        print("Database Update Failed !: {}".format(error))
        mysql.connection.rollback()
        return redirect('/Work')
   



@app.route('/hire')
def hire():
    return render_template('hire.html')




@app.route('/card')
def post():
    return render_template('create_job.html')



# Addpost Page
@app.route('/addpost',methods=['GET','POST'])
def addpost():
    if request.method =='POST':
        try:
            job_title=request.form['job_title']
            job_description=request.form['job_description']
            job_experience=request.form['job_experience']
            time=request.form['time']
            cur=mysql.connection.cursor()
            cur.execute(''' INSERT INTO post(job_title,job_experience, 	job_description,time) VALUES(%s,%s,%s,%s)''',(job_title,job_experience,job_description,time))
            mysql.connection.commit()
            cur.close()
            return redirect('/Work')
        except mysql.connection.Error as error:
            print("Database Update Failed !: {}".format(error))
            mysql.connection.rollback()
            return redirect('/card')
    return redirect('/card')



# signup_validation Page
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
