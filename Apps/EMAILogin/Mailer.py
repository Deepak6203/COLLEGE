# from flask import *  
# from flask_mail import *  
# from random import *   
from flask import Flask,render_template,request  
from flask_mail import Mail,Message 
from random import randrange 

  
app = Flask(__name__)

  
app.config["MAIL_SERVER"]='smtp.gmail.com'          # Name/IP address of email server
app.config["MAIL_PORT"] = 465                       # Port number of server used
app.config["MAIL_USERNAME"] = 'get7job@gmail.com'   # User name of sender
app.config['MAIL_PASSWORD'] = 'kxbmlyzjftjmrvjw'    # password of sender
# app.config['MAIL_PASSWORD'] = 'sltfllseqgbwtwxb'  # password of sender
app.config['MAIL_USE_TLS'] = False                  # Enable/disable Transport Security Layer encryption
app.config['MAIL_USE_SSL'] = True                   # Enable/disable Secure Sockets Layer encryption

  
# Create an instance of Mail class.  
mail = Mail(app)  #class constructor

# otp = randint(111111,999999)  
otp = randrange(000000, 999999)

 
@app.route('/')  
def index():  
    return render_template("index.html")  

 
@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]  
      
    msg = Message(' GET-JOB ',sender = 'get7job@gmail.com', recipients = [email])  
    # mess= "GET-JOB OTP ==> "
    mess= "GET-JOB OTP ==> "
    mass = "<br/>By Deepak Singh"
    
    msg.body = mess + str(otp) + mass  
    # msg.body = "GET-JOB OTP IS " + str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  

 
@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3>Email verified successfully</h3>"  
    return "<h3>failure</h3>"  
  



if __name__ == '__main__':  
    app.run(debug = True)  